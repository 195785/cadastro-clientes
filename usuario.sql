CREATE PROCEDURE CadastrarClientes
    @Nome VARCHAR(100),
    @CPF VARCHAR(14),
    @Telefone VARCHAR(20)
AS
BEGIN
    INSERT INTO Usuarios (Nome, CPF, Telefone)
    VALUES (@Nome, @CPF, @Telefone);
END;

EXEC CadastrarClientes 'João Silva', '123.456.789-00', '(11) 9999-8888';
EXEC CadastrarClientes 'Maria Santos', '987.654.321-00', '(22) 7777-6666';

SELECT * FROM Usuarios;

EXEC CadastrarClientes 'pedro henrique', '579.820.610-09', '(11) 99850-3031';

SELECT * FROM Usuarios;
