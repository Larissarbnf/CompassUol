-- Primeiramente eu desabilitei a verificação de chave primária, para não mudar os dados que eu tenho.
PRAGMA foreign_keys=off;

-- Removi a chave primária temporariamente
CREATE TABLE ClienteTemp AS
SELECT * FROM Cliente;

-- Depois inseri dados da tb_locacao na minha tabela cliente
INSERT INTO ClienteTemp (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Logo após restaurei a chave primária
DROP TABLE Cliente;
ALTER TABLE ClienteTemp RENAME TO Cliente;

-- E por fim reabilitei a verificação da chave primária.
PRAGMA foreign_keys=on;


-- Para a tabela CARRO, vou seguir o mesmo esquema anterior
PRAGMA foreign_keys=off;
CREATE TABLE CarroTemp AS
SELECT * FROM Carro;
INSERT INTO CarroTemp (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;
DROP TABLE Carro;
ALTER TABLE CarroTemp RENAME TO Carro;
PRAGMA foreign_keys=on;

-- Para a tabela COMBUSTIVEL, vou seguir o mesmo esquema anterior.
PRAGMA foreign_keys=off;
CREATE TABLE CombustivelTemp AS
SELECT * FROM Combustivel;
INSERT INTO CombustivelTemp (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;
DROP TABLE Combustivel;
ALTER TABLE CombustivelTemp RENAME TO Combustivel;
PRAGMA foreign_keys=on;

-- Para a tabela LOCACAO, vou seguir o mesmo esquema anterior
PRAGMA foreign_keys=off;
CREATE TABLE LocacaoTemp AS
SELECT * FROM Locacao;
INSERT INTO LocacaoTemp (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT
  idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;
DROP TABLE Locacao;
ALTER TABLE LocacaoTemp RENAME TO Locacao;
PRAGMA foreign_keys=on;


-- Para a tabela VENDEDOR, vou seguir o mesmo esquema anterior
PRAGMA foreign_keys=off;
CREATE TABLE VendedorTemp AS
SELECT * FROM Vendedor;
INSERT INTO VendedorTemp (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT
  idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;
DROP TABLE Vendedor;
ALTER TABLE VendedorTemp RENAME TO Vendedor;
PRAGMA table_info(VendedorTemp);
PRAGMA foreign_keys=on;



PRAGMA foreign_keys;

select * from Carro
select * from Vendedor 
select * from Locacao
select * from Cliente 
select * from Combustivel