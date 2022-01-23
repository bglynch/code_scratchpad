# Terraform

## Infrustructure as Code

The idea behind infrastructure as code (IAC) is that you write and execute code to define, deploy, update, and destroy your infrastructure. 

##### Configuration Management Tools

Chef, Puppet, Ansible, and SaltStack are all *configuration management tools*, which means that they are designed to install and manage software on existing servers. 

##### Server Templating Tools

An alternative to configuration management that has been growing in popularity recently are *server templating tools* such as Docker, Packer, and Vagrant.

##### Orchestration

Handling these tasks is the realm of *orchestration tools* such as Kubernetes, Marathon/Mesos, Amazon Elastic Container Service (Amazon ECS), Docker Swarm, and Nomad.

##### Provisioning Tools

*Provisioning tools* such as **Terraform**, CloudFormation, and OpenStack Heat are responsible for creating the servers themselves. In fact, you can use provisioning tools to not only create servers, but also databases, caches, load balancers, queues, monitoring, subnet configurations, firewall settings, routing rules, Secure Sockets Layer (SSL) certificates, and almost every other aspect of your infrastructure

---

### Install/Update Terraform

```bash
brew install tfenv                             # install tfenv
tfenv install 0.12.24 && tfenv use 0.12.24     # install and use chosen version of terraform

tfenv install 0.13.1 && tfenv use 0.13.1       # change version of terraform
```

### Terraform CLI

```bash
terraform init     # create a terraform project

terraform fmt      # auto format terraform code

terraform plan     # create an execution plan - specifies what actions terraform will take 

terraform apply                   # create or modify infrustructure
terraform apply --auto-approve    
terraform apply -target aws_instance.web_server_instance # deploy only specified resource

terraform destroy      # destroys resources in order which is needed
terraform destroy -target aws_instance.web_server_instance  # destroy only one resource

-----

terraform         # see list of all possible commands

terraform state       # see all possible state commands
terraform state list  # list out all the resources

# see detailed output for a resource
terraform state show <resource>.<resource name>  (e.g. terraform state show aws_eip.one)
```

---

### Resource Syntax

```json
resource "<provider>_<resource_type>" "name" {
	config options.....(will be key/value pairs)
}
```

##### Example

Create an AWS EC2 instance with the name `app`. Once created, run the bash command to start an apache server.

```bash
resource "aws_instance" "app" {
  instance_type     = "t2.micro"
  availability_zone = "us-east-2a"
  ami               = "ami-0c55b159cbfafe1f0"

  user_data = <<-EOF                        
              #!/bin/bash                   
              sudo service apache2 start
              EOF
  
  tags = {
    Name = "terraform-example"
  }              
}
```



- `user_data`: This is a Bash script that executes whenthe web server is booting. 
- `<<-EOF` and `EOF` : Terraform’s *heredoc* syntax, which allows you to create multiline strings without having to insert newline characters all over the place.



### Terminology

- **Expression**: An expression in Terraform is anything that returns a value
  - `instance_type     = "t2.micro"`
- **Reference**:  allows you to access values from other parts of your code
  - `aws_security_group.instance.id`

---

## Terraform Variables

### How to use

- **manual input** after running terraform apply

- **comand line argument**

  - ```bash
    $ terraform plan -var "server_port=8080"
    ```

- **export to shell** environmental variables: 

  - ```bash
    $ export TF_VAR_server_port=8080
    ```

- add **default value to variable** in terraform code

  - ```bash
    variable "number_example" {
      description = "An example of a number variable in Terraform"
      type        = number
      default     = 42
    }
    ```

- add to .tfvars file

#### Variable Types

- ```apl
  string, number, bool, list, map, set, object, tuple, any
  ```

#### Create variable samples

```bash
# checks to verify that the value you pass in is a number
variable "number_example" {
  description = "An example of a number variable in Terraform"
  type        = number
  default     = 42
}

# checks whether the value is a list
variable "list_example" {
  description = "An example of a list in Terraform"
  type        = list
  default     = ["a", "b", "c"]
}

# check that var is a list and only contains numbers
variable "list_numeric_example" {
  description = "An example of a numeric list in Terraform"
  type        = list(number)
  default     = [1, 2, 3]
}

# map that requires all of the values to be strings
variable "map_example" {
  description = "An example of a map in Terraform"
  type        = map(string)

  default = {
    key1 = "value1"
    key2 = "value2"
    key3 = "value3"
  }
}

# example of an object
variable "object_example" {
  description = "An example of a structural type in Terraform"
  type        = object({
    name    = string
    age     = number
    tags    = list(string)
    enabled = bool
  })

  default = {
    name    = "value1"
    age     = 42
    tags    = ["a", "b", "c"]
    enabled = true
  }
}
```



#### Use a variable

Typical

```bash
resource "aws_security_group" "instance" {
  name = "terraform-example-instance"

  ingress {
    from_port   = var.server_port
    to_port     = var.server_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

Curley Braces

```bash
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World" > index.html
              nohup busybox httpd -f -p ${var.server_port} &
              EOF
```



---

### Functions





#### Terraform Output

Give a text output in the command line after terraform apply is executed

```bash
#sample to output the private ip of the aws EC2 instance
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

- 