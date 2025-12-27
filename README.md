# FraudFlow – Data Pipeline de Detecção de Anomalias com Spark e Airflow

Este projeto implementa um **pipeline de dados para detecção de anomalias (fraudes)** utilizando **Apache Spark** para processamento distribuído, **Apache Airflow** para orquestração e **Docker** para padronização e execução do ambiente.

O objetivo é demonstrar, de forma prática, como integrar ferramentas amplamente usadas em engenharia de dados em um ambiente reproduzível e organizado.

---

## 🛠️ Tecnologias Utilizadas

- **Apache Spark**  
  Processamento distribuído de dados e transformações em larga escala.

- **Apache Airflow**  
  Orquestração do pipeline, controle de dependências e agendamento das tarefas.

- **Docker & Docker Compose**  
  Containerização e orquestração dos serviços, garantindo ambiente consistente.

- **Python (PySpark)**  
  Implementação das regras de negócio e transformações dos dados.

---

## 🏗️ Arquitetura do Projeto

O pipeline segue uma arquitetura simples e didática, focada em boas práticas de engenharia de dados:

1. **Airflow** é responsável por orquestrar o fluxo de execução.
2. O **DAG do Airflow** dispara jobs do **Spark**.
3. O **Spark** lê dados brutos (raw), processa e aplica regras de transformação.
4. Os dados transformados são gravados em uma camada intermediária (staging/processed).
5. Todo o ambiente roda de forma isolada via **Docker Compose**.

---

## ▶️ Como Executar o Projeto Localmente

### Pré-requisitos

- Docker
- Docker Compose

> Não é necessário instalar Spark ou Airflow localmente.

---

### Passo a passo

   ```bash
   git clone https://github.com/Andressa-Evelyn/fraudflow-spark-pipeline.git
   cd fraudflow-spark-pipeline
   docker compose up -d
   docker ps
   acesse o Airflow
   ative o DAG no painel do Airflow



