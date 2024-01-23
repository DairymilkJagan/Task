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
  name   = "file.txt"  # object in the bucket
  bucket = google_storage_bucket.example_bucket.name
  source = "D:\\Product Task\\task\\Terraform-Task\\file.txt"
  depends_on = [google_storage_bucket.example_bucket]

}


# terraform apply -var="bucket_location=your_desired_location"

#5. Print the output of a resource which you have created.
output "bucket_url" {
  value = google_storage_bucket.example_bucket.url
}