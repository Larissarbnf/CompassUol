try:
    # Abre o arquivo em modo de leitura ('r')
    with open('arquivo_texto.txt', 'r') as arquivo:
        # Lê todo o conteúdo do arquivo e remove a quebra de linha no final
        conteudo = arquivo.read().rstrip('\n')
        print(conteudo, end='')
except FileNotFoundError:
    print("O arquivo 'arquivo_texto.txt' não foi encontrado.")
except Exception as ex:
    print(f"Ocorreu um erro: {ex}")