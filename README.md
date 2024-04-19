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