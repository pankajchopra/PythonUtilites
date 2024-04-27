from pytube import YouTube
import youtube_dl
from moviepy.editor import VideoFileClip
import os


def capture_youtube_audio(_url, _output_path):
    try:
        yt = YouTube(_url)
        stream = yt.streams.filter(only_audio=True).first()
        if stream:
            print("Downloading audio...")
            _filename = stream.download(output_path=output_path)
            print("Download complete!")
            return _filename
        else:
            print("No suitable stream found.")
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
    # Example usage
    url = "https://www.youtube.com/shorts/NQV0Mj_WYuE"
    output_path = ""
    old_filename = capture_youtube_audio(url, output_path)
    if old_filename and ("webm" in old_filename or "mp4" in old_filename):
        filename = old_filename.replace(" ", "_").replace(".mp4",".mp3")
        rename_file(old_filename, filename)
    else:
        print(f"{old_filename} downloaded")
