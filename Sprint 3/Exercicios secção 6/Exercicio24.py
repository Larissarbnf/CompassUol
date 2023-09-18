class Ordenadora:
    def __init__(self, listaBaguncada): 
        self.listaBaguncada = listaBaguncada #Atributo

    def ordenacaoCrescente(self): #Método
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self): #Método
        return sorted(self.listaBaguncada, reverse=True)

# Instanciando o primeiro objeto com lista [3,4,2,1,5]
crescente = Ordenadora([3,4,2,1,5])

# Instanciando o segundo objeto com lista [9,7,6,8]
decrescente = Ordenadora([9,7,6,8])

# Imprimindo o resultado da ordenação crescente e decrescente
print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
