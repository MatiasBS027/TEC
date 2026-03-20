USE EmpleadosDB;
GO

-- SP 1: Lista todos los empleados ordenados por nombre
CREATE PROCEDURE dbo.sp_GetEmpleados
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Id, Nombre, Salario
    FROM   dbo.Empleado
    ORDER  BY Nombre ASC;
END;
GO
