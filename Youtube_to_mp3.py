import yt_dlp
import os

run = True
URL = ""
name = ""

# New mp3s will be created on the Desktop by default
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Change to the location you have the ffmpeg bin folder
ffmpeg_path = os.path.join(os.path.expanduser("~"), "ffmpeg-2024-12-19-git-494c961379-essentials_build/bin")

while run:
    print("▶️YouTubeダウンローダー🎧")
    URL = input("URLを入力するか、Qで終了: ")
    if URL.lower() == "q":
        run = False
        break
    name = input("ファイル名（拡張子なし）を入力: ")
    opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(desktop_path, f'{name}.mp3'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'ffmpeg_location': ffmpeg_path,
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([URL])
    except Exception as e:
        print(f"エラー: {e}")
