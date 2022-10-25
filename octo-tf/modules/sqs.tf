resource "aws_sqs_queue" "terraform_queue" {
    count = length(var.queue_names)
    name                      = "${var.queue_names[count.index]}"
    receive_wait_time_seconds = 20
    redrive_policy = jsonencode({
        deadLetterTargetArn = aws_sqs_queue.terraform_queue_deadletter[count.index].arn
        maxReceiveCount     = 4
    })
}

resource "aws_sqs_queue" "terraform_queue_deadletter" {
    count = length(var.queue_names)
    name                      = "${var.queue_names[count.index]}-dlq"
    receive_wait_time_seconds = 20
}
