from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import sys
import uselect
import time


# LCD
i2c = I2C(
    0,
    sda=Pin(0),
    scl=Pin(1),
    freq=400000
)

lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.clear()
lcd.putstr("Waiting...")

# BUTTON SETUP

play = Pin(2, Pin.IN, Pin.PULL_UP)
pause = Pin(3, Pin.IN, Pin.PULL_UP)
next_song = Pin(4, Pin.IN, Pin.PULL_UP)

# SERIAL SETUP

poll = uselect.poll()
poll.register(sys.stdin, uselect.POLLIN)


# LCD SCROLLING FUNCTION

def scroll_text(text, row, delay=0.3):

    if len(text) <= 16:
        lcd.move_to(0, row)
        lcd.putstr(text)
        return

    text = text + "    "

    for i in range(len(text) - 15):

        lcd.move_to(0, row)
        lcd.putstr(text[i:i+16])

        time.sleep(delay)

# MAIN LOOP

while True:

    # CHECK BUTTONS
  

    if not play.value():
        print("PLAY")
        time.sleep(0.3)

    if not pause.value():
        print("PAUSE")
        time.sleep(0.3)

    if not next_song.value():
        print("NEXT")
        time.sleep(0.3)

    # CHECK FOR MESSAGE FROM COMPUTER

    if poll.poll(10):

        message = sys.stdin.readline().strip()

        print("Received:", message)

        parts = message.split("|")

        if parts[0] == "SONG":

            song = parts[1]
            artist = parts[2]
            current_time = parts[3]
            total_time = parts[4]

            lcd.clear()

            scroll_text(song, 0)

            lcd.move_to(0, 1)
            lcd.putstr(current_time + "/" + total_time)


    time.sleep(0.05)
