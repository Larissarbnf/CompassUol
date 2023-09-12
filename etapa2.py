def calcular_media_gross():
    with open('actors.csv', 'r') as arquivo:
        linhas = arquivo.readlines()

        # Removendo o cabeçalho
        cabecalho = linhas[0]
        linhas = linhas[1:]

        total_gross = 0
        total_filmes = 0

        for linha in linhas:
            partes = linha.split(',')
            gross = partes[5].strip()  # A coluna "Gross" está no índice 5

            # Verificando se é um valor numérico
            if gross.replace('.', '', 1).isdigit():  
                total_gross += float(gross)

                # Contando o número total de filmes
                total_filmes += 1

        # Calculando a média
        media_gross = total_gross / total_filmes

        return media_gross

# Calcular a média de Gross
media_gross = calcular_media_gross()

# Imprimir na tela
print(f'A média de receita de bilheteria bruta dos principais filmes é: {media_gross:.2f} milhões de dólares')

