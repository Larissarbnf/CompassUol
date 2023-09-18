def removeduplicados(lista): #A função removeduplicados converte a lista para um conjunto (set) e depois volta a converter para uma lista antes de retornar.
    return list(set(lista))

# Lista de exemplo
lista_original = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

nova_lista = removeduplicados(lista_original)
print(nova_lista) #Imprime na tela a nova lista