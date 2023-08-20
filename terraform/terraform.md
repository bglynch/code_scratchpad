# Terraform

![Untitled Diagram](terraform.assets/Untitled Diagram.svg) 

## Infrustructure as Code

The idea behind infrastructure as code (IAC) is that you write and execute code to define, deploy, update, and destroy your infrastructure. 

##### Configuration Management Tools

>  Chef, Puppet, Ansible, and SaltStack are all *configuration management tools*, which means that they are designed to install and manage software on existing servers. 

##### Server Templating Tools

>  An alternative to configuration management that has been growing in popularity recently are *server templating tools* such as Docker, Packer, and Vagrant.

##### Orchestration

>  Handling these tasks is the realm of *orchestration tools* such as Kubernetes, Marathon/Mesos, Amazon Elastic Container Service (Amazon ECS), Docker Swarm, and Nomad.

##### Provisioning Tools

>  *Provisioning tools* such as **Terraform**, CloudFormation, and OpenStack Heat are responsible for creating the servers themselves. In fact, you can use provisioning tools to not only create servers, but also databases, caches, load balancers, queues, monitoring, subnet configurations, firewall settings, routing rules, Secure Sockets Layer (SSL) certificates, and almost every other aspect of your infrastructure

---

## Install/Update Terraform

> ```bash
> brew install tfenv                             # install tfenv
> tfenv install 0.12.24 && tfenv use 0.12.24     # install and use chosen version of terraform
> 
> tfenv install 0.13.1 && tfenv use 0.13.1       # change version of terraform
> ```
>

## Terraform CLI

> ###### Link: [How to set AWS credentials before running](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration)
>
> ```bash
> # option 01: command line with secret and access keys
> export AWS_ACCESS_KEY_ID="anaccesskey"
> export AWS_SECRET_ACCESS_KEY="asecretkey"
> export AWS_REGION="us-west-2"
> 
> # option 01: command line with profile
> export AWS_PROFILE="profile"
> export AWS_REGION="us-west-2"
> ```
>
> ###### help commands
>
> ```bash
> terraform         # see list of all possible commands
> terraform state   # see all possible state commands
> terraform version # see version
> ```
>
> ###### Format and Validate 
>
> ```bash
> terraform fmt                     # auto format terraform code
> terraform validate                # validate code for syntax
> terraform validate -backend=false # validate code skip backend validation
> ```
>
> ###### Initialise 
>
> ```bash
> terraform init     # create a terraform project
> ```
>
> ###### Plan, Deploy and Cleanup Infrastructure 
>
> ```bash
> terraform plan               # create deployment plan - specifies what actions terraform will take
> terraform plan -out plan.out # output deployment plan to plan.out
> terraform plan -destroy      # outputs a destroy plan
> terraform plan -var 'name=value'
> 
> terraform apply                   # create or modify infrustructure
> terraform apply --auto-approve    # apply changes without being prompted to enter “yes”
> terraform apply plan.out          # use the plan.out plan file to deploy infrastructure
> terraform apply -target aws_instance.web_server_instance # deploy only specified resource
> 
> terraform apply -var my_region_variable=us-east-1 # pass a variable via command-line while applying a configuration
> #lock the state file so it can’t be modified by any other Terraform apply or modification action(possible only where backend allows locking)
> terraform apply -lock=true 
> # do not reconcile state file with real-world resources(helpful with large complex deployments for saving deployment time)
> terraform apply refresh=false
> 
> terraform refresh      # reconcile the state in Terraform state file with real-world resources
>                     # does not modify the infrastructure in any way, it only updates the state file
> 
>    terraform destroy                  # destroys resources in order which is needed
> terraform destroy --auto-approve
> terraform destroy -target aws_instance.web_server_instance  # destroy only one resource
> 
> terraform providers # get information about providers used in current configuration
> ```
> 
> ###### State
>
> ```bash
>terraform state list  # list out all the resources tracked via the current state file
> 
> terraform state show aws_instance.my_ec2   # show details stored in Terraform state for the resource
> terraform state pull > terraform.tfstate   # download and output terraform state to a file
> 
> terraform state rm  aws_instance.myinstace # unmanage a resource, delete it from Terraform state file
> ```
> 
> ###### Outputs
>
> ```bash
>terraform output                     # list all outputs as stated in code
> terraform output instance_public_ip  # list out a specific declared output
> terraform output -json               # list all outputs in JSON format
> ```



---

## Location of statefile

> - [Locally](https://developer.hashicorp.com/terraform/language/v1.1.x/settings/backends/local)
> - [AWS S3](https://developer.hashicorp.com/terraform/language/v1.1.x/settings/backends/s3)

### Terraform Backends

A Terraform backend determines how Terraform loads and stores state

- local backend, which stores the state file on your local disk
- Remote backends allow you to store the state file in a remote, shared store. e.g AWS S3

### Benifits of AWS S£ as a backend

- It supports encryption, which reduces worries about storing sensitive data in state files.
- It supports locking via DynamoDB
- It supports versioning, so every revision of your state file is stored,

> ###### Typical AWS S3 backend
>
> ```python
> provider "aws" {
>   region = "us-east-2"
> }
> 
> resource "aws_s3_bucket" "terraform_state" {
>   bucket = "terraform-up-and-running-state"
>  
>   # Prevent accidental deletion of this S3 bucket
>   lifecycle {
>     prevent_destroy = true
>   }
> }
> ```
>
> Notes:
>
> - `bucket`:  
>   - Note that S3 bucket names must be globally unique among all AWS customers
> - `prevent_destroy`
>   - any attempt to delete that resource (e.g., by running terraform destroy) will cause Terraform to exit with an error
>   - if you really mean to delete it, you can just comment that setting out.
>
> ###### Updates to the S3 Bucket
>
> ```javascript
> // enable versioning so every update to a file in creates a new version of that file
> resource "aws_s3_bucket_versioning" "enabled" {
>   bucket = aws_s3_bucket.terraform_state.id
>   versioning_configuration {
>     status = "Enabled"
>   }
> }
> 
> // turn server-side encryption on by default for all data written to this S3 bucket
> resource "aws_s3_bucket_server_side_encryption_configuration" "default" {
>   bucket = aws_s3_bucket.terraform_state.id
> 
>   rule {
>     apply_server_side_encryption_by_default {
>       sse_algorithm = "AES256"
>     }
>   }
> }
> 
> // block all public access to the S3 bucket
> // terraform state files may contain sensitive data and secrets, it’s worth adding this extra layer of protection
> resource "aws_s3_bucket_public_access_block" "public_access" {
>   bucket                  = aws_s3_bucket.terraform_state.id
>   block_public_acls       = true
>   block_public_policy     = true
>   ignore_public_acls      = true
>   restrict_public_buckets = true
> }
> 
> // create a DynamoDB table to use for locking
> resource "aws_dynamodb_table" "terraform_locks" {
>   name         = "terraform-up-and-running-locks"
>   billing_mode = "PAY_PER_REQUEST"
>   hash_key     = "LockID"
> 
>   attribute {
>     name = "LockID"
>     type = "S"
>   }
> }
> ```
>
> ###### Update the backend code
>
> ```python
> terraform {
>   backend "s3" {
>     bucket         = "terraform-up-and-running-state"
>     key            = "global/s3/terraform.tfstate"
>     region         = "us-east-2"
> 
>     dynamodb_table = "terraform-up-and-running-locks"
>     encrypt        = true
>   }
> }
> ```
>
> ###### Note: Updating backend
>
> Need to run `terrafrom init` after updating the backend

## Configuration Files

### Resource Syntax

> ###### Comments
>
> ```
> #
> //
> /*  */
> ```
>
> ###### Example: Generic
>
> ```json
> resource "<provider>_<resource_type>" "name" {
> 	config options.....(will be key/value pairs)
> }
> ```
>
> ###### Example: Create an AWS EC2 instance with the name `app`. Once created, run the bash command to start an apache server.
>
> ```h
> resource "aws_instance" "app" {
>   instance_type     = "t2.micro"
>   availability_zone = "us-east-2a"
>   ami               = "ami-0c55b159cbfafe1f0"
> 
>   user_data = <<-EOF                        
>               #!/bin/bash                   
>               sudo service apache2 start
>               EOF
>   
>   tags = {
>     Name = "terraform-example"
>   }              
> }
> ```
>
> - `user_data`: This is a Bash script that executes whenthe web server is booting. 
> - `<<-EOF` and `EOF` : Terraform’s *heredoc* syntax, which allows you to create multiline strings without having to insert newline characters all over the place.

### Terminology

- **Expression**: An expression in Terraform is anything that returns a value
  - `instance_type     = "t2.micro"`
- **Reference**:  allows you to access values from other parts of your code
  - `aws_security_group.instance.id`



---



## Variables

### How to use

> ###### manual input
>
> - variables input on the command line after running `terraform apply`
>
> ###### command line arg
>
> ```bash
> terraform plan -var "server_port=8080"
> ```
>
> ###### **export to shell** environmental variables, before running terraform command
>
> ```bash
> export TF_VAR_server_port=8080
> terraform plan
> ```
>
> ###### add **default value to variable** in terraform code
>
> ```bash
> # Declaring
> variable "number_example" {
>   description = "An example of a number variable in Terraform"
>   type        = number
>   default     = 42
> }
> 
> # Calling
> var.number_example
> ```
>
> ###### create .tfvars file
>
> - store values in tfvars file

### Variable Types

> ```apl
> # Primitive
> string, number, bool
> 
> # Collection
> list, map, set
> 
> # Structural
> object, tuple
> 
> any
> ```

### Create variable samples with type restrictions

> ###### number
>
> ```bash
> # checks to verify that the value you pass in is a number
> variable "number_example" {
> description = "An example of a number variable in Terraform"
> type        = number
> default     = 42
> }
> ```
>
> ###### list
>
> ```bash
> # checks whether the value is a list
> variable "list_example" {
> description = "An example of a list in Terraform"
> type        = list
> default     = ["a", "b", "c"]
> }
> 
> # call
> 
> ```
>
> ###### list of numbers only
>
> ```bash
> # check that var is a list and only contains numbers
> variable "list_numeric_example" {
> description = "An example of a numeric list in Terraform"
> type        = list(number)
> default     = [1, 2, 3]
> }
> ```
>
> ###### map where values are strings
>
> ```bash
> # map that requires all of the values to be strings
> variable "map_example" {
> description = "An example of a map in Terraform"
> type        = map(string)
> 
> default = {
>  key1 = "value1"
>  key2 = "value2"
>  key3 = "value3"
> }
> }
> ```
>
> ###### object
>
> ```bash
> # example of an object
> variable "object_example" {
> description = "An example of a structural type in Terraform"
> type        = object({
>  name    = string
>  age     = number
>  tags    = list(string)
>  enabled = bool
> })
> 
> default = {
>  name    = "value1"
>  age     = 42
>  tags    = ["a", "b", "c"]
>  enabled = true
> }
> }
> ```

### Use a variable

> ###### Typical
>
> ```bash
> resource "aws_security_group" "instance" {
>   name = "terraform-example-instance"
> 
>   ingress {
>     from_port   = var.server_port  # variable used here
>     to_port     = var.server_port  # variable used here
>     protocol    = "tcp"
>     cidr_blocks = ["0.0.0.0/0"]
>   }
> }
> ```
>
> ###### Curley braces
>
> ```
>   user_data = <<-EOF
>               #!/bin/bash
>               echo "Hello, World" > index.html
>               nohup busybox httpd -f -p ${var.server_port} &
>               EOF
> ```

---

## Functions





---



## Output

Give a text output in the command line after terraform apply is executed

```bash
# sample to output the private ip of the aws EC2 instance
# value is gotten from running `terraform state show aws_instance.web_server_instance`
output "server_private_id" {
  value = aws_instance.web_server_instance.private_ip
}
```

#### Terraform Variables

```bash
# example variable
variable "subnet_prefix" {
  description = "cidr block for the subnet"
  default     = "10.0.66.0/24"
  type        = string
}
```



```bash
# dont specify the value
-- will be prompted for the value on the CLI after executing `terraform apply`

# specify the variable value on the CLI
terraform apply -var "<var name>=<var value>"

# store the variable values in a terraform variables file with default naming
touch terraform.tfvars
-- will automatically be checked for variables when `terraform apply` is run

# store the variable values in a terraform variables file with custom file name
touch variables.tfvars
terraform apply -var-file variables.tfvars
```

#### Variable as List of Objects

###### terraform.tfvars

```json
subnet_prefix = [{cidr_block = "10.0.1.0/24", name = "prod_subnet"}, 
								 {cidr_block = "10.0.2.0/24", name = "dev_subnet"}]
```

###### main.tf

```json
...

resource "aws_subnet" "subnet_1" {
  vpc_id     = aws_vpc.prod_vpc.id
  cidr_block = var.subnet_prefix[0].cidr_block
  availability_zone = "eu-west-1a"
  tags = {
      Name = var.subnet_prefix[0].name
  }
}

resource "aws_subnet" "subnet_2" {
  vpc_id     = aws_vpc.prod_vpc.id
  cidr_block = var.subnet_prefix[1].cidr_block
  availability_zone = "eu-west-1a"
  tags = {
      Name = var.subnet_prefix[1].name
  }
}

...
```



---

### Terraform Modules

A *Terraform module*  is a reusable piece of terraform code. You create a module and reuse it in multiple places throughout your code

Open up the *main.tf* file in *modules/services/webserver-cluster* and remove the `provider` definition. Providers should be configured by the user of the module and not by the module itself.

---



### Talk Notes: How to Build Reusable, Composable, Battle tested Terraform Modules

https://www.youtube.com/watch?v=LVgP63BkhKQ&list=LL&index=94&ab_channel=HashiCorp

#### What is a Module?

- They are like reusable blueprints for your infrastructure

### How to use a Module

#### Basic Example

- create a terraform code to create AWS EC2 instance
- create module using that code

> #### Create Directories and Terraform Code and Deploy
>
> ```bash
> mkdir terraform-example
> touch terraform-example/main.tf
> cd terraform-example
> code main.tf
> ```
>
> ```bash
> # terraform-example/main.tf
> 
> # Configure the AWS provider
> provider "aws" {
>   region = "us-east-1"
> }
> 
> # Create an EC2 instance
> resource "aws_instance" "app" {
>   ami               = "ami-0c55b159cbfafe1f0"
>   instance_type     = "t2.micro"
> 
>   tags = {
>     Name = "example"
>   }              
> }
> ```
>
> ```bash
> terraform init
> terraform plan
> terraform apply
> ```
>
> 
>
> #### Run code above as a Module
>
> - Even though the code is simple, any terraform code can be a module
>
> ```bash
> cd ..
> mkdir my-service
> touch my-service/main.tf
> cd my-service
> ```
>
> - code below will create 2 servers, by using all the terraform code in `"../terraform-example"`
>
> ```bash
> # my-service/main.tf
> 
> module "foo" {
> 	source = "../terraform-example"
> }
> 
> module "bar" {
> 	source = "../terraform-example"
> }
> ```
>
> ```bash
> terraform init
> terraform plan
> ```
>
> 
>
> #### Update Module code to make configurable
>
> - update instance name to be a terraform variable
>
> ```bash
> # terraform-example/main.tf
> 
> # Configure the AWS provider
> provider "aws" {
>   region = "us-east-1"
> }
> 
> # Create an EC2 instance
> resource "aws_instance" "app" {
>   ami               = "ami-0c55b159cbfafe1f0"
>   instance_type     = "t2.micro"
> 
>   tags = {
>     Name = "${var.instance_name}"
>   }              
> }
> 
> variable "instance_name" {}
> ```
>
> - update code that calls module to use variable
>
> ```bash
> # my-service/main.tf
> 
> module "foo" {
> 	source = "../terraform-example"
> 	instance_name = "foo"
> }
> 
> module "bar" {
> 	source = "../terraform-example"
> 	instance_name = "bar"
> }
> ```
>
> - now we can run `terrafrom plan` from withing `my-service` dir to see that 

#### Folder Structure

###### Simple Module

> ```bash
> .
> ├── main.tf       # resources creted 
> ├── outputs.tf    # the 'outputs' for what the module returns
> ├── variables.tf  # the 'inputs' to your module 
> └── README.md     # documentation
> ```

###### More Complex Module

> ```bash
> .
> ├── main.tf      
> ├── outputs.tf   
> ├── variables.tf 
> ├── README.md
> ├── modules
> │   ├── submodule-bar
> │   │   ├── main.tf     
> │   │   ├── outputs.tf  
> │   │   └── variables.tf
> │   └── submodule-foo    
> │       ├── install.sh     # submodule does not have to be terraform code
> │       └── run.sh
> ├── examples
> │   ├── example-bar
> │   │   ├── main.tf     
> │   │   ├── outputs.tf  
> │   │   └── variables.tf
> │   └── example-foor
> │       ├── main.tf     
> │       ├── outputs.tf  
> │       └── variables.tf
> └── test 
>     ├── example_foo_test.go
>     └── example_cra_test.go
> ```
>
> - Submodule
>   - handles one use case
> - examples
>   - executable documentation
>   - shows you how to use submodules in different permeatations
> - [tests](https://youtu.be/LVgP63BkhKQ?list=LL&t=1853)
>   - typically integration tests
>   - how they work
>     - run terraform apply to deploy the code into a real account
>     - validate that it works as expected
>     - run terraform destroy to clean up

---



#### Terrafrom Files

- .terraform
  - gets created after we run `terraform init`
  - configs for resources are stored in here
- terraform.tfstate
  - current state of the terraform deployment
  - dont modify values in this file
- 

---

### Keywords

- terraform
- module
- resource
- provider
- variable
- data
- locals
- output
- 

---

## Links

###### Talks

- **How to Build Reusable, Composable, Battle tested Terraform Modules,**  by Yevgeniy Brikman, 2017