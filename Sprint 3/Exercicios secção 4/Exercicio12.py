import json

# Lê o arquivo 'person.json'
with open('person.json', 'r') as arquivo:
    # Faz o parsing do JSON
    conteudo_json = json.load(arquivo)
    # Imprime o conteúdo
    print(conteudo_json)
