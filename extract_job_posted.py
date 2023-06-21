import pandas as pd
import requests
import json
from datetime import datetime
import os



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
    


        
def transformed_raw_data():
    csv_data = []
    with open('raw/raw_job_posted_data.json', 'r') as job_file:
        reader = json.load(job_file)
        data = reader['data']
        
    
    # reading the data to pandas dataframe, first we create a column name
    column_names = ['employer_website', 'job_id', 'job_employment_type', 'job_title', 'job_apply_link', 'job_description', 'job_city', 'job_country', 'job_posted_at_timestamp','employer_company_type']
    job_df = pd.DataFrame(data, columns=column_names)
    
    #converting the timestamp vale to date
    print(job_df['job_posted_at_timestamp'])

    
    # filepath = os.path('API_ETL_PIPELINE/Transfromed/job_posted_data.csv')   
    # job_df.to_csv(filepath)