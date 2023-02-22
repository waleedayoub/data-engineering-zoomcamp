locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
<<<<<<< HEAD
  description = "possible-lotus-375803"
=======
  description = "Your GCP Project ID"
>>>>>>> class/main
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
<<<<<<< HEAD
  default = "northamerica-northeast1"
=======
  default = "europe-west6"
>>>>>>> class/main
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "trips_data_all"
<<<<<<< HEAD
}
=======
}
>>>>>>> class/main
