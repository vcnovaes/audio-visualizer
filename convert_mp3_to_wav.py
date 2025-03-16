from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    """
    Converts an MP3 file to a WAV file.

    Parameters:
        mp3_file (str): Path to the input MP3 file.
        wav_file (str): Path to the output WAV file.
    """
    # Load the MP3 file
    audio = AudioSegment.from_file(mp3_file, format="mp3")
    
    # Export as WAV
    audio.export(wav_file, format="wav")
    print(f"Converted {mp3_file} to {wav_file}")


convert_mp3_to_wav("assets/capitain.mp3", "assets/capitain.wav")