import pandas as pd
import numpy as np

# Lê o arquivo CSV com o Pandas
df = pd.read_csv('actors.csv')

# Calcula a média por filme usando NumPy e Pandas
total_gross = df['Total Gross'].to_numpy()
num_movies = df['Number of Movies'].to_numpy()
df['Average per Movie'] = np.divide(total_gross, num_movies)

# Encontra o ator/atriz com a maior média por filme usando Pandas
ator_com_maior_media = df.loc[df['Average per Movie'].idxmax()]['Actor']

print(f'O ator/atriz com a maior média por filme é {ator_com_maior_media}.')
