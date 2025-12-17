FROM apache/airflow:2.10.2-python3.11

# ======================
# 1️⃣ SISTEMA / JAVA / SPARK
# ======================
USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-17-jdk \
        curl \
        wget \
        ca-certificates \
        procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# JAVA
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# SPARK
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3

RUN curl -fSL https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    | tar -xz -C /opt/

ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
ENV PATH=$SPARK_HOME/bin:$PATH

# ======================
# 2️⃣ PYTHON DEPENDENCIES (COMO airflow)
# ======================
USER airflow

RUN pip install --no-cache-dir \
    apache-airflow-providers-apache-spark==4.6.0 \
    pyspark==3.5.1 \
    pandas==2.1.4 \
    numpy==1.26.4

# ======================
# 3️⃣ PERMISSÕES
# ======================
USER root
RUN mkdir -p /opt/airflow && chown -R 50000:0 /opt/airflow

# ======================
# 4️⃣ USUÁRIO FINAL
# ======================
USER 50000:0
