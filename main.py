
import boto3
import requests
import json

# AWS and Elasticsearch Configuration
REGION = "us-east-1"
ES_ENDPOINT = "https://your-elasticsearch-domain.amazonaws.com"
LOG_GROUP_NAME = "your-log-group-name"

# Initialize CloudWatch Logs client
logs_client = boto3.client('logs', region_name=REGION)

# Fetch logs from CloudWatch
response = logs_client.filter_log_events(
    logGroupName=LOG_GROUP_NAME,
    limit=100
)

# Ingest logs into Elasticsearch
for event in response['events']:
    log_entry = {
        "timestamp": event['timestamp'],
        "message": event['message']
    }
    headers = {"Content-Type": "application/json"}
    es_url = f"{ES_ENDPOINT}/logs/_doc"
    requests.post(es_url, headers=headers, data=json.dumps(log_entry))

print("Logs successfully ingested into Elasticsearch")
