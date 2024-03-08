# ======================================================================================
# =================================== PROVIDERS ========================================
# ======================================================================================
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# ======================================================================================
# =================================== RESOURCES ========================================
# ======================================================================================
resource "aws_instance" "" {
  ami           = var.ami
  instance_type = var.instance_type

  network_interface {
    network_interface_id = var.network_interface_id
    device_index         = 0
  }

  credit_specification {
    cpu_credits = "unlimited"
  }
}

# ======================================================================================
# =================================== VARIABLES ========================================
# ======================================================================================
variable "network_interface_id" {
  type = string
  default = "network_id_from_aws"
}

variable "ami" {
    type = string
    default = "ami-005e54dee72cc1d00"
}

variable "instance_type" {
    type = string
    default = "t2.micro"
}