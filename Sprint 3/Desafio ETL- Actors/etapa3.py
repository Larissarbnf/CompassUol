def encontrar_maior_media_gross_por_filme():
    with open('actors.csv', 'r') as arquivo:
        linhas = arquivo.readlines()

        # Removendo o cabeçalho
        cabecalho = linhas[0]
        linhas = linhas[1:]

        maior_media_gross = 0
        ator_maior_media_gross = ''

        for linha in linhas:
            partes = linha.split(',')
            ator = partes[0]
            media_gross = float(partes[3])  # A coluna "Average per Movie" está no índice 3

            if media_gross > maior_media_gross:
                maior_media_gross = media_gross
                ator_maior_media_gross = ator

        return ator_maior_media_gross, maior_media_gross

# Encontrar ator com maior média de Gross por filme
ator_maior_media_gross, maior_media_gross = encontrar_maior_media_gross_por_filme()

# Imprimir na tela
print(f'O ator/atriz com a maior média de receita de bilheteria bruta por filme é {ator_maior_media_gross} com uma média de {maior_media_gross:.2f} milhões de dólares por filme.')
