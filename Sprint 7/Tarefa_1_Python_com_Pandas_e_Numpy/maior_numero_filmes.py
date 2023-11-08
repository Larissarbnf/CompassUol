import pandas as pd
import numpy as np

# Lê o arquivo CSV
df = pd.read_csv('actors.csv')

# Calcula o número de filmes por ator/atriz usando NumPy
num_filmes_por_ator = df.groupby('Actor')['Number of Movies'].sum().reset_index()
num_filmes_por_ator = num_filmes_por_ator.to_numpy()

# Encontra o ator ou atriz com o maior número de filmes usando NumPy
ator_com_mais_filmes = num_filmes_por_ator[np.argmax(num_filmes_por_ator[:, 1]), 0]
numero_de_filmes = np.max(num_filmes_por_ator[:, 1])

print(f'O ator/atriz com mais filmes é: {ator_com_mais_filmes}, com um total de {numero_de_filmes} filmes.')
