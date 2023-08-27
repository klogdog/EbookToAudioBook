def read_from_txt(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_as_txt(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def split_text_into_files(text, words_per_file=5000, base_filename='output'):
    words = text.split()
    num_files = len(words) // words_per_file + (1 if len(words) % words_per_file else 0)
    
    for i in range(num_files):
        start_idx = i * words_per_file
        end_idx = (i+1) * words_per_file
        chunk = ' '.join(words[start_idx:end_idx])
        filename = f"{base_filename}_{i+1}.txt"
        save_as_txt(chunk, filename)
        print(f"Saved {filename}")

# Read from the text file
txt_path = 'path_to_your_text_file.txt'
text_content = read_from_txt(txt_path)

# Split the text into multiple files
split_text_into_files(text_content)
