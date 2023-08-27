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
