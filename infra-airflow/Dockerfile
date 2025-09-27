# 🔧 Versões fixas (evita puxar Airflow 3.x instável)
FROM apache/airflow:2.10.2-python3.11

# 🐍 Instalar dependências adicionais do Python
# - Spark Provider para integração com Spark
# - pandas e numpy para manipulação de dados
RUN pip install --no-cache-dir \
    apache-airflow-providers-apache-spark \
    pandas \
    numpy

# ⚙️ Mudar para root para instalar utilitários básicos
USER root
RUN apt-get update --allow-releaseinfo-change \
  && apt-get install -y --no-install-recommends \
       wget \
       curl \
       ca-certificates \
       procps \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 🧼 Garantir permissões corretas para Airflow
RUN mkdir -p /opt/airflow && chown -R 50000:0 /opt/airflow

# 👤 Voltar para usuário padrão do Airflow
USER 50000:0

# 🐚 Entrar no bash por padrão (útil para debug)
CMD ["bash"]
