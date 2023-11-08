import pandas as pd
import numpy as np

def contar_aparicoes(data):
    filmes = data['#1 Movie'].to_numpy()
    nomes, contagens = np.unique(filmes, return_counts=True)
    contagem = np.column_stack((nomes, contagens))
    contagem = contagem[contagem[:,1].argsort()[::-1]]
    return contagem

try:
    # Lê o arquivo CSV com o Pandas
    data = pd.read_csv('actors.csv')

    # Chama a função para contar as aparições usando NumPy
    contagem = contar_aparicoes(data)

    # Exibe os resultados com o Pandas
    resultado = pd.DataFrame(contagem, columns=['Nome Filme', 'Quantidade'])
    print(resultado)

except FileNotFoundError:
    print("O arquivo 'actors.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
