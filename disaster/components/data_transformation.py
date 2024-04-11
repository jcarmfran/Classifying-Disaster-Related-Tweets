import os
import re
import sys
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from disaster.logger import logging 
from disaster.exception import CustomException
from disaster.entity.config_entity import DataTransformationConfig
from disaster.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts


class DataTransformation:
    def __init__(self,data_transformation_config: DataTransformationConfig,data_ingestion_artifacts:DataIngestionArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts


    def dropping_columns(self):
        try:
            logging.info("Entered into the dropping_columns function")
            # Training Data
            data=pd.read_csv(self.data_ingestion_artifacts.data_file_path)
            data.drop(self.data_transformation_config.ID, axis=self.data_transformation_config.AXIS, inplace=self.data_transformation_config.INPLACE)
            # repeating instead of adding to above drop method.
            # I have a newborn and right now, my brain is too mushy to try to figure out an elegant way to include items in a list into a list of desired dropped columns.
            data.drop(self.data_transformation_config.DROP_COLUMNS, axis=self.data_transformation_config.AXIS, inplace = self.data_transformation_config.INPLACE) 
            return data

        except Exception as e:
            raise CustomException(e,sys) from e 


    def data_cleaning(self, words):
        try:
            logging.info("Entered into the data_cleaning function")
            # Let's apply stemming and stopwords on the data
            stemmer = nltk.SnowballStemmer("english")
            stopword = set(stopwords.words('english'))
            words = str(words).lower()
            words = re.sub(r'[^a-zA-Z]', ' ', words)
            words = [word for word in words.split(' ') if words not in stopword]
            words=" ".join(words)
            words = [stemmer.stem(word) for word in words.split(' ')]
            words=" ".join(words)
            logging.info("Exited the data_cleaning function")
            return words 

        except Exception as e:
            raise CustomException(e, sys) from e


    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        try:
            logging.info("Entered the initiate_data_transformation method of Data transformation class")
            df = self.dropping_columns()
            df[self.data_transformation_config.TEXT]=df[self.data_transformation_config.TEXT].apply(self.data_cleaning)

            os.makedirs(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR, exist_ok=True)
            df.to_csv(self.data_transformation_config.TRANSFORMED_FILE_PATH,index=False,header=True)

            data_transformation_artifact = DataTransformationArtifacts(
                transformed_data_path = self.data_transformation_config.TRANSFORMED_FILE_PATH
            )
            logging.info("Returning DataTransformationArtifacts")
            return data_transformation_artifact

        except Exception as e:
            raise CustomException(e, sys) from e
