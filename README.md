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

#This Part Costs $$ and assumes you have a GCP account
Attach to the container and enter the following in command line
```
gcloud auth login
```
Follow the directions and authorize the container to use your google account
