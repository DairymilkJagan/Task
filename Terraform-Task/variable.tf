# 4 Try static and dynamic values passing for the variables that will be used by the resource during creationtime.
variable "bucket_name" {
  type    = string
  default = "demo-task"
}
# 4
variable "bucket_location" {
  type    = string
}