# Scorecard Application

## Introduction
Our project presents a structure framework for developing a highly accurate credit scorecard, accompanied by a deployment solution tailored for serving high loads of requests. The framework is separated in three parts: 
  
1. Model Development, 
2. Application Development, and 
3. Application Deployment. 

With our framework, the scorecard model was able to achieve high prediction power with AUC of 0.9873, and F1 score of 0.9793. A Streamlit web application was successfully developed with functionalities of receiving declared input from users and generate the credit score presented with a gauge chart on a friendly user interface. At the final stage, model deployment, the application was containerized and deployed on a Kubernetes cluster, which was able to handle more than 100 requests per second with CPU utilization being stable at around 50%.

## Installation

### Prerequisites
- Docker desktop (URL: https://docs.docker.com/desktop/install)
- Kubernetes (kubectl module, URL: https://docs.docker.com/desktop/kubernetes/) 
  - metric server (URL: https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html)
### Install commands

First, we build the scorecard image

```shell
cd [path_to_root_dir]
docker built -t scorecard .
```

Next, we create kubernetes cluster using yaml files:

```shell
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

If everything goes right, we should be able to access the application at http://localhost:80.

<img src="D:\OneDrive\OneDrive - Trent University\5610\Final project\scorecard_app\home.png" width="500"/>

### Collaboration

- Stanley Chen [LinkedIn](https://www.linkedin.com/in/stanley-xueyu-chen)
- Minh Dinh [LinkedIn](https://www.linkedin.com/in/minhdinh1305/)
- Thanh Hoang [LinkedIn](https://www.linkedin.com/in/thanh-hoang-5125a2197)
