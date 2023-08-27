import os
import wave

def combine_wav_files(directory, output_filename):
    """
    Combine all .wav files in a directory into a single .wav file.
    
    :param directory: Path to directory containing .wav files
    :param output_filename: Path to the combined output .wav file
    """
    # List all files in the directory and filter only the .wav files
    files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    files = sorted(files)  # Sorting to combine in order
    
    # Open the first file to get properties
    with wave.open(os.path.join(directory, files[0]), 'rb') as w:
        params = w.getparams()

    # Create output file
    with wave.open(output_filename, 'wb') as output:
        output.setparams(params)
        for f in files:
            with wave.open(os.path.join(directory, f), 'rb') as w:
                output.writeframes(w.readframes(w.getnframes()))

if __name__ == "__main__":
    # Define directory containing .wav files and output filename
    dir_path = "./"  # This is the current directory. Change as needed.
    combined_output = "combined_output.wav"
    
    combine_wav_files(dir_path, combined_output)
    print(f"All .wav files in {dir_path} combined into {combined_output}!")
