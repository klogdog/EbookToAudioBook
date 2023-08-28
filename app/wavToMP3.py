from pydub import AudioSegment

def convert_wav_to_mp3(wav_file, mp3_file):
    sound = AudioSegment.from_wav(wav_file)
    sound.export(mp3_file, format="mp3")
