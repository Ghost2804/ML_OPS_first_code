import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import pymysql

from dotenv import load_dotenv

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading mysql database started")

    try:
        
        mysql = pymysql.connect(
            host= host,
            user = user,
            password= password,
            db= db
        )
        logging.info("Connection Establish",mysql)

        df = pd.read_sql_query("select * from heart",mysql)
        if df.empty:
            logging.warning("Query returned an empty DataFrame.")
            raise ValueError("Database table 'heart' is empty or does not exist.")

        print(df.head())  

        mysql.close()  
        return df  

    except Exception as e:
        raise CustomException(e)