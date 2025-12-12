# 🔧 Versão fixa do Airflow (evita Airflow 3)
FROM apache/airflow:2.10.2-python3.11

# 1️⃣ Instalar dependências Python como usuário airflow
USER airflow

RUN pip install --no-cache-dir \
    apache-airflow-providers-apache-spark==4.6.0 \
    pyspark==3.5.1 \
    pandas==2.1.4 \
    numpy==1.26.4

# 2️⃣ Voltar para root para instalar utilitários do sistema
USER root

RUN apt-get update --allow-releaseinfo-change \
  && apt-get install -y --no-install-recommends \
       wget \
       curl \
       ca-certificates \
       procps \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 3️⃣ Ajustar permissões do diretório do Airflow
RUN mkdir -p /opt/airflow && chown -R 50000:0 /opt/airflow

# 4️⃣ Voltar para usuário correto do Airflow
USER 50000:0
