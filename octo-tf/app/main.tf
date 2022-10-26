module "cool_sqs_queue" {
  source       = "../modules/"
  queue_names  = ["priority-10", "priority-100"]
  create_roles = true
}