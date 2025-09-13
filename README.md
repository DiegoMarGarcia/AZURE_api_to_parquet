# 📊 Projeto: Ingestão de Dados do IBGE em Azure + Power BI  

Este projeto implementa uma solução de dados em **Azure**, utilizando APIs do **IBGE** para ingestão de **População (2024)** e **PIB Municipal (2021)**.  
O objetivo é construir um **Data Lakehouse** com camadas (Bronze, Silver, Gold) e disponibilizar indicadores em **Power BI**.  

---

## 🚀 Arquitetura da Solução  

A arquitetura segue o padrão **Medallion (Bronze → Silver → Gold)**:  

- **Bronze (Raw Layer):** ingestão direta da API do IBGE em formato **Parquet**.  
- **Silver (Curated Layer):** padronização de schemas e tratamento de dados.  
- **Gold (Delivery Layer):** indicadores prontos para consumo no Power BI.  
- **Power BI:** visualização final dos indicadores.  

📌 *Sugestão de imagem:* diagrama mostrando **Azure Databricks + ADLS + Power BI**.  

---

## 🏗️ Serviços no Azure  

### 🔹 Resource Group  
- Nome sugerido: `rg-ibge-datalake`  
- Centraliza todos os recursos do projeto.  

📌 *Imagem sugerida:* print do **Resource Group** no Azure Portal.  

---

### 🔹 Azure Data Lake Storage Gen2 (ADLS)  
Estrutura de containers no storage:  
- `bronze/` → dados crus da API IBGE  
- `silver/` → dados tratados  
- `gold/` → indicadores finais  

📌 *Imagem sugerida:* tela do **ADLS** mostrando os containers.  

---

### 🔹 Azure Databricks  
- Workspace provisionado para execução dos jobs em PySpark.  
- Notebooks criados:  
  - `src/ingest_ibge.py` → ingestão da API e escrita no **bronze**.  
  - `src/transform_silver_to_gold.py` → transformação e criação de métricas no **gold**.  

📌 *Imagem sugerida:* tela do **Databricks** rodando o código PySpark.  

---

## ⚙️ Ingestão de Dados (Bronze)  

- APIs do IBGE consumidas:  
  - População → **Agregado 6579**  
  - PIB Municipal → **Agregado 5938**  
- Dados gravados no **ADLS** em `parquet`.  

📌 *Imagem sugerida:* execução do código com `.write.parquet(...)`.  

---

## 🔄 Transformação (Silver → Gold)  

No Databricks, realizamos:  
- Normalização de schemas.  
- Criação de métricas:  
  - PIB per capita.  
  - Variação **YoY** (Year-over-Year).  
  - **Share na UF** e **share no Brasil**.  
  - **Rankings** por PIB e População.  
- Escrita em **Parquet** no container `gold`.  

📌 *Imagem sugerida:* dataframe Spark mostrando as colunas finais (`pib_per_capita`, `yoy`, `share_uf`, `share_brasil`).  

---

## 📈 Dashboard no Power BI  

- Conexão com a camada **Gold** do Data Lake.  
- Indicadores entregues:  
  - PIB total, População total, PIB per capita.  
  - Evolução **YoY**.  
  - Rankings de Municípios e UFs.  
  - Participação percentual no PIB Nacional.  

📌 *Imagem sugerida:* dashboard com gráficos de barras e mapas do Brasil.  

---

## ✅ Boas Práticas Aplicadas  

- **Formato Parquet** para performance e compressão.  
- **Medallion Architecture** para clareza e escalabilidade.  
- **PySpark em Databricks** para processamento distribuído.  
- **Versionamento GitHub** para colaboração e reprodutibilidade.  
- **Documentação clara** para facilitar a execução do pipeline.  

---

## 📂 Estrutura do Repositório  

