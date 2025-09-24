# 🔧 Versões configuráveis
ARG AIRFLOW_VERSION="3.0.6"
ARG PYTHON_MAJOR_MINOR_VERSION="3.11"
FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_MAJOR_MINOR_VERSION}

# 🐍 Instalar dependências Python adicionais via build arg
ARG PIP_ADDITIONAL_REQUIREMENTS=""
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
  && if [ -n "${PIP_ADDITIONAL_REQUIREMENTS}" ]; then \
       pip install --no-cache-dir ${PIP_ADDITIONAL_REQUIREMENTS}; \
     fi

# ⚙️ Mudar para root para instalar pacotes do sistema (apenas utilitários básicos)
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
