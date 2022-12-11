import pymongo
import pandas as pd
from dataclasses import dataclass
import os
import urllib

@dataclass
class EnvironmentVariable:
    mongo_db_passwd:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")
    mongo_db_url:str = "mongodb+srv://viketan:"+urllib.parse.quote(mongo_db_passwd)+"@cluster0.et7ujxe.mongodb.net/test"


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "phishing"