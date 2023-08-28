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
[Link text Here](localhost:8501)
