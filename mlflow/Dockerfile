FROM python:3.8.2

RUN apt-get update -y
RUN apt-get install libpq-dev -y

RUN pip install --upgrade pip
RUN pip3 install Cython && \
    pip install mlflow[extras]==1.9.1 && \
    pip install psycopg2-binary==2.8.5 && \
    pip install boto3==1.15.16 \
    pip install protobuf~=3.12

EXPOSE 5000

ENTRYPOINT ["mlflow", "server"]