# Databricks notebook source

# Required each time the cluster is restarted which should be only on the first notebook as they run in order 
tiers = ["bronze", "silver", "gold"]
adls_paths = {tier: f"abfss://{tier}@ibgecase.dfs.core.windows.net/" for tier in tiers}

# Accessing paths 
bronze_adls = adls_paths ["bronze"] 
silver_adls = adls_paths ["silver"] 
gold_adls = adls_paths["gold"]

dbutils.fs.ls (bronze_adls)
#dbutils.fs.ls(silver_adls) 
#dbutils.fs.ls(gold_adls)

# COMMAND ----------

import requests
from pyspark.sql import SparkSession

# Criar sessão Spark
spark = SparkSession.builder.appName("IBGE_PIB").getOrCreate()

# URL oficial IBGE (PIB Municipal)
url_pib = "https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/all/variaveis/all?localidades=N1[all]"
url_pop = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/all/variaveis/all?localidades=N1[all]"


# Requisição
res = requests.get(url_pib)

if res.status_code == 200:
    data = res.json()
    rows = []
    for item in data:
        var_id = item["id"]
        variavel = item["variavel"]
        unidade = item["unidade"]

        for resultado in item["resultados"]:
            for serie in resultado["series"]:
                localidade = serie["localidade"]["nome"]
                for ano, valor in serie["serie"].items():
                    rows.append({
                        "id": var_id,
                        "variavel": variavel,
                        "unidade": unidade,
                        "localidade": localidade,
                        "ano": int(ano),
                        "valor": None if valor == "-" else float(valor)
                    })

    # Criar DataFrame Spark
    df = spark.createDataFrame(rows)

    # Visualizar
    df.show(10, truncate=False)
    df.printSchema()

    #salvando no blob storage
    df = df.coalesce(1)  #salva um unico arquivo parquet
    df.write.format("parquet").mode("overwrite").save(bronze_adls + "pib_municipal.parquet")
else:
    print(f"Erro {res.status_code}: {res.text}")


# COMMAND ----------

url_pop = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/all/variaveis/all?localidades=N1[all]"


# Requisição
res = requests.get(url_pop)

if res.status_code == 200:
    data = res.json()
    rows = []
    for item in data:
        var_id = item["id"]
        variavel = item["variavel"]
        unidade = item["unidade"]

        for resultado in item["resultados"]:
            for serie in resultado["series"]:
                localidade = serie["localidade"]["nome"]
                for ano, valor in serie["serie"].items():
                    rows.append({
                        "id": var_id,
                        "variavel": variavel,
                        "unidade": unidade,
                        "localidade": localidade,
                        "ano": int(ano),
                        "valor": None if valor == "-" else float(valor)
                    })

    # Criar DataFrame Spark
    df = spark.createDataFrame(rows)

    # Visualizar
    df.show(10, truncate=False)
    df.printSchema()

    #salvando no blob storage
    df = df.coalesce(1)  #salva um unico arquivo parquet
    df.write.format("parquet").mode("overwrite").save(bronze_adls + "pop_municipal.parquet")
else:
    print(f"Erro {res.status_code}: {res.text}")
