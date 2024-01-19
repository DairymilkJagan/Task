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

