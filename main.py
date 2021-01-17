import machine
import utime
import ujson
import network
import secrets
import max7219  # , httpclient
import SSD1306
from machine import Pin, SPI, ADC, I2C
from time import sleep

# ESP32 Pin assignment
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Welcome', 0, 0)
oled.text('Starting up.....', 0, 20)
oled.text('https://c-j.tech', 0, 30)
oled.show()

utime.sleep_ms(1000)
oled.fill(0)
utime.sleep_ms(1000)

oled.text("connecting to", 0, 20)
oled.text("wifi.........", 0, 40)
oled.show()


# print(secrets.WIFI_SSID)
# print(secrets.WIFI_PASSWORD)
# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.isconnected()
# station.ifconfig()
# oled.pixel(0, 0, 0)
# station.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
# oled.show()
# if not station.isconnected():
#     oled.fill(0)
#     oled.text("connecting...", 0, 0)


#     oled.fill(0)
#     oled.text("Connected:", 0, 0)
#     oled.text(station.ifconfig()[2], 0, 10)
#     oled.show()

def do_connect():
    oled.fill(0)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        oled.text('connecting to network...', 0, 10)
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    
    oled.fill(0)
    oled.text('network config:', 0, 10)
    oled.text(wlan.ifconfig()[0], 0, 20)
    oled.show()


def setup_screen():
    spi = SPI(1, baudrate=10000000, polarity=1,
              phase=0, sck=Pin(4), mosi=Pin(2))
    screen = max7219.Max7219(32, 16, spi, Pin(5))
    screen.brightness(0)
    return screen


do_connect()
screen = setup_screen()
screen.text("wait", 0, 0, 1)
screen.text("pls",  0, 8, 1)
screen.show()

# def multiline_marquee(screen, *lines, width=32):
#     start = width + 1
#     longest = len(max(lines, key=len))
#     extent = 0 - (longest * 8) - 32
#     for x in range(start, extent, -1):
#         screen.fill(0)
#         for y in range(0, len(lines)):
#             screen.text(lines[y], x, y * 8, 1)
#         screen.show()
#         utime.sleep_ms(30)

# multiline_marquee( screen,
#                    " Hey ,
#                    "There")
# screen.show()
