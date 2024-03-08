# Set terraform version
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Set provider as aws
provider "aws" {
  region  = "eu-west-1"
  profile = "aws-profile"
}

# create a dynamodb table
#  - primary key: "unique_id"
#  - index on "customer"
resource "aws_dynamodb_table" "blynch-test-table" {
  name         = "TestTable"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "unique_id"

  attribute {
    name = "unique_id"
    type = "S"
  }
  
  attribute {
    name = "customer"
    type = "S"
  }

  global_secondary_index {
    name               = "CustomerIndex"
    hash_key           = "customer"
    projection_type    = "INCLUDE"
    non_key_attributes = ["size"]
  }
}