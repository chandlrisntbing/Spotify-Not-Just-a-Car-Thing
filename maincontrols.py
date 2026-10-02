import serial
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# SPOTIFY SETUP

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_NEW_CLIENT_SECRET"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

scope = "user-modify-playback-state user-read-playback-state"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope
    )
)

print("Spotify connected!")

# PICO SETUP

pico = serial.Serial(
    "COM11",
    115200,
    timeout=0.1
)

time.sleep(2)

print("Pico connected!")


# TIME FORMATTING FUNCTION

def format_time(milliseconds):

    total_seconds = milliseconds // 1000

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:02d}"

# SEND CURRENT SONG TO PICO

def send_song_to_pico(current):

    title = current["item"]["name"]

    artists = ", ".join(
        artist["name"]
        for artist in current["item"]["artists"]
    )

    progress_ms = current["progress_ms"]
    duration_ms = current["item"]["duration_ms"]

    current_time = format_time(progress_ms)
    total_time = format_time(duration_ms)

    message = (
        f"SONG|{title}|{artists}|"
        f"{current_time}|{total_time}\n"
    )

    pico.write(message.encode())

    print("Sending to Pico:", message.strip())

# MAIN LOOP
last_song_id = None
last_time = None

while True:
    # 1. CHECK FOR BUTTON COMMANDS FROM PICO

    if pico.in_waiting:

        command = pico.readline().decode().strip()

        print("Received from Pico:", command)

        if command == "PLAY":

            print("Playing...")
            sp.start_playback()

        elif command == "PAUSE":

            print("Pausing...")
            sp.pause_playback()

        elif command == "NEXT":

            print("Skipping...")
            sp.next_track()


    # 2. CHECK SPOTIFY

    current = sp.current_playback()

    if current and current["item"]:

        song_id = current["item"]["id"]

        progress_ms = current["progress_ms"]

        current_time = format_time(progress_ms)


        if song_id != last_song_id or current_time != last_time:

            send_song_to_pico(current)

            last_song_id = song_id
            last_time = current_time

    # 3. SMALL DELAY

    time.sleep(0.2)
