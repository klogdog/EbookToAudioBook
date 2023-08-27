import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub_as_text(file_path):
    book = epub.read_epub(file_path)
    text = ""
    
    for item in book.items:
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            text += soup.get_text() + "\n"
    
    return text

def save_as_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Use the function to read the EPUB file
epub_path = 'nameOfEbook.epub'
epub_text = read_epub_as_text(epub_path)

# Save the extracted text to a .txt file
txt_path = epub_path.rsplit('.', 1)[0] + '.txt'
save_as_txt(epub_text, txt_path)
print(f"Text saved to: {txt_path}")
