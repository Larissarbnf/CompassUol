import csv

# Inicialize as variáveis para armazenar o ator com o maior número de filmes
ator_maior_numero_filmes = ""
maior_numero_filmes = 0

# Abra o arquivo CSV
with open('actors.csv', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Pule o cabeçalho
    next(leitor_csv)
    
    # Percorra as linhas do arquivo
    for linha in leitor_csv:
        nome_ator = linha[0]
        numero_filmes = int(linha[2])
        
        # Verifique se o número de filmes é maior que o atual
        if numero_filmes > maior_numero_filmes:
            ator_maior_numero_filmes = nome_ator
            maior_numero_filmes = numero_filmes

# Imprima o ator com o maior número de filmes
print(f"O ator com mais filmes é {ator_maior_numero_filmes} com {maior_numero_filmes} filmes.")

