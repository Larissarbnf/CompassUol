# Leitura dos números a partir de um arquivo
with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

# Filtrar  números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# 5 maiores valores pares
maiores_pares = sorted(pares, reverse=True)[:5]

# Calcular a soma dos 5 maiores valores pares
soma_maiores_pares = sum(maiores_pares)

# Imprimir os resultados
print(maiores_pares)
print(soma_maiores_pares)


