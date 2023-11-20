# Passo 1: Instalar a biblioteca names
# Execute no terminal: pip install names

# Passo 2: Importar as bibliotecas
import random
import time
import os
import names

# Passo 3: Definir parâmetros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar nomes aleatórios
aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

# Passo 5: Gerar arquivo de texto
with open('nomes_aleatorios.txt', 'w') as file:
    for nome in dados:
        file.write(nome + '\n')

# Passo 6: Verificar o conteúdo do arquivo
with open('nomes_aleatorios.txt', 'r') as file:
    conteudo = file.read()

print(conteudo)
