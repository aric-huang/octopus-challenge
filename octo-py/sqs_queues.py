#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
# Gets the current number of items in SQS queues and their dead letter queues. #
################################################################################
import boto3
import sys


def get_queues_message_totals(queues):
    # Create SQS resource
    # should probably ask for region to be passed in
    sqs = boto3.resource('sqs', 'us-east-1')
    pass

def main():
    queueList = []
    for value in sys.argv[1:]:
        queueList.append(value)
    get_queues_message_totals(queueList)

if __name__  == '__main__':
    main()
