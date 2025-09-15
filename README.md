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

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1ff135f0-4c57-4395-bb44-0fe67ad854ef" />


---

## 🏗️ Serviços no Azure  

### 🔹 Resource Group  
- Nome: `teste_case_contratacao`  
- Centraliza todos os recursos do projeto.  

<img width="1487" height="313" alt="image" src="https://github.com/user-attachments/assets/e83f3031-f7aa-47a7-b8ac-c8ce4ee2e549" />


---

### 🔹 Azure Data Lake Storage Gen2 (ADLS)  
Estrutura de containers no storage:  
- `bronze/` → dados crus da API IBGE  
- `silver/` → dados tratados  
- `gold/` → indicadores finais  

<img width="541" height="359" alt="image" src="https://github.com/user-attachments/assets/66010524-f356-4338-8a68-4bc0902d907b" />

---

### 🔹 Azure Databricks  
- Workspace provisionado para execução dos jobs em PySpark.  
- Notebooks criados:  
  - `src/API_ingestion_parquet_ondemand.py` → ingestão da API e escrita no **bronze**.  
  - `src/BRONZE_to_SILVER___pib_municipal_ondemand.py` → dados tratados na **silver**.  

<img width="1084" height="139" alt="image" src="https://github.com/user-attachments/assets/4df9dbf6-174d-432d-b124-2d9bb513ea4a" />


---

## ⚙️ Ingestão de Dados (Bronze)  

- APIs do IBGE consumidas:  
  - População → **Agregado 6579**  
  - PIB Municipal → **Agregado 5938**  
- Dados gravados no **ADLS** em `parquet`.  

<img width="720" height="572" alt="image" src="https://github.com/user-attachments/assets/2e0931be-eef0-4d10-9433-4e06136204de" />


---

## 🔄 Transformação (Silver → Gold)  --to do

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

## 📈 Dashboard no Power BI  --to do

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


