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
    
    # the raw csv is read by a json load function 
    with open('raw/raw_job_posted_data.json', 'r') as job_file:
        reader = json.load(job_file)
        data = reader['data']
        
    
    # reading the data to pandas dataframe, and the selected columns required are listed in the column_name
    column_names = ['employer_website', 'job_id', 'job_employment_type', 'job_title', 'job_apply_link', 'job_description', 'job_city', 'job_country', 'job_posted_at_timestamp','employer_company_type']
    job_df = pd.DataFrame(data, columns=column_names)
    
    #converting the timestamp vale to date
    job_date=pd.to_datetime(job_df['job_posted_at_timestamp'], unit='s')
    job_df['job_posted_at_timestamp'] = job_date
    job_df = job_df.rename(columns={"job_employment_type": "employment_type", "job_city": "City", 
                            "job_country": "Country", "job_posted_at_timestamp": "job_posted_date", "employer_company_type": "Sector"})
    
    # write the transformed data to a csv file 
    filepath = 'Transformed/cleaned_job_posted.csv'
    job_df.to_csv(filepath, sep='\t', encoding='utf-8', index=False)
    print('clean date succesffuly write to the transformed staging area')
    

    
    # filepath = os.path('API_ETL_PIPELINE/Transfromed/job_posted_data.csv')   
    # job_df.to_csv(filepath)