import streamlit as st
import os
from pathlib import Path
import shutil
import parseebook
import breakUpLongSentences
import chunkText
import googleCloudTextToWav
import downloadAllBlobs
import combineWaveFiles
import multiprocessing
import wavToMP3
from multiprocessing import Pool

# Create a folder to store the uploaded files
os.makedirs('uploads', exist_ok=True)

# List of Google Cloud locations
locations = [
    'asia-east1', 'asia-east2', 'asia-northeast1', 'asia-northeast2',
    'asia-northeast3', 'asia-south1', 'asia-south2', 'asia-southeast1',
    'asia-southeast2', 'australia-southeast1', 'australia-southeast2',
    'europe-central2', 'europe-north1', 'europe-west1', 'europe-west2',
    'europe-west3', 'europe-west4', 'europe-west6', 'northamerica-northeast1',
    'northamerica-northeast2', 'southamerica-east1', 'us-central1', 'us-east1',
    'us-east4', 'us-west1', 'us-west2', 'us-west3', 'us-west4'
]

# Define the parse ebook function
def parse_ebook(file_path):
    # Get the text content from the EPUB file
    epub_text = parseebook.read_epub_as_text(file_path)
    cleaned_text = parseebook.remove_special_characters(epub_text)
    
    # Save the extracted text to a .txt file
    txt_path = file_path.parent / (file_path.stem + '.txt')
    parseebook.save_as_txt(cleaned_text, txt_path)
    
    return txt_path

# Define the break up sentences function
def break_up_sentences(txt_path):
    # Read from the text file
    text_content = breakUpLongSentences.read_from_txt(txt_path)
    
    # Insert a period every 100 words
    modified_text = breakUpLongSentences.insert_period_every_n_words(text_content)
    
    # Save the modified text back to a .txt file
    modified_txt_path = txt_path.parent / (txt_path.stem + '_modified.txt')
    breakUpLongSentences.save_as_txt(modified_text, modified_txt_path)
    
    return modified_txt_path

# Define the chunk text function
def chunk_text(modified_txt_path):
    # Read from the modified text file
    text_content = chunkText.read_from_txt(modified_txt_path)
    
    # Get the ebook's name
    ebook_name = uploaded_file.name.rsplit('.', 1)[0]
    output_folder = f'output/{ebook_name}'
    
    # Split the text into multiple files
    chunkText.split_text_into_files(text_content, output_folder=output_folder, ebookName= ebook_name)
    
def process_file(file_name, output_folder, projectID, location, bucketName):
    file_path = os.path.join(output_folder, file_name)
    if file_path.endswith('.txt'):
        output_wav_name = os.path.splitext(file_name)[0]
        text = chunkText.read_from_txt(file_path)
        text = text.replace('..', '.') # Remove double periods
        googleCloudTextToWav.synthesize_long_audio(projectID, location, bucketName, text, output_wav_name)

# Streamlit app
st.title('Ebook Processor')

# ProjectID input
projectID = st.text_input('Enter ProjectID')

# GCS Bucket Name
bucketName = st.text_input('Enter Bucket Name')

# Location dropdown
location = st.selectbox('Select Location', locations)

# File uploader
uploaded_file = st.file_uploader("Choose an EPUB file", type="epub")

if uploaded_file is not None:
    # Save the uploaded file to the uploads folder
    file_path = Path('uploads') / uploaded_file.name
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.write(f"Uploaded file: {file_path}")
    
    # Parse Ebook
    if st.button('Parse Ebook'):
        st.write('Parsing ebook...')
        txt_path = parse_ebook(file_path)
        st.write(f'Text saved to: {txt_path}')
        # Save the path to the txt file for the next steps
        st.session_state.txt_path = txt_path

    # Break Up Sentences
    if st.button('Break Up Sentences'):
        st.write('Breaking up sentences...')
        modified_txt_path = break_up_sentences(st.session_state.txt_path)
        st.write(f'Modified text saved to: {modified_txt_path}')
        # Save the path to the modified txt file for the next step
        st.session_state.modified_txt_path = modified_txt_path

    # Chunk Text
    if st.button('Chunk Text'):
        st.write('Chunking text...')
        chunk_text(st.session_state.modified_txt_path)

    # Convert Text to WAV
    if st.button('Convert Text to WAV'):
        st.write('Converting text to WAV...')
        
        # Get the ebook's name
        ebook_name = uploaded_file.name.rsplit('.', 1)[0]
        output_folder = f'output/{ebook_name}'      

        # Convert text in each file to WAV
        # Create a pool of processes
        availableCores = multiprocessing.cpu_count() // 2
        if availableCores < 1:
            availableCores = 1
        with Pool(processes=availableCores ) as pool:
            # Apply the process_file function to each file in the output_folder
            pool.starmap(process_file, [(file_name, output_folder, projectID, location, bucketName) for file_name in sorted(os.listdir(output_folder), key=lambda x: int(x.replace(ebook_name, '').replace('.txt', '')))])
        st.write('Text converted to WAV successfully')

    # Download All Blobs
    if st.button('Download All Blobs'):
        st.write('Downloading all blobs...')
        downloadAllBlobs.download_all_files(bucketName, "wave")
        st.write('All blobs downloaded successfully')
    # Combine Wave Files
    if st.button('Combine Wave files'):
        st.write('Combining wave files...')
        combineWaveFiles.combine_wav_files(uploaded_file.name.rsplit('.', 1)[0])
        st.write('wav file written successfully')
    # Convert WAV to MP3
    if st.button('Convert WAV to MP3'):
        st.write('Converting..')
        wavToMP3.convert_wav_to_mp3(uploaded_file.name.rsplit('.', 1)[0] + ".wav", uploaded_file.name.rsplit('.', 1)[0] + ".mp3")
        st.write('mp3 file written successfully')
        # Zip the MP3 file
        mp3_file = uploaded_file.name.rsplit('.', 1)[0] + ".mp3"
        shutil.make_archive(mp3_file.rsplit('.', 1)[0], 'zip', '.', mp3_file)
        zip_file = mp3_file + ".zip"
        
        # Make the zip file available for download
        with open(zip_file, 'rb') as f:
            bytes = f.read()
        st.download_button('Download MP3 Zip File', data=bytes, file_name=f"{mp3_file}.zip", mime='application/zip')