import google 
import google.cloud
import google.cloud.storage
import google.cloud.storage.bucket
import google.cloud.storage.client
import os

def blob_getter(filename, bucketname):
    storage_client = google.cloud.storage.client.Client()
    bucket = google.cloud.storage.bucket.Bucket(storage_client, name=bucketname)
    blob = bucket.blob(filename)
    return blob
#filename = "s.txt"
#bucketname = "pytutoring-bucket"

if __name__ == "__main__":
    blob = blob_getter("s.txt", "pytutoring-dev-bucket")
    blob.upload_from_filename("LICENSE")
