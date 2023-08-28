import os
import wave

def combine_wav_files(ebook_name):
    """
    Combine all .wav files in a directory into a single .wav file.
    
    :param directory: Path to directory containing .wav files
    :param output_filename: Path to the combined output .wav file
    """
    directory = "wave"
    # List all files in the directory and filter only the .wav files
    files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    files = sorted(files, key=lambda x: int(x.replace(ebook_name, '').replace('.wav', '')))
    
    # Open the first file to get properties
    with wave.open(os.path.join(directory, files[0]), 'rb') as w:
        params = w.getparams()

    # Create output file
    with wave.open(ebook_name + ".wav", 'wb') as output:
        output.setparams(params)
        for f in files:
            with wave.open(os.path.join(directory, f), 'rb') as w:
                output.writeframes(w.readframes(w.getnframes()))