In the project, an etl pipeline is used to extract, transform and load job vacancy for Data Engineer and Data Analyst in the UK and US.
the data is extracted an stored in the raw staging area where it is the transformed and stored the Transformed staging before finally
persisting the data in postgres database.

.env file created in the root directory contains the RapidAPI key and Host. created an account in the RapidAPI and assign it to value variable below

X-RapidAPI-Key= API_KEY

X-RapidAPI-Host= API_HOST

env also contained the variables for the database connection 

DB_NAME=

DB_USER=

DB_PASSWORD=

DB_HOST=

DB_PORT=


util.py provides the function that return the database and rapidapi connection.

extract_job_posted.py - ETL pipeline code

main.py calls the function in extract_job_posted.py







