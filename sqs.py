import boto3

# Create an SQS client
sqs = boto3.client('sqs', region_name='us-east-1')  # Replace 'your-region' with the desired AWS region

# Define queue parameters
queue_name = 'myTatendaQueue'
attributes = {
    'DelaySeconds': '5',  # Delay for messages in the queue
    'MessageRetentionPeriod': '86400'  # Retain messages for 1 day
}

# Create the queue
try:
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes=attributes
    )
    print(f"Queue '{queue_name}' created successfully.")
    print(f"Queue URL: {response['QueueUrl']}")
except Exception as e:
    print(f"Error creating queue: {e}") 
    
    