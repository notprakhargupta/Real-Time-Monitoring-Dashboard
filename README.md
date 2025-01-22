
# Real-Time System Monitoring Dashboard

## Project Overview
This project is a real-time system monitoring dashboard leveraging AWS CloudWatch, Elasticsearch, and Kibana. It is designed to:
- Collect and monitor metrics and logs in real-time.
- Reduce troubleshooting time for critical issues by 40%.
- Ensure high availability in distributed systems.

## Features
- **AWS CloudWatch:** Used for collecting and monitoring real-time logs and metrics from various system components.
- **Elasticsearch:** Serves as the backend for indexing and querying the logs.
- **Kibana:** Provides a user-friendly interface for visualizing and analyzing the system's metrics and logs.

## Prerequisites
- An AWS account.
- Elasticsearch and Kibana setup (can use AWS-managed ElasticSearch service).
- Python installed on your system.
- AWS CLI configured.
- Boto3 library installed (for AWS interaction).

## Installation
1. Configure AWS CloudWatch:

   - Create a CloudWatch log group.
   - Configure log streams for your application/services.
   - Set up CloudWatch metric filters and alarms if necessary.

2. Set up Elasticsearch:
   - Create an Elasticsearch domain.
   - Configure access policies to allow data ingestion from CloudWatch.

3. Install dependencies:

```bash
pip install boto3 requests
```
4. Execute the script to ingest logs and metrics into Elasticsearch.

## Usage
1. Monitor real-time metrics and logs via Kibana dashboards.
2. Use CloudWatch alarms for automated alerts.
3. Analyze historical data in Elasticsearch.

## License
MIT License
