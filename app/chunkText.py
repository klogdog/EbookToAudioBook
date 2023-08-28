import os
def read_from_txt(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_as_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def split_text_into_files(text, words_per_file=500, output_folder='output', ebookName="output_"):
    words = text.split()
    num_files = len(words) // words_per_file + (1 if len(words) % words_per_file else 0)
    
    os.makedirs(output_folder, exist_ok=True)
    
    for i in range(num_files):
        start_idx = i * words_per_file
        end_idx = (i+1) * words_per_file
        chunk = ' '.join(words[start_idx:end_idx])
        filename = f"{output_folder}/{ebookName}{i+1}.txt"
        save_as_txt(chunk, filename)
        print(f"Saved {filename}")