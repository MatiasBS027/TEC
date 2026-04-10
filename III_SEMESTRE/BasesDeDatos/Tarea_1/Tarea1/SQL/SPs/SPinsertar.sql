USE EmpleadosDB;
GO

-- SP 2: Inserta un empleado, valida duplicado por nombre
CREATE PROCEDURE dbo.sp_InsertEmpleado
    @Nombre    VARCHAR(128),
    @Salario   MONEY,
    @Resultado INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1 FROM dbo.Empleado
        WHERE LOWER(LTRIM(RTRIM(Nombre))) = LOWER(LTRIM(RTRIM(@Nombre)))
    )
    BEGIN
        SET @Resultado = 1;
        RETURN;
    END

    INSERT INTO dbo.Empleado (Nombre, Salario)
    VALUES (@Nombre, @Salario);

    SET @Resultado = 0;
END;
GO