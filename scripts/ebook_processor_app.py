import streamlit as st
import os
from pathlib import Path
import shutil
import parseebook
import breakUpLongSentences
import chunkText

# Create a folder to store the uploaded files
os.makedirs('uploads', exist_ok=True)

# Define the parse ebook function
def parse_ebook(file_path):
    # Get the text content from the EPUB file
    epub_text = parseebook.read_epub_as_text(file_path)
    
    # Save the extracted text to a .txt file
    txt_path = file_path.parent / (file_path.stem + '.txt')
    parseebook.save_as_txt(epub_text, txt_path)
    
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
    chunkText.split_text_into_files(text_content, output_folder=output_folder)
    
    # Create a zip archive of the output folder
    shutil.make_archive(output_folder, 'zip', output_folder)
    zip_file = f"{output_folder}.zip"
    
    st.write('Text chunked successfully')
    
    # Make the zip file available for download
    with open(zip_file, 'rb') as f:
        bytes = f.read()
    st.download_button('Download Zip File', data=bytes, file_name=f"{ebook_name}.zip", mime='application/zip')

# Streamlit app
st.title('Ebook Processor')

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
