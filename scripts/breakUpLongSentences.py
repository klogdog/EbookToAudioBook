def insert_period_every_n_words(text, n=100):
    words = text.split()
    for i in range(n, len(words), n):
        words[i] = words[i] + '.'
    return ' '.join(words)

def read_from_txt(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_as_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Read from the text file
txt_path = 'path_to_your_text_file.txt'
text_content = read_from_txt(txt_path)

# Insert a period every 100 words
modified_text = insert_period_every_n_words(text_content)

# Save the modified text back to a .txt file
modified_txt_path = txt_path.rsplit('.', 1)[0] + '_modified.txt'
save_as_txt(modified_text, modified_txt_path)
print(f"Modified text saved to: {modified_txt_path}")
