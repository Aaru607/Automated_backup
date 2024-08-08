import json
import boto3
import pymongo
import datetime
import os
from pymongo import MongoClient

# Environment variables
MONGO_URI = os.getenv('MONGO_URI')  # MongoDB connection string
DB_NAME = os.getenv('DB_NAME')  # Name of the MongoDB database
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')  # Name of the S3 bucket

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    # Create a backup filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = f"mongodb_backup_{timestamp}.json"
    
    # Create a backup of all collections in the database
    backup_data = {}
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        backup_data[collection_name] = list(collection.find({}))
    
    # Convert backup data to JSON
    backup_json = json.dumps(backup_data, default=str)
    
    # Metadata to include in S3
    metadata = {
        'Backup-Timestamp': timestamp,
        'Database-Name': DB_NAME
    }
    
    # Upload the backup to S3
    try:
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=backup_filename,
            Body=backup_json,
            ContentType='application/json',
            Metadata=metadata
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Backup successfully uploaded to S3 with metadata!')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading backup to S3: {str(e)}')
        }
