def soma_numeros(string_numeros):
    numeros = [int(num) for num in string_numeros.split(',')] #Divide a string em uma lista de strings usando split(','), converte cada string em um número inteiro e armazena os números em uma lista.
    soma = sum(numeros) #Calcula a soma dos números usando a função sum
    return soma

# String de números
string_numeros = "1,3,4,6,10,76"

# Chama a função e imprime a soma
soma = soma_numeros(string_numeros)
print(soma)