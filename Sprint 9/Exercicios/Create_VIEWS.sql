CREATE VIEW DimCliente AS
SELECT
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM Cliente;
 
SELECT * FROM DimCliente;

CREATE VIEW DimCombustivel AS
SELECT
    idCombustivel,
    tipoCombustivel
FROM Combustivel;

CREATE VIEW DimVendedor AS
SELECT
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM vendedor;

CREATE VIEW DimCarro AS
SELECT
    idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    idCombustivel
FROM Carro;


CREATE VIEW FatoLocacao AS
SELECT
    L.idLocacao,
    L.idCliente,
    L.idCarro,
    L.dataLocacao,
    L.horaLocacao,
    L.qtdDiaria,
    L.vlrDiaria,
    L.dataEntrega,
    L.horaEntrega,
    L.idVendedor,
    C.nomeCliente,
    CC.tipoCombustivel,
    V.nomeVendedor,
    CR.kmCarro,
    CR.classiCarro,
    CR.marcaCarro,
    CR.modeloCarro,
    CR.anoCarro
FROM Locacao L
JOIN Cliente C ON L.idCliente = C.idCliente
JOIN Carro CR ON L.idCarro = CR.idCarro
JOIN Combustivel CC ON CR.idCombustivel = CC.idCombustivel
JOIN vendedor V ON L.idVendedor = V.idVendedor;
