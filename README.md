# EbookToAudioBook
Scripts, tools, and docs on how to take an ebook in epub format and turn it into an audiobook for your listening pleasure

This tutorial assumes you have a docker engine and the capability to create and run images

Open a terminal

```
git clone https://github.com/klogdog/EbookToAudioBook.git
```
```
cd EbookToAudioBook/app
```

```
docker build -t ebook-processor .
```

```
docker run -p 8501:8501 ebook-processor
```

Open a browser and navigate to the streamlit app
localhost:8501

Upload your desired .epub file
Parse the ebook
Breakup the sentences
Chunk the text
Download the zip

You now have a chuncked text of the ebook which is ready to be consumed by Google wavenet :)

# This Part Costs $$ and assumes you have a GCP account
Attach to the container and enter the following in command line
```
gcloud auth login
```
Follow the directions and authorize the container to use your google account

# Google wrote this part

Before you begin
Before you can send a request to the Text-to-Speech API, you must have completed the following actions. See the before you begin page for details.

Enable Text-to-Speech on a GCP project.
Make sure billing is enabled for Text-to-Speech.
Create and/or assign one or more service accounts to Text-to-Speech.
Download a service account credential key.
Make sure the service account has the following permissions roles to the output GCS bucket.
Storage Object Creator
Storage Object Viewer
Set your authentication environment variable.
