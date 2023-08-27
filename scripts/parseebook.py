import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub_as_text(file_path):
    # Read the EPUB file
    book = epub.read_epub(file_path)
    
    # Extract the text content from the EPUB file
    text_content = ''
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.content, 'html.parser')
        text_content += soup.get_text() + '\n'
    
    return text_content

def save_as_txt(content, output_path):
    # Save the content to a .txt file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
