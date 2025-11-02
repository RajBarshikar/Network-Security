import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print(f"MONGO_URI: {MONGO_URI}")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import  pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

def row_to_json(feature_list, columns):
        json_data = dict(zip(columns, feature_list))
        return json.dump(json_data)

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
        
    def csv_to_json(self, file_path):

        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict('records')
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongo(self, records, database, collection):
         try:
            self.database = database
            self.collection = collection
            self.records = records


            self.mongo_client = pymongo.MongoClient(MONGO_URI)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return (len(self.records))
         except Exception as e:
            raise NetworkSecurityException(e, sys)



if __name__ == "__main__":
    FILE_PATH = 'R:/Internship/MLops/Network_Data/phisingData.csv'
    DATABASE = "NetworkSecurity"
    COLLECTION = "phishing_data"
    nde = NetworkDataExtract()
    records = nde.csv_to_json(file_path=FILE_PATH)
    no_of_records = nde.insert_data_to_mongo(records, DATABASE, COLLECTION)
    print(no_of_records)
