def imprimeparametros(*args, **kwargs): #Essa recebe um número variável de parâmetros não-nomeados (*args) e um número variável de parâmetros nomeados (**kwargs).
    
    for i in args: #Inicia um loop for que irá iterar sobre os argumentos não nomeados args
        print(i)

    for parametro, valor in kwargs.items(): # Inicia um loop for que irá iterar sobre os argumentos nomeados kwargs.
        print(valor)

# Chamando a função com os parâmetros fornecidos
imprimeparametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
