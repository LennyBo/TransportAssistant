
import time
import sys
import network
from secret import WIFI_PASSWORD, WIFI_SSID



def connect():
    sta_if = network.WLAN(network.STA_IF)  # Create a station interface object
    if not sta_if.isconnected():
        print('Connecting to Wi-Fi...')
        sta_if.active(True)  # Activate the station interface
        # Connect to the Wi-Fi network
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)

        while not sta_if.isconnected():
            print(f"Waiting...")
            time.sleep(1)

    print('Wi-Fi connection successful!')
    print(f"Network:{WIFI_SSID}")
    print(f"IP address: {sta_if.ifconfig()[0]}")
    time.sleep(5)