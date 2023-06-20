import pandas as pd
import requests
import json



def get_job_posted(headers):
    """
    
    """
    
    
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query":"Data Engineer and Data Analyst in UK and USA","page":"1","num_pages":"1"}


    response = requests.get(url, headers=headers, params=querystring)

    response_data = response.json()
    
    with open ('raw/raw_job_posted_data.json', 'w') as jobfile:
        json.dump(response_data, jobfile)
        print('data successfully written to a raw database file')
    


        
        