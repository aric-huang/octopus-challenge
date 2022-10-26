output "queue_arns" {
  value = aws_sqs_queue.terraform_queue[*].arn
}

output "consume_policy_arn" {
  value = aws_iam_policy.sqs_consume_policy.arn
}

output "write_policy_arn" {
  value = aws_iam_policy.sqs_write_policy.arn
}

output "consume_role_arn" {
  value = aws_iam_role.sqs_consume_role
}

output "write_role_arn" {
  value = aws_iam_role.sqs_write_role
}
