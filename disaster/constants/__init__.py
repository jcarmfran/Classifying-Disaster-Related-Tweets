import os
from datetime import datetime


# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'ml_datasets_01'
ZIP_FILE_NAME = 'disaster_tweets.zip'
LABEL = 'target'
TWEET = 'text'

# Data Ingestion Constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_TRAIN_DATA_DIR = "train.csv"
DATA_INGESTION_TEST_DATA_DIR = "test.csv"