provider "google" {
 project = "playpen-2940ab" # change this
 region = "europe-west2"
 zone = "europe-west2-a"
 }

 resource "google_bigquery_dataset" "default" {
 dataset_id = "MS_student_dataset"
 description = "Student records"
 location = "EU"
}

resource "google_bigquery_table" "default" {
 dataset_id = google_bigquery_dataset.default.dataset_id
 table_id = "Student_ID"
 schema = file("${path.module}/student_schema.json")
 deletion_protection=false

}