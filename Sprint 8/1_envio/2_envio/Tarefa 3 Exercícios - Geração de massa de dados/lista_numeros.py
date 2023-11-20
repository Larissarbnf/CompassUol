import random

# Passo 1: Gerar lista de 250 inteiros aleatórios
lista_inteiros = [random.randint(1, 1000) for _ in range(250)]

# Passo 2: Inverter a lista
lista_inteiros.reverse()

# Passo 3: Imprimir o resultado
print(lista_inteiros)
