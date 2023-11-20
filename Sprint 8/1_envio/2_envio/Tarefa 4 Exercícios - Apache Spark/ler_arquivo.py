from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
import random

# Configurando a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Lendo o arquivo nomes_aleatorios.txt
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeando a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
# Adicionando a coluna "Escolaridade"
df_nomes = df_nomes.withColumn("Escolaridade", F.when(F.rand() < 1/3, "Fundamental")
                                           .when(F.rand() < 2/3, "Médio")
                                           .otherwise("Superior"))
# Adicionando a coluna "Pais"
paises_americadosul = ["Brasil", "Argentina", "Chile", "Colômbia", "Equador", "Paraguai", "Uruguai", "Bolívia", "Peru", "Venezuela", "Suriname", "Guiana", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Pais", F.expr("array('Brasil', 'Argentina', 'Chile', 'Colômbia', 'Equador', 'Paraguai', 'Uruguai', 'Bolívia', 'Peru', 'Venezuela', 'Suriname', 'Guiana', 'Guiana Francesa')[int(rand() * 13)]"))

# Adicionando a coluna "AnoNascimento"
df_nomes = df_nomes.withColumn("AnoNascimento", F.expr("int(rand() * (2010-1945+1)) + 1945"))

# Selecionando pessoas nascidas neste século "df_select"
df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000).limit(10)
df_select.show()

# Registrando o dataframe como uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Executando um comando SQL para selecionar todas as pessoas
spark.sql("SELECT * FROM pessoas").show()

# Exibindo algumas linhas do dataframe
df_nomes.show(5)

# Exibindo o Schema
df_nomes.printSchema()

# Contando o número de pessoas da geração Millennials usando o método select
count_millennials_df = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
print("Número de Millennials (DataFrame):", count_millennials_df)

# Contando o número de pessoas da geração Millennials usando Spark SQL
count_millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print("Número de Millennials (Spark SQL):", count_millennials_sql)

# Obtendo a quantidade de pessoas por país e geração usando Spark SQL
df_paises_geracoes = spark.sql("""
    SELECT Pais, 
           CASE 
               WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
               WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
               WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
               WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
               ELSE 'Outro' 
           END AS Geracao,
           COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao
""")
df_paises_geracoes.show()



