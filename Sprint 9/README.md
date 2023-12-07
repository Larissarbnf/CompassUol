Pontuando o primeiro Exercício da Sprint 9:

## <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/DBeaver_logo.png" width="25"> Usando o Dbeaver:

Primeiro fiz a criação de tabelas pelo Dbeaver, que está dentro da pasta de Exercicios. Coloquei todas as fotos do dados que obtive nas tabelas criadas.
Criei tabelas para Cliente, Combustivel, Vendedor, Carro e Locação.

### Cliente:
Armazena informações sobre os clientes, como nome, cidade, estado e país.
Chave primária (idCliente) para identificar exclusivamente cada cliente.

### Combustivel:
Mantém os tipos de combustíveis disponíveis.
Chave primária (idCombustivel) para identificar exclusivamente cada tipo de combustível.
Essa tabela pode ser referenciada por outras tabelas (como a tabela Carro) para indicar o tipo de combustível utilizado por um carro.

### Vendedor:
Contém dados sobre os vendedores, incluindo nome, sexo e estado.
Chave primária (idVendedor) para identificar exclusivamente cada vendedor.

### Carro:
Armazena informações específicas sobre os carros, como quilometragem, classificação, marca, modelo e ano.
Possui uma chave primária (idCarro) para identificar exclusivamente cada carro.
Contém uma chave estrangeira (idCombustivel) que se relaciona com a tabela Combustivel, indicando o tipo de combustível utilizado pelo carro.

### Locacao:
Registra informações sobre as locações de carros, como cliente, carro, data, hora, quantidade diária, valor diário, data de entrega, hora de entrega e vendedor.
Possui uma chave primária (idLocacao) para identificar exclusivamente cada locação.

## Locacao precisa de referência de Carro, Cliente e Vendedor:

#### Cliente: 
A chave estrangeira idCliente em Locacao estabelece uma relação com a tabela Cliente. 
Isso permite associar cada locação a um cliente específico, garantindo que a referência ao cliente seja válida.

#### Carro: 
A chave estrangeira idCarro em Locacao está relacionada à tabela Carro. Essa relação indica qual carro está sendo alugado em cada locação,
garantindo que a referência ao carro seja válida.

#### Vendedor:
A chave estrangeira idVendedor em Locacao está relacionada à tabela Vendedor. 
Isso permite associar cada locação a um vendedor específico, garantindo a validade da referência ao vendedor.

## Carro precisa de referência de Combustivel:

A chave estrangeira idCombustivel em Carro está relacionada à tabela Combustivel. Isso é útil para indicar o tipo de combustível que um determinado carro utiliza. Essa relação garante que a referência ao tipo de combustível seja válida e consistente.

# Diagrama feito com o DBeaver:
 ![Diagrama](https://github.com/Larissarbnf/CompassUol/blob/main/Sprint%209/Exercicios/Diagrama1.png)
