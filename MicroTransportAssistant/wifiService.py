
import time
import sys
import network
from secret import WIFI_PASSWORD

def connect():
    
    wifi = network.WLAN(network.STA_IF)
    wifi.active(False)
    time.sleep(0.5)
    wifi.active(True)

    wifi.connect('FBI Surveillance Van', WIFI_PASSWORD)

    for i in range(1, 5):
        time.sleep(2)
        if wifi.isconnected():
            print(wifi.ifconfig())
            break
        else:
            print(f"unable to connect trying again {5 - i}")

    if wifi.isconnected():
        print('Wifi connection success')
    else:
        print('Failed to connect to Wifi\nExiting script')
        sys.exit(-1)
