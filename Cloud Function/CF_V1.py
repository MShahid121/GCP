import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery

'''
Python libraries to be installed

gcsfs
fsspec
pandas
pandas-gbq

'''
## The above libraries need to be referenced in the requirement file

def gcs_to_bigQuery(event,context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
    """
    # Step 0: Gathering the event info
    file_name = event['name']
    table_name = file_name.split('.')[0]
    bucket_name = event['bucket']

    # Loading the data into BigQuery using Pandas

    # Step 1: Read our csv file into BigQuery
    df_data = pd.read_csv('gs://' + bucket_name + '/' + file_name)
    # Step 2: Write our csv file into BigQuery
    df_data.to_gbq('gcp_ms_demo.' + table_name, # Change the table name.
                   project_id='gcp_ms_demo-demos-123242', ## Change the project ID
                   if_exists='append',
                   location='us') ## location of BigQuery instance instance
