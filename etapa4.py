def contar_filmes_maior_bilheteria():
    with open('actors.csv', 'r') as arquivo:
        linhas = arquivo.readlines()

        # Removendo o cabeçalho
        cabecalho = linhas[0]
        linhas = linhas[1:]

        # Criar um dicionário para contar os filmes
        contagem_filmes = {}

        for linha in linhas:
            partes = linha.split(',')
            filme = partes[4].strip()  # A coluna "#1 Movie" está no índice 4

            if filme in contagem_filmes:
                contagem_filmes[filme] += 1
            else:
                contagem_filmes[filme] = 1

        # Ordenar os filmes por quantidade de aparições
        filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: x[1], reverse=True)

        return filmes_ordenados

# Contar filmes de maior bilheteria
filmes_ordenados = contar_filmes_maior_bilheteria()

# Escrever no arquivo etapa-4.txt
with open('etapa-4.txt', 'w') as arquivo_etapa_4:
    for sequencia, (filme, quantidade) in enumerate(filmes_ordenados, 1):
        arquivo_etapa_4.write(f'{sequencia} - O filme {filme} aparece {quantidade} vez(es) no dataset\n')

# Listar e imprimir na tela
for sequencia, (filme, quantidade) in enumerate(filmes_ordenados, 1):
    print(f'{sequencia} - O filme {filme} aparece {quantidade} vez(es) no dataset')
