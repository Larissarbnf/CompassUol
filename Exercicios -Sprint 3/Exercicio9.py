#Você deve Utilizar a função enumerate().
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for a,b in enumerate(primeirosNomes): #Define duas variáveis a e b que serão utilizadas para armazenar os valores retornados por enumerate.
    print(f'{a} - {primeirosNomes[a]} {sobreNomes[a]} está com {idades[a]} anos') #Imprime na tela conforme solicitado
