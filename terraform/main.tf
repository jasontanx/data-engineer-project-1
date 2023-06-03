provider "google" {
  credentials = file("/Users/junshengtan/Desktop/de-project/terraform/creds.json")
  project     = var.project_id
  region      = var.region
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id  = "eu_busy_airport"
  description = "This dataset is about European busiest airpots"
  location    = var.region

  labels = {
    environment = "default"
  }
}

resource "google_bigquery_table" "table" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = "eu_busy_airport_v1"

  schema = <<EOF
[
  { "name": "airport", "type": "STRING" },
  { "name": "city_served", "type": "STRING" },
  { "name": "country", "type": "STRING" },
  { "name": "passenger_2021", "type": "INTEGER" },
  { "name": "passenger_2020", "type": "INTEGER" },
  { "name": "change_2021_2020", "type": "INTEGER" },
  { "name": "change_percentage_2021_2020", "type": "FLOAT" }
]
EOF

}


    
