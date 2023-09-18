class Pessoa:
    def __init__(self, id):
        self.__nome = None  # Atributo privado
        self.id = id  # Atributo público

    @property #Metodo
    def nome(self): 
        return self.__nome #Retornando o valor do atributo privado

    @nome.setter #Metodo usado para modificar o valor de __nome
    def nome(self, novo_nome):
        self.__nome = novo_nome #estamos atribuindo o novo valor de __nome 
# Exemplo de uso
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)