def divlista(lista):
    tamanho = int(len(lista) /3) #Dividindo a lista em 3 partes
    lista1=lista[:tamanho] # 1 parte da lista
    lista2=lista[tamanho:tamanho*2] # 2 parte da lista
    lista3=lista[tamanho*2:] # 3 parte da lista
    return lista1,lista2,lista3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(divlista(lista)[0], end=' ')
print(divlista(lista)[1], end=' ')
print(divlista(lista)[2])
