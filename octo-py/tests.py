import boto3
from moto import mock_sqs
import sqs_queues

@mock_sqs
def test_get_messages_in_queue_happy():
    # Create SQS resource
    sqs = boto3.resource('sqs', 'us-east-1')

    # Create queue and dlq, just for testing, don't need to correlate them
    queue = sqs.create_queue(QueueName='test-queue')
    dlq   = sqs.create_queue(QueueName='test-queue-dlq')

    # Push message into queue before actual testing so not everything is just 0
    queue.send_message(MessageBody='test-message')

    result = sqs_queues.get_queues_message_totals['test-queue', 'test-queue-dlq']
    expected = {{'test-queue': '1', 'test-queue-dlq': '0'}}
    assert result['test-queue'] == expected['test-queue'], "function returned queue doesn't match expected result"
    print("Number of messages in queues matches")

@mock_sqs
def test_get_messages_in_queue_number_mismatch():
    # Create SQS resource
    sqs = boto3.resource('sqs', 'us-east-1')

    # Create queue and dlq, just for testing, don't need to correlate them
    queue = sqs.create_queue(QueueName='test-queue')
    dlq   = sqs.create_queue(QueueName='test-queue-dlq')

    # Push message into queue before actual testing so not everything is just 0
    queue.send_message(MessageBody='test-message')

    result = sqs_queues.get_queues_message_totals['test-queue', 'test-queue-dlq']
    expected = {{'test-queue': '0', 'test-queue-dlq': '0'}}
    assert result['test-queue'] != expected['test-queue'], "function returned number shouldn't match expected result but does match"
    print("Number of messages in queues do not match")
