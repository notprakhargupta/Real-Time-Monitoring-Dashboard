from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_image():
    if 'inputFile' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['inputFile']
    file.save('uploaded_image.jpg')
    return 'Image uploaded successfully'

import boto3

sqs = boto3.client('sqs')

web_to_app_queue_url = 'YOUR_WEB_TO_APP_QUEUE_URL'

def send_image_to_app(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    response = sqs.send_message(
        QueueUrl=web_to_app_queue_url,
        MessageBody=image_data
    )
    
    print("Image sent to App Tier:", response['MessageId'])

# Call this function after image upload
send_image_to_app('uploaded_image.jpg')

def receive_recognition_results():
    while True:
        response = sqs.receive_message(
            QueueUrl=app_to_web_queue_url,
            WaitTimeSeconds=20  # Long polling for efficient message retrieval
        )
        
        if 'Messages' in response:
            for message in response['Messages']:
                # Assuming recognition results are in the message body
                recognition_results = message['Body']
                print("Recognition Results:", recognition_results)
                
                # Delete the message from the queue
                sqs.delete_message(
                    QueueUrl=app_to_web_queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
        else:
            print("No messages received")
        
        time.sleep(5)  # Polling interval

# Call this function to start receiving recognition results
receive_recognition_results()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, threaded=True)
