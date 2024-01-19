provider "google" {
  credentials = file("D:\\Product Task\\task\\Terraform-Task\\terraform-411609-2016aed69555.json")
  project     = "terraform-411609"
  region      = "us-central1"
}

# 1st Create Bucket 
resource "google_storage_bucket" "example_bucket" {
  name          = "demo-task"
  location      = "US"
  force_destroy = true
}

# 2nd Create State file Bucket
terraform {
  backend "gcs" {
    bucket  = "demo-task"
    prefix  = "demo"
  }
}

# 3rd Depends on Modules 

resource "google_storage_bucket_object" "example_object" {
  name   = "file.txt"  # Name of the object in the bucket
  bucket = google_storage_bucket.example_bucket.name
  source = "D:\\Product Task\\task\\Terraform-Task\\file.txt"
  depends_on = [google_storage_bucket.example_bucket]

   metadata = {
    dynamic_key   = var.dynamic_value
    static_key    = "static_metadata_value"
  }
}

variable "dynamic_value" {
  description = "A dynamic value for the object metadata"
  type        = string
  default     = "default_dynamic_value"
}
