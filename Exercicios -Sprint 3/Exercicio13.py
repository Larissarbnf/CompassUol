def my_map(lista, funcao): #Essa função usa uma compreensão de lista para aplicar a função a cada elemento da lista e retorna uma nova lista com os resultados.
    return [funcao(elemento) for elemento in lista]

# Função que calcula a potência de 2
def potenciaDe2(x):
    return (x**2)

# Lista de entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Aplica my_map com a função de potência de 2
resultado = my_map(lista, potenciaDe2)

print(resultado) #Imprime o resultado
