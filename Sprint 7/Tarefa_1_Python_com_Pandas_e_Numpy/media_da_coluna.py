import pandas as pd
import numpy as np

# Lê o arquivo CSV com o Pandas
df = pd.read_csv('actors.csv')

# Calcula a média do número de filmes usando NumPy e Pandas
numero_de_filmes = df['Number of Movies'].to_numpy()
media_numero_de_filmes = np.mean(numero_de_filmes)

print(f'A média do número de filmes é {media_numero_de_filmes}.')
