from utils import get_playlist_duration

if __name__ == "__main__":
    playlist_url = input("Enter playlist URL: ")
    duration_seconds = get_playlist_duration(playlist_url)
    if duration_seconds is not None:
        print(f"Total Playlist Duration: {duration_seconds} seconds")
