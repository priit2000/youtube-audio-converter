import yt_dlp

def download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_id = input("Enter YouTube video ID: ")
    download_audio(f"https://www.youtube.com/watch?v={video_id}")
    print("Conversion complete.")