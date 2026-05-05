CREATE PROCEDURE sp_ProcesarVacacionesBatch
    @FechaOperacion DATE
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    -- Verificar si la fecha de operación es feriado
    -- Si es feriado, no se procesa nada
    IF EXISTS (SELECT 1 FROM Feriados WHERE Fecha = @FechaOperacion)
    BEGIN
        PRINT 'Fecha de operación es feriado. No se aplican débitos.';
        RETURN;
    END

    BEGIN TRY
        BEGIN TRANSACTION;

        -- ============================================================
        -- Tabla temporal con las solicitudes a procesar
        -- Solicitudes aprobadas donde la fecha de operación está
        -- entre FechaDesde y FechaHasta
        -- ============================================================
        CREATE TABLE #SolicitudesAProcesar (
            idSolicitud         INT,
            idEmpleado          INT,
            SaldoDiasSolicitud  INT,
            DiasRestantes       INT,
            SaldoActualEmpleado DECIMAL(10,2)
        );

        INSERT INTO #SolicitudesAProcesar (
            idSolicitud,
            idEmpleado,
            SaldoDiasSolicitud,
            DiasRestantes,
            SaldoActualEmpleado
        )
        SELECT
            sv.id,
            sv.idEmpleado,
            sv.SaldoDiasSolicitud,
            -- Días restantes = días totales de la solicitud menos los ya consumidos
            DATEDIFF(DAY, @FechaOperacion, sv.FechaHasta) AS DiasRestantes,
            e.SaldoVacaciones
        FROM SolicitudVacaciones sv
        INNER JOIN Empleado e ON e.id = sv.idEmpleado
        WHERE sv.CDVacSolicitados IS NOT NULL          -- aprobadas
            AND sv.EstadoSolicitud = 'Aprobado'
            AND @FechaOperacion BETWEEN sv.FechaDesde AND sv.FechaHasta;

        -- ============================================================
        -- Insertar emails de notificación
        -- ============================================================
        INSERT INTO Email (idEmpleado, Texto)
        SELECT
            s.idEmpleado,
            'Esperamos que ud esta disfrutando de sus vacaciones, aun le faltan ' 
                + CAST(s.DiasRestantes AS VARCHAR(10)) 
                + ' dias de vacaciones según su solicitud aprobada, su nuevo saldo de vacaciones de '
                + CAST(s.SaldoActualEmpleado - 1 AS VARCHAR(10))   -- saldo después del débito de hoy
                + ' dias.'
        FROM #SolicitudesAProcesar s;

        DROP TABLE #SolicitudesAProcesar;

        COMMIT TRANSACTION;
        END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
END CATCH;
END