def listar_atores_por_receita_bruta():
    with open('actors.csv', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        # Removendo o cabeçalho
        cabecalho = linhas[0]
        linhas = linhas[1:]

        # Criar uma lista de tuplas com o nome do ator e a receita total bruta
        lista_atores = []

        for linha in linhas:
            partes = linha.split(',')
            ator = partes[0]
            total_gross = partes[1].strip()  # A coluna "Total Gross" está no índice 1

            # Verificando se é um valor numérico
            if total_gross.replace('.', '', 1).isdigit():
                lista_atores.append((ator, float(total_gross)))

        # Ordenar os atores por receita bruta em ordem decrescente
        lista_atores_ordenada = sorted(lista_atores, key=lambda x: x[1], reverse=True)

        return lista_atores_ordenada

# Listar atores por receita bruta
atores_ordenados = listar_atores_por_receita_bruta()

# Escrever no arquivo etapa-5.txt
with open('etapa-5.txt', 'w', encoding='utf-8') as arquivo_etapa_5:
    for ator, total_gross in atores_ordenados:
        arquivo_etapa_5.write(f'{ator} - {total_gross:.2f}\n')

# Listar e imprimir na tela
for ator, total_gross in atores_ordenados:
    print(f'{ator} - {total_gross:.2f}')
