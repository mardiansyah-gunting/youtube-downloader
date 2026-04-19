# pip install yt-dlp

import yt_dlp

def download_youtube_video(url):
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        print(f"Download from {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nSucces!")
    except Exception as e:
        print(f"\nError {e}")

# youtube link
url_video = 'https://youtu.be/hyGqAmfl0n8?si=iUumy4VDofmsZ2_Z' 

if __name__ == "__main__":
    download_youtube_video(url_video)