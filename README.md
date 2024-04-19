# Classifying-Disaster-Related-Tweets
As the name of this repository suggests, this application classifies tweets (or whatever they're called now...) as disaster related or not.

## Running Locally
Running this on your local machine requires at least implementing the following steps. Commands are given below each step.  
1. Clone this repository
    ```
    git clone https://github.com/jcarmfran/Classifying-Disaster-Related-Tweets.git
    ```
2.  Create an appropriate `conda` environment.
    ```
    conda create -n hate python=3.8 -y
    ```
3. Activate the environment
    ```
    conda activate hate
    ```
4. Install necessary requirements
    ```
    pip install -r requirements.txt
    ```
5. Run the application
    ```
    python app.py
    ```

Save any errors following step 5, navigating to `localhost:8080` on your web browser will reveal the application!

### Deploying to the Cloud via Github Actions
There are a few ways you can deploy this application to the cloud.

#### AWS: ECR
1. Login into your AWS console
2. Create IAM user for deployment and give the following permissions:
    - AmazonEC2ContainerRegistryFullAccess
    - AmazonEC2FullAccess
3. Build the docker image from source
4. Create ECR repo to store docker image
5. Push the docker image to ECR
6. Build and launch EC2 instance
    In our case, we'll build the EC2 with Ubuntu
7. Open EC2 and install docker
```
#optional

sudo apt-get update -y

sudo apt-get upgrade


#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
7. Configure EC2 as self-hosted runner
    In the projects Github page, navigate to 
    -> Settings 
    -> Actions 
    -> Runner 
    -> New self hosted runner 
    -> choose os 
    -> then run commands one by one
8. Setup your Github secrets
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
    - AWS_ECR_LOGIN_URI
    - ECR_REPOSITORY_NAME