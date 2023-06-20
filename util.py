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




