# DynamoDB - Terraform

#### Docs

- [Resource: aws_dynamodb_table](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table)

### Create tf file to store aws provider

> ```bash
> touch aws.tf
> ```
> 
> ```json
> terraform {
>   required_providers {
>     aws = {
>       source  = "hashicorp/aws"
>       version = "~> 3.0"
>     }
>   }
> }
> 
> provider "aws" {
>   region  = "eu-west-1"
>   profile = "aws-profile"
> }
> ```



### Create file to store dynamodb 

##### Sample: Create Music Table with Partition Key and Sort Key using Provisioned billing mode

> ```json
> resource "aws_dynamodb_table" "Music" {
>   name           = "Music"
>   read_capacity  = 5
>   write_capacity = 5
>   hash_key       = "Artist"
>   range_key      = "SongTitle"
> 
>   attribute {
>     name = "Artist"
>     type = "S"
>   }
>   attribute {
>     name = "SongTitle"
>     type = "S"
>   }
>   tags = {
>     Name        = "dynamodb-table-1"
>     Environment = "production"
>   }
> }
> ```

##### Sample: Create Music Table with Partition Key and Sort Key using Provisioned billing mode

> ```bash
> resource "aws_dynamodb_table" "blynch-test-table" {
>   name         = "TestTable"
>   billing_mode = "PAY_PER_REQUEST"
>   hash_key     = "unique_id"
> 
>   attribute {
>     name = "unique_id"
>     type = "S"
>   }
>   attribute {
>     name = "customer"
>     type = "S"
>   }
>   # attribute {
>   #   name = "date"
>   #   type = "N"
>   # }
> 
>   global_secondary_index {
>     name               = "CustomerIndex"
>     hash_key           = "customer"
>     # range_key          = "date"
>     projection_type    = "INCLUDE"
>     non_key_attributes = ["size"]
>   }
> }
> ```

