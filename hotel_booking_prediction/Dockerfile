FROM python:3.7-slim

RUN apt-get update

# Copy local code to the container image.
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

#Runs a single unvicorn process so we can handle replication at the cluster level
#Otherwise we can use gunicorn as a process manager
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]