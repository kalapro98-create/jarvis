import yt_dlp
import subprocess
music_process = None
def play_youtube_audio(query):
    global music_process
    if query == "":
        print("Music name is empty")
        return False
    stop_music()
    ydl_opts = {
        "format": "bestaudio/best","quiet": True,"noplaylist": True,"default_search": "ytsearch1"}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                entry = info["entries"][0]
            else:
                entry = info
            audio_url = entry["url"]
            title = entry.get("title", "music")
            print("Playing:", title)
            music_process = subprocess.Popen(["ffplay","-nodisp","-loglevel","quiet",audio_url])
        return True
    except Exception as e:
        print("Music error:", e)
        return False
def stop_music():
    global music_process
    if music_process is not None:
        music_process.terminate()
        music_process = None
        print("Music stopped")
        return True
    return False
def is_music_playing():
    global music_process
    if music_process is None:
        return False
    if music_process.poll() is None:
        return True
    music_process = None
    return False