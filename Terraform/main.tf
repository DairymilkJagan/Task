provider "google" {
  credentials = file("D:\\Product Task\\task\\Terraform\\terraform-411609-2016aed69555.json")
  project     = "terraform-411609"
  region      = "us-central1"
}

# 1 Create any one resource using terraform in any cloud.
resource "google_storage_bucket" "ex_bucket" {
  name     = var.bucket_name
  location = "us-central1"  
  force_destroy = true
}

# 2 Try local and cloud storage backend configuration to store state files.
# 3 Try to use depends on module in code.
data "terraform_remote_state" "store" {
  depends_on = [google_storage_bucket.ex_bucket]
  backend    = "gcs"
  config = {
    bucket  = "demo-task"
    prefix  = "statefile"
  }
}

# 5. Print the output of a resource which you have created.
output "bucket_url" {
  value = google_storage_bucket.ex_bucket.url
}
