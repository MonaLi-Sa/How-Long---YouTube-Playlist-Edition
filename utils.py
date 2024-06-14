import requests
from bs4 import BeautifulSoup

def get_playlist_duration(playlist_url):
    try:
        response = requests.get(playlist_url)
        response.raise_for_status()  # Raise error for bad response status

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements that contain the video durations
        time_elements = soup.find_all('div', class_='badge-shape-wiz__text')

        # Print all the times found in the playlist
        print("Times found in the playlist:")
        for idx, time_element in enumerate(time_elements, 1):
            time_str = time_element.text.strip()
            print(f"{idx}. {time_str}")

        total_seconds = 0
        for time_element in time_elements:
            time_str = time_element.text.strip()
            if ':' in time_str:
                time_parts = time_str.split(':')
                if len(time_parts) == 2:  # MM:SS
                    minutes, seconds = map(int, time_parts)
                    total_seconds += minutes * 60 + seconds
                elif len(time_parts) == 3:  # HH:MM:SS
                    hours, minutes, seconds = map(int, time_parts)
                    total_seconds += hours * 3600 + minutes * 60 + seconds

        print(f"\nTotal Playlist Duration: {total_seconds} seconds")  # Debug output
        return total_seconds

    except requests.exceptions.RequestException as e:
        print(f"Error fetching playlist data: {e}")
        return None
    except Exception as ex:
        print(f"Error: {ex}")
        return None