import ebooklib
from ebooklib import epub
import re
from bs4 import BeautifulSoup

def read_epub_as_text(file_path):
    book = epub.read_epub(file_path)
    text = ''
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.content, 'html.parser')
        text += soup.get_text()
    return text

def remove_special_characters(text):
    # Remove all special characters except for periods, spaces, and alphanumeric characters
    cleaned_text = re.sub(r'[^a-zA-Z0-9 .]', '', text)
    return cleaned_text

def save_as_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Example usage:
# epub_path = 'path/to/your/ebook.epub'
# epub_text = read_epub_as_text(epub_path)
# cleaned_text = remove_special_characters(epub_text)
# save_as_txt(cleaned_text, 'output.txt')
