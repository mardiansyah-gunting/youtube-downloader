# pip install yt-dlp

import yt_dlp

def download_youtube_video(url):
    # Konfigurasi opsi unduhan
    ydl_opts = {
        'format': 'best', # Mengunduh gabungan video dan audio kualitas terbaik
        'outtmpl': '%(title)s.%(ext)s', # Menyimpan file dengan nama judul asli video
    }

    try:
        print(f"Mengambil informasi dan mulai mengunduh dari: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nUnduhan berhasil diselesaikan!")
    except Exception as e:
        print(f"\nTerjadi kesalahan saat mengunduh: {e}")

# youtube link
url_video = 'https://youtu.be/hyGqAmfl0n8?si=iUumy4VDofmsZ2_Z' 

if __name__ == "__main__":
    download_youtube_video(url_video)