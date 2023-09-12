def primo(num): #define uma função chamada primo que verifica se um número é primo.
    if num < 2: # Verifica se o número num é menor que 2, o que inclui o 0 e o 1.
        return False
    for i in range(2, int(num**0.5) + 1): #Inicia um loop que percorre todos os números de 2 até a raiz quadrada de "num" arredonda para cima mais 1. 
        if num % i == 0:
            return False
    return True

# Itera através dos números de 1 a 100
for numero in range(1, 101):
    if primo(numero):
        print(numero) #Imprime na tela os números primos