-- ==========================
-- Matias Benavides Sandoval - 2025102376
-- Sebastián Ramírez Abarca - 2025071280
-- ==========================

CREATE PROCEDURE sp_ProcesarVacacionesBatch
    @inFechaOperacion DATE
    , @outResultCode INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY

        SET @outResultCode = 0;

        DECLARE
            @SecActual INT
            , @SecMax INT
            , @idEventLogActual INT
            , @LastIdEmail INT
            , @LastIdMovimiento INT
            , @UltimaLlaveProcesada INT
            , @IDTIPOMOVIMIENTO INT
            , @TIPOEVENTOBATCH INT
            , @TIPOEVENTOFERIADO INT
        ;

        SET @SecActual = 1;
        SET @IDTIPOMOVIMIENTO = 5          -- Numero elegido para id de debito vacaciones
        SET @TIPOEVENTOBATCH = 1           -- Numero elegido para id de tipo evento batch vacaciones
        SET @TIPOEVENTOFERIADO = 2         -- Numero elegido para id de tipo evento feriado

        -- =============================================================
        -- Verificar si ya se corrio completo para la fecha de operacion
        -- =============================================================
        IF EXISTS (
            SELECT 1
            FROM dbo.EventLog EL
            WHERE EL.IdEventType = @TIPOEVENTOBATCH
                AND EL.EventDate = @inFechaOperacion
                AND EL.QuantityIdsToBeProcessed = EL.QuantityIdsProcessed
        )
        BEGIN
            SET @outResultCode = 50001;
            RETURN;
        END;

        -- ==========================
        -- Verificar si es feriado
        -- ==========================
        IF EXISTS (
            SELECT 1
            FROM dbo.Feriados F
            WHERE F.Fecha = @inFechaOperacion
        )
        BEGIN

            INSERT INTO dbo.EventLog (
                IdEventType
                , EventDate
                , Descripcion
                , QuantityIdsToBeProcessed
                , QuantityIdsProcessed
                , LastIdProcessed
            )
            VALUES(
                @TIPOEVENTOFERIADO
                , @inFechaOperacion
                , 'Fecha de operación es feriado. No se aplican débitos.'
                , 0
                , 0
                , 0
            );
            RETURN;
        END;


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
        ORDER BY SV.id;

        SELECT @SecMax = MAX(S.SEC)
        FROM @SolicitudesAProcesar S;


        IF EXISTS (
            SELECT 1
            FROM dbo.EventLog EL
            WHERE EL.IdEventType = @TIPOEVENTOBATCH
                AND EL.EventDate = @inFechaOperacion
                AND EL.QuantityIdsToBeProcessed <> EL.QuantityIdsProcessed
        )
        BEGIN
            
            -- Si falló continuar donde quedó
            SELECT TOP 1 @idEventLogActual = EL.id
            FROM dbo.EventLog EL
            WHERE EL.IdEventType = @TIPOEVENTOBATCH
                AND EL.EventDate = @inFechaOperacion
            ORDER BY EL.id DESC;

            SELECT @SecActual = S.SEC + 1
            FROM @SolicitudesAProcesar S
            INNER JOIN dbo.EventLog EL ON EL.LastIdProcessed = S.idSolicitud
            WHERE EL.id = @idEventLogActual;
        END

        ELSE
        BEGIN
            
            -- Es primera vez corriendo
            INSERT INTO dbo.EventLog(
                IdEventType
                , EventDate
                , Descripcion
                , QuantityIdsToBeProcessed
                , QuantityIdsProcessed
                , LastIdProcessed
            )
            VALUES (
                @TIPOEVENTOBATCH
                , @inFechaOperacion
                , 'Inicio proceso batch vacaciones'
                , @SecMax
                , 0
                , 0
            );

            SET @idEventLogActual = SCOPE_IDENTITY();
        END;

        -- ============================
        -- Iteracion por cada solicitud
        -- ============================
        WHILE @SecActual <= ISNULL(@SecMax, 0)
        BEGIN
           

            BEGIN TRANSACTION tSolicitud;

                -- ============================================================
                -- Insertar emails de notificación
                -- ============================================================
                INSERT INTO dbo.Email (idEmpleado, Texto)
                SELECT
                    S.idEmpleado,
                    'Esperamos que ud esta disfrutando de sus vacaciones, aun le faltan ' 
                        + CAST(S.DiasRestantes AS VARCHAR(10)) 
                        + ' dias de vacaciones según su solicitud aprobada, su nuevo saldo de vacaciones de '
                        + CAST(S.SaldoActualEmpleado - 1 AS VARCHAR(10))   -- saldo después del débito de hoy
                        + ' dias.'
                FROM @SolicitudesAProcesar S
                WHERE S.SEC = @SecActual;

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
                SELECT
                    S.idEmpleado
                    , @IDTIPOMOVIMIENTO 
                    , @LastIdEmail
                    , @inFechaOperacion
                    , 1
                    , 0
                    , S.SaldoActualEmpleado - 1
                    , S.idUsuario
                    , S.PostInIP
                FROM @SolicitudesAProcesar S
                WHERE S.SEC = @SecActual;

                SET @LastIdMovimiento = SCOPE_IDENTITY();

                -- =======================================================================
                -- Insertar en MovDebitoXSolcitud para relacionar solicitud con movimiento
                -- =======================================================================
                INSERT INTO dbo.MovDebitoXSolicitud (idMovimiento, idSolicitud)
                SELECT 
                    @LastIdMovimiento
                    , S.idSolicitud
                FROM @SolicitudesAProcesar S
                WHERE S.SEC = @SecActual;

                -- =====================================================
                -- Actualizar SaldoDiasSolicitado en SolicitudVacaciones
                -- =====================================================
                UPDATE SV
                SET SV.SaldoDiasSolicitado = SV.SaldoDiasSolicitado - 1
                FROM dbo.SolicitudVacaciones SV
                INNER JOIN @SolicitudesAProcesar S ON S.idSolicitud = SV.id
                WHERE S.SEC = @SecActual;

                -- =======================================
                -- Actualizar SaldoVacaciones del empleado
                -- =======================================
                UPDATE E
                SET E.SaldoVacaciones = E.SaldoVacaciones - 1
                FROM dbo.Empleado E
                INNER JOIN @SolicitudesAProcesar S ON S.idEmpleado = E.id
                WHERE S.SEC = @SecActual;

                -- ============================================
                -- Actualizar EventLog con UltimaLlaveProcesada
                -- ============================================
                SELECT @UltimaLlaveProcesada = S.idSolicitud
                FROM @SolicitudesAProcesar S
                WHERE S.SEC = @SecActual;

                UPDATE EL
                SET EL.LastIdProcessed = @UltimaLlaveProcesada
                    , EL.QuantityIdsProcessed = EL.QuantityIdsProcessed + 1
                FROM dbo.EventLog EL
                WHERE EL.id = @idEventLogActual;

            COMMIT TRANSACTION tSolicitud;

            SET @SecActual = @SecActual + 1;
        END;

    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION tSolicitud;

        SET @outResultCode = 50002

    END CATCH;
END;
GO