CREATE PROCEDURE DeletarUsuario
    @Nome NVARCHAR(100),
    @CPF CHAR(11),
    @Telefone NVARCHAR(20)
AS
BEGIN
    SET NOCOUNT ON;

    DELETE FROM Usuarios
    WHERE Nome = @Nome
    AND CPF = @CPF
    AND Telefone = @Telefone;
END;
SELECT FROM Usuarios