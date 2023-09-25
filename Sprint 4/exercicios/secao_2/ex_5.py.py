# Leitura do arquivo
with open('estudantes.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

# Função para calcular a média das três maiores notas
calcular_media = lambda notas: round(sum(sorted(notas, reverse=True)[:3]) / 3, 2)

# Lista para armazenar os dados formatados
dados_formatados = []

for alunos in linhas:
    partes = alunos.strip().split(',')
    nome = partes[0]
    notas = list(map(int, partes[1:]))  # Agora as notas são convertidas para inteiros
    tres_maiores_notas = sorted(notas, reverse=True)[:3]
    media = calcular_media(notas)

    # Formatação da média
    media_formatada = f'{media:.1f}' if media.is_integer() else f'{media:.2f}'

    # Adiciona os dados formatados à lista
    dados_formatados.append(f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media_formatada}")

# Ordena as linhas pelo nome do aluno
relatorio = sorted(dados_formatados)

# Imprime cada linha do relatório
for linha in relatorio:
    print(linha)

