# from machine import I2C, Pin
# from pico_i2c_lcd import I2cLcd
# from time import sleep

# # I2C setup
# i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# # LCD settings
# I2C_ADDR = 0x27
# ROWS = 2
# COLS = 16

# # Create LCD object
# lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)

# # Wait a moment
# sleep(1)

# # Clear screen
# lcd.clear()

# # Display text
# lcd.putstr(":D")

import network
import time
import urequests
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd

# Wi-Fi credentials
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASS = "YOUR_WIFI_PASSWORD"

# Local server or proxy endpoint providing JSON: {"song": "Track Name", "left": "2:45"}
# (Building a tiny Flask/FastAPI script on your PC running Spotipy is recommended to feed this endpoint)
DATA_URL = "http://192.168.1"

# Initialize I2C and LCD (16 columns, 2 rows)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    lcd.putstr("Connecting WiFi")
    while not wlan.isconnected():
        time.sleep(1)
    lcd.clear()
    lcd.putstr("Connected!")
    time.sleep(1)
    lcd.clear()

def update_display():
    try:
        response = urequests.get(DATA_URL)
        data = response.json()
        response.close()
        
        song = data.get("song", "No Music")[:16]
        left_time = data.get("left", "--:--")[:16]
        
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(song)       # Line 1: Track Name
        lcd.move_to(0, 1)
        lcd.putstr(left_time)  # Line 2: MM:SS left
    except Exception as e:
        lcd.clear()
        lcd.putstr("Fetch Error")

connect_wifi()

while True:
    update_display()
    time.sleep(2)  # Refresh every 2 seconds
