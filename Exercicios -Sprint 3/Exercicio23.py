class Calculo:
    def somar(self, x, y): #Função para a soma
        return x + y

    def subtrair(self, x, y): #Função para subtração
        return x - y

# Valores para testar
x = 4
y = 5

# Criando uma instância 
calculo = Calculo()

# Chamando os métodos e imprimindo os resultados
print(f"Somando: {x} + {y} = {calculo.somar(x, y)}")
print(f"Subtraindo: {x} - {y} = {calculo.subtrair(x, y)}")