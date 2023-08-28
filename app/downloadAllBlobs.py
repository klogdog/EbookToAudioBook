from google.cloud import storage
import os

def download_all_files(bucket_name, destination_directory):
    """
    Downloads all files from a GCS bucket to a local directory.

    :param bucket_name: Name of the GCS bucket.
    :param destination_directory: Local directory to save the files to.
    """
    # Create a client
    client = storage.Client()

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get the list of all files in the bucket
    blobs = bucket.list_blobs()

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    # Download each file
    for blob in blobs:
        destination_file_name = os.path.join(destination_directory, blob.name)
        os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
        blob.download_to_filename(destination_file_name)

# Example usage:
# download_all_files('my-bucket', 'my-local-directory')