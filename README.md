This is a hot mess of code samples I've pulled from various trial and error, but thus far, with lots of searching and code samples from various sources (too many to mention), I've got something somewhat working with an ESP32 microcontroller running MicroPython, with both 2 4x8x8 MAX7219 LED matrixes in a top/bottom config to give a total of a 32 x 16 LED matrix.

I've also hooked up a OLED display to display some text for when the chip is booting, a splash screen/status of sorts until it connects to the WIFI, then is displays the IP address.

The following is my pin out for both

## LED Matrix

|ESP32 Board Pin|MAX7219 Pin|
|-|-|
|V5|VCC|
|GND|GND|
|G2|DIN|
|G5|CS|
|G4|CLK|

## OLED

|ESP32 Board Pin|MAX7219 Pin|
|-|-|
|3.3|VCC|
|GND|GND|
|G22|SCL|
|G21|SDA|

I hope to provide a Fritzing or other diagram at a later date!

I also have a secrets.py file, the contents of which are simply similar to the following

```python
WIFI_SSID='YourNetworkName'
WIFI_PASSWORD='YourNetworkPassword'

AN_API__CLIENT_ID='athingymebob'
AN_API_CLIENT_SECRET='blahblahblah'
```

![image](https://user-images.githubusercontent.com/3969086/104858972-c2f83400-591a-11eb-9a6a-741db2d6b1fc.png)

![image](https://user-images.githubusercontent.com/3969086/104858978-d73c3100-591a-11eb-9880-28bbc5aa1e5e.png)

![image](https://user-images.githubusercontent.com/3969086/104859003-defbd580-591a-11eb-8165-9eb91cfc24e6.png)

![image](https://user-images.githubusercontent.com/3969086/104859251-d35cde80-591b-11eb-98e7-0176a2506623.png)

![image](https://user-images.githubusercontent.com/3969086/104859254-da83ec80-591b-11eb-8692-93bf3ac53a35.png)

![image](https://user-images.githubusercontent.com/3969086/104859258-e1aafa80-591b-11eb-9a2a-053edda70e76.png)

