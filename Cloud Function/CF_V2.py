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

def gcs_to_bigQuery(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context:  Metadata for the event.
    """
    # Create a list to store information about the event
    lst = []
    file_name = event['name']
    table_name = file_name.split('.')[0]
    # Step 1:  Define a dictionary containing info about metadata about the event
    dct = {
        'Event_ID': context.event_id,
        'Event_type': context.event_type,
        'Bucket_name': event['bucket'],
        'File_name': event['name'],
        'Created': event['timeCreated'],
        'Updated': event['updated']
    }
    lst.append(dct)
    # Step 2: Read the data from the dictionary into pandas data frame.
    df_metadata = pd.DataFrame.from_records(lst)
    # Step 3: Write the data into BigQuery.
    df_metadata.to_gbq('gcp_ms_demo.data_loading_metadata', # Change the dataset and table name
                       project_id='gcp_ms_demo-123124', # Change project_id
                       if_exists='append',
                       location='us')
    # Let's now write our CSV file to BigQuery

    # Step 1: Read the file into pandas data frame
    df_data = pd.read_csv('gs://' + event['bucket'] + '/' + file_name)

    # Step 2: Loading the data into BigQuery
    df_data.to_gbq('gcp_dataeng_demos.' + table_name, # Change this
                   project_id='gcp-dataeng-demos-365206', # Change this
                   if_exists='append',
                   location='us')