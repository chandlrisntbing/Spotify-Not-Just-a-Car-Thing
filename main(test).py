from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep

# I2C setup
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# LCD settings
I2C_ADDR = 0x27
ROWS = 2
COLS = 16

# Create LCD object
lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)

# Wait a moment
sleep(1)

# Clear screen
lcd.clear()

# Display text
lcd.putstr(":D")

