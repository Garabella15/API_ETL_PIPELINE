from extract_job_posted import get_job_posted, transformed_raw_data
from util import get_api_auth

def main():
    headers = get_api_auth()
    'Main function for running all other functions/modules.'
    # Pull exchange rates data from API
    # get_job_posted(headers)
    # Transform raw job posted data from an external JSON file
    transformed_raw_data()
    #print('Transformed data written to a csv file')

main()