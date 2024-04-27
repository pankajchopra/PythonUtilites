import subprocess


def convert_mp3_to_wav(mp3_file, wav_file):
    command = ["ffmpeg", "-i", mp3_file, "-acodec", "pcm_s16le", "-ar", "44100", wav_file]
    try:
        subprocess.run(command, check=True)
        print("Conversion successful.")
    except Exception as e:
        print("Error converting MP3 to WAV:", e)


# Call the function to convert MP3 to WAV
convert_mp3_to_wav("./TUMHE_DEKHTI_HOON_by_Pranita_Deshpande.mp3", "./TUMHE_DEKHTI_HOON_by_Pranita_Deshpande.wav")
