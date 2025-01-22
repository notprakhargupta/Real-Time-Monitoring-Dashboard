import boto3
import requests
import json
import time

# Configuration
AWS_REGION = "us-east-1"  # Update to your AWS region
ES_ENDPOINT = "https://your-elasticsearch-domain.amazonaws.com"  # Replace with your Elasticsearch endpoint
LOG_GROUP_NAME = "your-log-group-name"  # Replace with your CloudWatch log group name
INDEX_NAME = "cloudwatch-logs"  # Index in Elasticsearch

# Initialize AWS CloudWatch client
logs_client = boto3.client("logs", region_name=AWS_REGION)

def fetch_logs():
    """
    Fetch logs from AWS CloudWatch.
    """
    print("Fetching logs from CloudWatch...")
    response = logs_client.filter_log_events(
        logGroupName=LOG_GROUP_NAME,
        limit=100  # Adjust as needed
    )
    return response.get("events", [])

def ingest_to_elasticsearch(logs):
    """
    Ingest logs into Elasticsearch.
    """
    headers = {"Content-Type": "application/json"}
    for log in logs:
        log_entry = {
            "timestamp": log["timestamp"],
            "message": log["message"]
        }
        response = requests.post(
            f"{ES_ENDPOINT}/{INDEX_NAME}/_doc",
            headers=headers,
            data=json.dumps(log_entry)
        )
        if response.status_code == 201:
            print("Log entry ingested successfully:", log_entry)
        else:
            print("Failed to ingest log entry:", response.text)

def main():
    """
    Main function to fetch logs and send them to Elasticsearch.
    """
    while True:
        logs = fetch_logs()
        if logs:
            ingest_to_elasticsearch(logs)
        else:
            print("No logs found. Retrying...")
        time.sleep(30)  # Fetch logs every 30 seconds

if __name__ == "__main__":
    main()
