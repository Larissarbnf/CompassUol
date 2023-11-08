import boto3
from datetime import datetime

# Configuração AWS
chave_acesso = 'AKIAVIQABTV56MUYWVLM'
chave_acesso_secreta = '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'
s3 = boto3.client('s3', aws_access_key_id=chave_acesso, aws_secret_access_key=chave_acesso_secreta)

# Arquivos CSV
movies = 'movies.csv'
series = 'series.csv'

# Caminho do bucket
nome_bucket = 'desafio-etl-1-compass'
camada_de_armazenamento = 'Raw'
origem_do_dado = 'Local'
formato_do_dado = 'CSV'
data_de_processamento = datetime.now().strftime('%Y/%m/%d')
caminho_movies = f'{camada_de_armazenamento}/{origem_do_dado}/{formato_do_dado}/Movies/{data_de_processamento}/{movies}'
caminho_series = f'{camada_de_armazenamento}/{origem_do_dado}/{formato_do_dado}/Series/{data_de_processamento}/{series}'

# Gravação no S3
s3.upload_file(movies, nome_bucket, caminho_movies)
s3.upload_file(series, nome_bucket, caminho_series)