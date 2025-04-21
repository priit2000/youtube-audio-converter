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
    user_input = input("Enter YouTube video ID or URL: ")
    if not user_input.startswith(("http://", "https://")):
        video_url = f"https://www.youtube.com/watch?v={user_input}"
    else:
        video_url = user_input
    download_audio(video_url)
    print("Conversion ready.")
