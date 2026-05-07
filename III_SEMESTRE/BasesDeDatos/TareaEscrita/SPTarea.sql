CREATE PROCEDURE sp_ProcesarVacacionesBatch
    @inFechaOperacion DATE
    , @outResultCode INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;


    BEGIN TRY

        SET @outResultCode = 0;

        DECLARE
            @LastIdEmail INT
            , @QSolicitudes INT
            , @LastIdMovimiento INT
            , @isFeriado BIT
            , @UltimaLlaveProcesada INT
            , @UltimaLlaveLote INT
            , @SecActual INT
            , @SecMax INT
            , @IdSolicitudActual INT
            , @IdEmpleadoActual INT
            , @IdUsuarioActual INT
            , @DiasRestantesActual INT
            , @SaldoActualEmpleadoActual DECIMAL(10,2)
            , @PostInIPActual VARCHAR(32)
        ;

        SET @isFeriado = 0;
        SET @UltimaLlaveProcesada = 0;
        SET @UltimaLlaveLote = 0;

        SELECT @UltimaLlaveProcesada = ISNULL(MAX(UltimaLlave), 0)
        FROM EventLog
        WHERE idEventType IN (1, 3);

        SET @UltimaLlaveLote = @UltimaLlaveProcesada;

        
        -- Verificar si la fecha de operación es feriado
        -- Si es feriado, no se procesa nada
        IF EXISTS (SELECT 1 FROM Feriados WHERE Fecha = @inFechaOperacion)
        BEGIN
            SET @isFeriado = 1;
        END

        IF @isFeriado = 0
        BEGIN

            -- ============================================================
            -- Tabla variable con las solicitudes a procesar
            -- Solicitudes aprobadas donde la fecha de operación está
            -- entre FechaDesde y FechaHasta
            -- ============================================================
            DECLARE @SolicitudesAProcesar TABLE (
                SEC INT IDENTITY(1,1)
                , idSolicitud INT
                , idEmpleado INT
                , idUsuario INT
                , SaldoDiasSolicitado INT
                , DiasRestantes INT
                , SaldoActualEmpleado DECIMAL(10,2)
                , PostInIP VARCHAR(32)
            );

            INSERT INTO @SolicitudesAProcesar (
                idSolicitud
                , idEmpleado
                , idUsuario
                , SaldoDiasSolicitado
                , DiasRestantes
                , SaldoActualEmpleado
                , PostInIP
            )
            SELECT
                SV.id
                , SV.idEmpleado
                , SV.idUserPostByubie        -- idUsuario
                , SV.SaldoDiasSolicitado
                -- Días restantes = días totales de la solicitud menos los ya consumidos
                , DATEDIFF(DAY, @inFechaOperacion, SV.FechaHasta)
                , E.SaldoVacaciones
                , SV.PostInIP
            FROM SolicitudVacaciones SV
            INNER JOIN Empleado E ON E.id = SV.idEmpleado
            WHERE SV.EstadoSolicitud = 'Aprobado'
                AND @inFechaOperacion BETWEEN SV.FechaDesde AND SV.FechaHasta
                AND SV.id > @UltimaLlaveProcesada
            ORDER BY SV.id;

            SET @SecActual = 1;
            SELECT @SecMax = MAX(SEC) FROM @SolicitudesAProcesar;
            SET @QSolicitudes = 0;

            WHILE @SecActual <= ISNULL(@SecMax, 0)
            BEGIN
                SELECT
                    @IdSolicitudActual = S.idSolicitud
                    , @IdEmpleadoActual = S.idEmpleado
                    , @IdUsuarioActual = S.idUsuario
                    , @DiasRestantesActual = S.DiasRestantes
                    , @SaldoActualEmpleadoActual = S.SaldoActualEmpleado
                    , @PostInIPActual = S.PostInIP
                FROM @SolicitudesAProcesar S
                WHERE S.SEC = @SecActual;

                SET @UltimaLlaveLote = @IdSolicitudActual;

                BEGIN TRANSACTION

                    -- ============================================================
                    -- Insertar email de notificación
                    -- ============================================================
                    INSERT INTO Email (idEmpleado, Texto)
                    VALUES (
                        @IdEmpleadoActual,
                    'Esperamos que ud esta disfrutando de sus vacaciones, aun le faltan ' 
                        + CAST(@DiasRestantesActual AS VARCHAR(10)) 
                        + ' dias de vacaciones según su solicitud aprobada, su nuevo saldo de vacaciones de '
                        + CAST(@SaldoActualEmpleadoActual - 1 AS VARCHAR(10))   -- saldo después del débito de hoy
                        + ' dias.'
                    );

                    SET @LastIdEmail = SCOPE_IDENTITY();

                    -- ============================================================
                    -- Insertar movimiento en MovimientoVac
                    -- ============================================================
                    INSERT INTO MovimientoVac (
                        idEmpleado
                        , idTipoMovimientos
                        , idTextoEmail
                        , Fecha
                        , Monto
                        , EsInvisible
                        , NuevoSaldo
                        , IdPostByUser
                        , PostInIP
                    )
                    VALUES (
                    @IdEmpleadoActual
                    , 5                     -- id del movimiento Debito de vacaciones (inventado ya que no tenemos acceso a las tablas). 
                    , @LastIdEmail
                    , @inFechaOperacion
                    , 1
                    , 0
                    , @SaldoActualEmpleadoActual - 1
                    , @IdUsuarioActual
                    , @PostInIPActual
                    );

                    SET @LastIdMovimiento = SCOPE_IDENTITY();

                    -- =======================================================================
                    -- Insertar en MovDebitoXSolcitud para relacionar solicitud con movimiento
                    -- =======================================================================
                    INSERT INTO MovDebitoXSolcitud (idMovimiiento, idSolicitud)
                    VALUES (@LastIdMovimiento, @IdSolicitudActual);

                    -- =====================================================
                    -- Actualizar SaldoDiasSolicitado en SolicitudVacaciones
                    -- =====================================================
                    UPDATE SV
                    SET SV.SaldoDiasSolicitado = SV.SaldoDiasSolicitado - 1
                    FROM SolicitudVacaciones SV
                    WHERE SV.id = @IdSolicitudActual;

                    -- =======================================
                    -- Actualizar SaldoVacaciones del empleado
                    -- =======================================
                    UPDATE E
                    SET E.SaldoVacaciones = E.SaldoVacaciones - 1
                    FROM Empleado E
                    WHERE E.id = @IdEmpleadoActual;

                COMMIT TRANSACTION;

                SET @QSolicitudes = @QSolicitudes + 1;
                SET @SecActual = @SecActual + 1;
            END

            -- ===================================================================
            -- Actualizar bitacora para llevar control de la úlƟma llave procesada
            -- ===================================================================
            INSERT INTO EventLog (idEventType, EventDate, Descripcion, UltimaLlave)
            VALUES (
                1,
                GETDATE(),
                'Procesadas ' + CAST(@QSolicitudes AS VARCHAR(10)) + ' solicitudes',
                @UltimaLlaveLote
            );
        END
        ELSE
        BEGIN
            INSERT INTO EventLog (idEventType, EventDate, Descripcion, UltimaLlave)
            VALUES (
                2,
                GETDATE(),
                'No se procesa: fecha feriada',
                @UltimaLlaveProcesada
            );
        END

    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        SET @outResultCode = 1;

        INSERT INTO EventLog (idEventType, EventDate, Descripcion, UltimaLlave)
        VALUES (
            3,
            GETDATE(),
            'Error: ' + ERROR_MESSAGE(),
            ISNULL(@IdSolicitudActual, @UltimaLlaveLote)
        );
    END CATCH
END;
GO