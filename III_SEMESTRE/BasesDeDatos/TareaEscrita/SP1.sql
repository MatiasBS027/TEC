/*
    SP1.sql
    Plantilla de estudio para escribir paso a paso el SP batch de vacaciones.

    Idea docente:
    - Primero entiendes el flujo.
    - Luego escribes la sentencia exacta.
    - Si una columna no se ve clara en la captura, no se inventa: se marca como supuesto.

    Objetivo funcional del SP:
    - Procesar solicitudes aprobadas cuya fecha de operación cae dentro del rango.
    - Omitir el caso si la fecha es feriado para ese empleado.
    - Insertar email.
    - Insertar movimiento de vacaciones.
    - Insertar movimiento débito ligado a la solicitud.
    - Actualizar saldo días solicitado.
    - Actualizar saldo de vacaciones del empleado.
    - Dejar evidencia de la corrida en la bitácora conceptual.

    Este archivo está escrito para que lo puedas completar por encima.
    Los comentarios te dicen qué hace cada bloque y por qué existe.
*/

CREATE PROCEDURE sp_ProcesarVacacionesBatch
    @FechaOperacion DATE
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    -- Paso 0: validar la entrada.
    -- Si no hay fecha, no hay batch.
    IF @FechaOperacion IS NULL
    BEGIN
        RAISERROR('Parámetro @FechaOperacion no puede ser NULL',16,1);
        RETURN;
    END

    /*
        Supuestos confirmados por la captura y la conversación:
        - SolicitudVacaciones: id, idEmpleado, FechaDesde, FechaHasta, EstadoSolicitud,
            QDiasSolicitados, SaldoDiasSolicitado, idUserPostByUbie, PostInIP.
        - Empleado: id, SaldoVacaciones y campos de apoyo.
        - MovimientoVac: id, idEmpleado, idTipoMovimientos, idTextoEmail, Fecha,
            Monto, EsInvisible, NuevoSaldo, idPostByUser, PostInIP.
        - Email: id, idEmpleado, Texto.
        - MovDebitoXSolicitud: idMovimiento, idSolicitud.
        - EventLog: bitácora conceptual mínima.

        Si alguna columna no se usa en este SP, no pasa nada: solo se documenta.
    */

    BEGIN TRY
        BEGIN TRANSACTION;

        -- ============================================================
        -- Paso 1: construir el conjunto elegible.
        -- Aquí seleccionamos las solicitudes que sí deben entrar al batch.
        -- ============================================================
        IF OBJECT_ID('tempdb..#SolicitudesAProcesar') IS NOT NULL
            DROP TABLE #SolicitudesAProcesar;

        CREATE TABLE #SolicitudesAProcesar (
            idSolicitud INT PRIMARY KEY,
            idEmpleado INT NOT NULL,
            FechaDesde DATE,
            FechaHasta DATE,
            SaldoDiasSolicitud INT,
            SaldoActualEmpleado DECIMAL(10,2),
            DiasRestantes INT
        );

        -- Esta consulta forma la lista de trabajo del día.
        -- Si mañana cambian los nombres físicos, este es uno de los primeros sitios a ajustar.
        INSERT INTO #SolicitudesAProcesar (idSolicitud, idEmpleado, FechaDesde, FechaHasta, SaldoDiasSolicitud, SaldoActualEmpleado, DiasRestantes)
        SELECT
            sv.id,
            sv.idEmpleado,
            sv.FechaDesde,
            sv.FechaHasta,
            sv.SaldoDiasSolicitud,
            e.SaldoVacaciones,
            -- Días residuales: cuánto le falta para terminar su rango aprobado.
            DATEDIFF(DAY, @FechaOperacion, sv.FechaHasta) AS DiasRestantes
        FROM SolicitudVacaciones sv
        INNER JOIN Empleado e ON e.id = sv.idEmpleado
        WHERE (sv.CDVacSolicitados IS NOT NULL OR sv.CDVacSolicitados <> '')
            AND sv.EstadoSolicitud = 'Aprobado'
            AND @FechaOperacion BETWEEN sv.FechaDesde AND sv.FechaHasta;

        -- ============================================================
        -- Paso 2: bitácora conceptual.
        -- La idea es dejar evidencia de la corrida aunque el DDL exacto no esté cerrado.
        -- ============================================================
        /*
            Si la base trae EventLog, ese es el lugar natural para registrar:
            - fecha de operación
            - estado de la corrida
            - descripción resumida

            Si no se usa físicamente, este bloque sigue siendo útil como explicación
            del control del proceso.
        */
        -- TODO: registrar inicio de corrida en EventLog o tabla equivalente.

        -- ============================================================
        -- Paso 3: procesar una solicitud por vez.
        -- Aquí es donde el SP realmente “hace trabajo”.
        -- ============================================================

        DECLARE @idSolicitud INT, @idEmpleado INT, @SaldoDiasSolicitud INT, @SaldoActualEmpleado DECIMAL(10,2), @DiasRestantes INT;
        DECLARE @idMovimiento INT;

        WHILE EXISTS (SELECT 1 FROM #SolicitudesAProcesar)
        BEGIN
            SELECT TOP(1)
                @idSolicitud = idSolicitud,
                @idEmpleado = idEmpleado,
                @SaldoDiasSolicitud = SaldoDiasSolicitud,
                @SaldoActualEmpleado = SaldoActualEmpleado,
                @DiasRestantes = DiasRestantes
            FROM #SolicitudesAProcesar
            ORDER BY idSolicitud; -- orden determinista

            -- Savepoint: si algo falla en esta fila, solo se revierte esta parte.
            SAVE TRANSACTION ProcVac_SavePoint;

            BEGIN TRY
                -- 3.1) Validar feriado.
                -- Si la fecha aplica como feriado para este caso, se omite solo esta solicitud.
                IF EXISTS (SELECT 1 FROM Feriados WHERE Fecha = @FechaOperacion)
                BEGIN
                    -- TODO: registrar omisión por feriado.
                    DELETE FROM #SolicitudesAProcesar WHERE idSolicitud = @idSolicitud;
                    CONTINUE;
                END

                -- 3.2) Seguridad contra doble débito.
                -- Si ya existe un movimiento para esta solicitud en esta fecha, no se vuelve a tocar.
                IF EXISTS (
                    SELECT 1 FROM MovDebitoXSolicitud md
                    INNER JOIN MovimientoVac mv ON mv.id = md.idMovimiento
                    WHERE md.idSolicitud = @idSolicitud AND CONVERT(date, mv.Fecha) = @FechaOperacion
                )
                BEGIN
                    -- Ya estaba procesado -> omitir.
                    DELETE FROM #SolicitudesAProcesar WHERE idSolicitud = @idSolicitud;
                    CONTINUE;
                END

                -- 3.3) Validaciones de saldo.
                -- Política conservadora: no negativos.
                IF @SaldoDiasSolicitud <= 0
                BEGIN
                    -- La solicitud ya no tiene días para consumir.
                    -- TODO: registrar omisión por saldo de solicitud agotado.
                    DELETE FROM #SolicitudesAProcesar WHERE idSolicitud = @idSolicitud;
                    CONTINUE;
                END

                IF @SaldoActualEmpleado < 1
                BEGIN
                    -- El empleado no tiene saldo suficiente.
                    -- TODO: registrar omisión por saldo del empleado insuficiente.
                    DELETE FROM #SolicitudesAProcesar WHERE idSolicitud = @idSolicitud;
                    CONTINUE;
                END

                -- ============================================================
                -- 3.4) Acciones del negocio.
                -- Orden recomendado:
                --   a) email
                --   b) movimiento
                --   c) débito ligado a la solicitud
                --   d) actualización de saldos
                -- ============================================================

                -- a) Insertar Email.
                INSERT INTO Email (idEmpleado, Texto)
                VALUES (
                    @idEmpleado,
                    'Esperamos que ud esta disfrutando de sus vacaciones, aun le faltan ' +
                    CAST(@DiasRestantes AS VARCHAR(10)) +
                    ' dias de vacaciones según su solicitud aprobada, su nuevo saldo de vacaciones de ' +
                    CAST(@SaldoActualEmpleado - 1 AS VARCHAR(10)) + ' dias.'
                );

                -- b) Insertar MovimientoVac.
                -- Esta tabla es la evidencia del movimiento de vacaciones.
                -- TODO: aquí debes escribir el INSERT exacto con las columnas reales.
                -- TODO: capturar el id generado para usarlo en MovDebitoXSolicitud.
                -- Ejemplo mental: insertar empleado, tipo de movimiento, texto, fecha, monto y nuevo saldo.

                -- c) Insertar el movimiento débito ligado a la solicitud.
                -- Aquí se conecta el movimiento con la solicitud que lo originó.
                INSERT INTO MovDebitoXSolicitud (idMovimiento, idSolicitud)
                VALUES (@idMovimiento, @idSolicitud);

                -- d) Actualizar el saldo de días solicitado.
                UPDATE SolicitudVacaciones
                SET SaldoDiasSolicitud = SaldoDiasSolicitud - 1
                WHERE id = @idSolicitud;

                -- e) Actualizar el saldo de vacaciones del empleado.
                UPDATE Empleado
                SET SaldoVacaciones = SaldoVacaciones - 1
                WHERE id = @idEmpleado;

                -- f) Registrar detalle exitoso en bitácora conceptual.
                -- TODO: insertar descripción de éxito si la base trae EventLog.

                -- Quitar la fila de la lista temporal para seguir con la siguiente.
                DELETE FROM #SolicitudesAProcesar WHERE idSolicitud = @idSolicitud;

            END TRY
            BEGIN CATCH
                -- Si falla esta fila, deshacemos solo esta parte.
                ROLLBACK TRANSACTION ProcVac_SavePoint;
                DECLARE @ErrMsg NVARCHAR(4000) = ERROR_MESSAGE();
                -- TODO: registrar el error en EventLog o bitácora equivalente.

                -- Quitamos la fila para no quedar atrapados en el mismo error.
                DELETE FROM #SolicitudesAProcesar WHERE idSolicitud = @idSolicitud;
                CONTINUE;
            END CATCH
        END -- fin while

        -- ============================================================
        -- Paso 4: cierre de corrida.
        -- Si el modelo físico trae bitácora real, aquí se deja el resumen final.
        -- ============================================================
        -- TODO: registrar cierre exitoso en EventLog o tabla equivalente.

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
        DECLARE @ErrorMsg NVARCHAR(4000) = ERROR_MESSAGE();
        RAISERROR('Error en sp_ProcesarVacacionesBatch: %s',16,1,@ErrorMsg);
        RETURN;
    END CATCH

END
    