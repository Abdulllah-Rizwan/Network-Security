import sys
import os
import json
import pandas as pd
import numpy as np
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
import certifi
from dotenv import load_dotenv
import pymongo

load_dotenv(override=True)

MONGODB_URL = os.getenv('MONGODB_URL')
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list( json.loads(data.T.to_json()).values()) 
            return records
        except Exception as e:
            raise NetworkSecurityException(e)
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGODB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == '__main__':
    FILE_PATH='Network_Data\phisingData.csv'
    DATABASE='NetworkSecurity'
    COLLECTION='NetworkData'
    
    obj = NetworkDataExtract()

    records = obj.csv_to_json(FILE_PATH)

    len = obj.insert_data_to_mongodb(records=records,database=DATABASE,collection=COLLECTION)

    print(len)


    
