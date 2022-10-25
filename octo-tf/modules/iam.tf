resource "aws_iam_policy" "sqs_consume_policy" {
    name   = "sqs-consume-policy"
    policy = data.aws_iam_policy_document.sqs_consume_policy_document.json
}

data "aws_iam_policy_document" "sqs_consume_policy_document" {
  statement {
    actions = [
      "sqs:ReceiveMessage",
      "sqs:DeleteMessage",
    ]
    resources = [
      jsonencode(aws_sqs_queue.terraform_queue[*].arn),
      jsonencode(aws_sqs_queue.terraform_queue_deadletter[*].arn),
    ]
  }
}

resource "aws_iam_policy" "sqs_write_policy" {
    name   = "sqs-write-policy"
    policy = data.aws_iam_policy_document.sqs_write_policy_document.json
}

data "aws_iam_policy_document" "sqs_write_policy_document" {
  statement {
    actions = [
      "sqs:SendMessage",
    ]
    resources = [
      jsonencode(aws_sqs_queue.terraform_queue_deadletter[*].arn),
    ]
  }
}
