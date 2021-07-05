# terraform-python-hcl2-example

An example for Python -> HCL2 write for .tfvars

Medium article: [How to write HCL2 from python](https://nklya.medium.com/how-to-write-hcl2-from-python-53ac12e45874)

## How-to test

* [Install Terraform](https://www.terraform.io/downloads.html), tested on 0.14
* Run `terraform init`
* Run `./pets-gen.py`, with optional `-c <number of pets>` parameter
* Run `terraform apply`

Done, terraform will create pets from generated tfvars file and will show them in output.