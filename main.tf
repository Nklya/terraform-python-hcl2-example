resource "random_pet" "this" {
  for_each = var.pets

  length = each.value.length
  separator = each.value.separator
}

variable "pets" {
  description = "Pets map"
  default     = {}
}

output "pets" {
  description = "Generated pets"
  value = [for i in random_pet.this: i.id]
}
