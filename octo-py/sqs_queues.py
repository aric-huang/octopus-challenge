#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
# Gets the current number of items in SQS queues and their dead letter queues. #
################################################################################
import boto3
import sys

# Function uses list of queues and writes a dictionary string to stdout
def get_queues_message_totals(queues):
    # type: (list(str)) -> None
    # Create SQS resource
    # should probably ask for region to be passed in
    sqs = boto3.resource('sqs', 'us-east-1')

    toReturn = {}
    # loop to start checking if queue exists and if so, get the queue attributes
    for value in queues:
        dlq_name = value + '-dlq'

        #call get_messages function twice to get both values for queue and dlq
        active_messages, dlq_active_messages = get_messages_in_queue(value)
        
        #add values to dictionary to print out later
        toReturn[value] = active_messages
        toReturn[dlq_name] = dlq_active_messages

    sys.stdout.write(str(toReturn))

# Check if queue with name exists and returns number of messages in queue. 
# Returns error message with comment and exits if not found
def get_messages_in_queue(name):
    # type: (str) -> tuple[int, int]
    dlq_name = name + '-dlq'
    sqs = boto3.resource('sqs', 'us-east-1')
    # Using try catch here since get_queue_by_name might throw an exception if no queue with name is found
    # TODO: Find a cleaner way to do this without having to sys.exit()
    try: 
        sqs.get_queue_by_name(QueueName=name)
    except Exception as e:
        sys.stderr.write('queue with name: ' + name + ' does not exist, queue names are case sensitive\n{}'.format(e))
        sys.exit()
    messages = sqs.get_queue_by_name(QueueName=name).attributes.get('ApproximateNumberOfMessages')
    dlq_messages = sqs.get_queue_by_name(QueueName=dlq_name).attributes.get('ApproximateNumberOfMessages')
    return messages, dlq_messages


def main():
    queueList = []
    for value in sys.argv[1:]:
        queueList.append(value)
    get_queues_message_totals(queueList)

if __name__  == '__main__':
    main()
