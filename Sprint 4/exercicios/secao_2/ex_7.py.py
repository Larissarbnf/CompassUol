def pares_ate(n: int):
    for i in range(2, n+1, 2):
        yield i

# Exemplo de uso
for numero in pares_ate(20):
    print(numero)


