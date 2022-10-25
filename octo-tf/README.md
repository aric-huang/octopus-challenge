# SQS_Queues

A Terraform module to create SQS queues, Dead Letter Queues, and their respective access management infrastructure on AWS given a list of strings.

Before using this module, you will first need to set up Terraform locally and familiarize yourself with it's commands via the [AWS get started](https://learn.hashicorp.com/collections/terraform/aws-get-started) guide 

## Usage 
To use this module, you should source it and pass in your list of queue names like shown below.

```
module "cool_sqs_queue" {
  source        = "../sqs/"
  queue_names   = ["cool_queue_name_1", "queue_2"]
}
```

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| queue_names | The list of names to create SQS queues for | list(string) | - | yes |

## Outputs

| Output Name | meaning |
|-------------|---------|
| `queue_arns` | A list of queue arns for all of the SQS queues |
| `consume_policy_arn` | The iam policy arns for SQS message consumption |
| `write_policy_arn` | The iam policy arns for SQS message writing |