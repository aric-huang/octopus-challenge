terraform {
    # I don't know what free tier aws allows, so lets not add this, but remote states are nice to have
    # backend "s3" {
    #     bucket = "terraformstate"
    #     key    = "sqs.tfstate"
    #     region = "us-east-1"
    # }
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 4.0"
        }
    }
}

# Configure the AWS Provider
provider "aws" {
    region = "us-east-1"
}
