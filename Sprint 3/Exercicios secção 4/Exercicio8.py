def palindromo (palavra): #Cria uma função para verificar se a palavra é palindromo
  if palavra == palavra[::-1]: #A função compara a palavra original com a palavra invertida.
    return True 
  
lista=['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for palavra in lista: #Um loop para percorrer a lista
    if palindromo(palavra): #chamando a função para fazer a verificação
        print(f'A palavra: {palavra} é um palíndromo') #Se a palavra for palindromo imprime na tela.
    else:
        print(f'A palavra: {palavra} não é um palíndromo')#Se nãofor palindromo imprime na tela.