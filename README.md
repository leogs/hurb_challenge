# Hurb Challenge

This repository contains the code for a prediction API based on a classification model proposed by Hurb as a coding challenge.
Details of the model are [in this link](https://www.kaggle.com/code/niteshyadav3103/hotel-booking-prediction-99-5-acc).

The API was created using FastAPI. Besides the API Service, the container for a MLFlow tracking server using Minio and Postgres as backend storage are also provided.

To run the project, first install minikube following the [instructions in the documentation](https://minikube.sigs.k8s.io/docs/start/).

1. Start your cluster with
```
minikube start
```
2. Enable minikube-ingress:

```
minikube addons enable ingress
```

3. Run the run.sh file in the root directory. This file will apply all the kubernetes manifests with the Postgres, MinIO, Mlflow and FastAPI services. All the docker images are already in Dockerhub, so you don't need to build and push them.

```
chmod +x run.sh
./yourscript.sh
```

4. Since we are using Ingress, you need to add the hosts to your /etc/hosts file with

```
sudo nano /etc/hosts
```

With nano, add the following line and save:

```
127.0.0.1       localhost mlflow-server.local mlflow-minio.local api-server.local
```

With this line, you will be able to reach the API in api-server.local and the Mlflow Tracking Server in mlflow-server.local

5. Then run minikube tunnel:

```
minikube tunnel
```

6. Now you can try the API endpoints going to your browser and reaching the swagger docs in

```
http://api-server.local/docs

```
Before sending requests, authenticate using admin as user and password. Security keys and passwords were not properly secured due to time constraints.

To train the model and save the metrics on Mlflow, send a post request to:

```
http://api-server.local/train

```

To make predictions send requests to:

```
http://api-server.local/predict

```

The input schema is described in the API docs.
