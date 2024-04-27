from pytube import YouTube
import os
import subprocess
from moviepy.editor import VideoFileClip


def convert_mp3_to_wav(mp3_file, wav_file):
    command = ["ffmpeg", "-i", mp3_file, "-acodec", "pcm_s16le", "-ar", "44100", wav_file]
    try:
        subprocess.run(command, check=True)
        print("Conversion successful.")

    except Exception as e:
        print("Error converting MP3 to WAV:", e)


def download_youtube_section(video_url, start_time, end_time, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        output_file = stream.download(output_path=output_path)

        # Rename the downloaded file
        # temp_file = f"{output_path}/temp.mp4"
        # output_file = f"{output_path}/output.mp4"
        # os.rename(temp_file, output_file)

        mp4output = output_file.replace(" ", "_")
        rename_file(output_file, mp4output)
        filename = mp4output.removesuffix(".mp4")

        # Trim the video using ffmpeg
        subprocess.run(['ffmpeg', '-i', mp4output, '-ss', start_time, '-to', end_time, '-c', 'copy', f"{filename}_trimmed.mp4"], check=True)
        print("Video downloaded and trimmed successfully.")
        if filename:
            os.remove(mp4output)
            print(f"File '{mp4output}' deleted successfully.")
        return filename
    except Exception as e:
        print("Error:", e)


def extract_audio(input_file, output_file):
    try:
        video = VideoFileClip(input_file)
        audio = video.audio
        if audio:
            audio.write_audiofile(output_file)
            print("Extraction of audio to MP3 complete!")
            return output_file
        else:
            print("The video does not contain any audio.")
    except Exception as e:
        print("Error:", e)


def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except Exception as e:
        if "file already exists" in str(e):
            os.rename(old_name, new_name + "_1")
        else:
            print("Error:", e)


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=ZK481WtfyL0"  # Replace with your YouTube video URL
    start_time = "00:13:02"  # Specify the start time (format: HH:MM:SS)
    end_time = "00:15:23"  # Specify the end time (format: HH:MM:SS)
    output_path = ""  # Specify the output directory

    output_mp4 = download_youtube_section(video_url, start_time, end_time, output_path)
    print(output_mp4)
    onlyFilename = output_mp4.removesuffix(".mp4")
    mp3Filename = onlyFilename + ".mp3"
    wavfileName = onlyFilename + ".wav"

    mp4Filename = onlyFilename + "_trimmed.mp4"
    print(mp4Filename)
    extract_audio(mp4Filename, mp3Filename)
    convert_mp3_to_wav(mp3Filename, wavfileName)
