# YouTube Audio Downloader

This Python script allows you to download the audio from a YouTube video in MP3 format using the `yt_dlp` library. It fetches the best available audio stream and converts it to MP3 at 192 kbps quality.

## Features

- Downloads best audio stream from YouTube
- Converts to MP3 format using FFmpeg
- Saves the file with the video title as filename
- Simple terminal input: just enter the video ID

## Requirements

- Python 3.7 or newer
- `yt_dlp` Python package
- `ffmpeg` installed and accessible via system PATH

## Installation

1. **Clone or download this repository**  
   Or copy the script into your own project.

2. **Install Python dependencies**

```bash
pip install yt-dlp
```

3. **Install FFmpeg**

FFmpeg is required for audio conversion. You can install it via:

### macOS (Homebrew)

```bash
brew install ffmpeg
```

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows

- Download from: https://ffmpeg.org/download.html
- Add the FFmpeg `bin` directory to your system's PATH

## Usage

Run the script from the command line:

```bash
python downloader.py
```

You'll be prompted to enter a **YouTube video ID** (the part after `v=` in a YouTube URL).

Example:

If the URL is:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Then the video ID is:
```
dQw4w9WgXcQ
```

The script will download the audio and save it as:

```
Rick Astley - Never Gonna Give You Up.mp3
```

## Example Output

```bash
Enter YouTube video ID: dQw4w9WgXcQ
[youtube] dQw4w9WgXcQ: Downloading webpage
[download] Rick Astley - Never Gonna Give You Up.webm has already been downloaded
[ExtractAudio] Destination: Rick Astley - Never Gonna Give You Up.mp3
Conversion complete.
```

## License

This script is provided as-is for personal and educational use.