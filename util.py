import requests
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()



def get_api_auth():
    ''' 
    the function returns the api credential from the environment variables
    file (.env) in the project directory
    parameter: takes no parameter
    return value : a tuple consisting of the api credentials
    return type: tuple
    
    '''
    rapidapi_key = os.getenv("X-RapidAPI-KEY")
    rapidapi_host = os.getenv("X-RapidAPI-Host")
    headers = { 
                    "X-RapidAPI-Key":  rapidapi_key,
	                "X-RapidAPI-Host":  rapidapi_host
            }
    return headers


def db_connection():
    """
    the function creates a connection to the database talent_db by retriving database
    credential store in the .env file
    parameter : takes no parameter
    return value: database connection
    return type : bool
    """
    name = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password= os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}")
    
    return engine


