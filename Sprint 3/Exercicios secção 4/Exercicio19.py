import random

random_list = random.sample(range(500), 50)
list_ordenada = sorted(random_list)

media = sum(random_list) / len(random_list) #soma
valor_minimo = min(random_list)
valor_maximo = max(random_list)

if len(list_ordenada) % 2 != 0: #Se lista for par
    mediana = list_ordenada[len(list_ordenada) // 2]
else: #Se lista for impar
    mediana = (list_ordenada[len(list_ordenada) // 2 - 1] + list_ordenada[len(list_ordenada) // 2]) / 2

# Imprimindo os resultados no formato solicitado
print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")