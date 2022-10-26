variable "queue_names" {
  description = "A list of SQS queue names"
  type        = list(string)
  default     = []
}

variable "create_roles" {
  description = "A flag to create iam_roles"
  default     = false
}

