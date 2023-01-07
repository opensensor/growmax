import random
import time
from machine import Pin

from growmax import ntpclient
from growmax.moisture import Moisture
from growmax.pump import Pump
from growmax.utils.configs import get_moisture_threshold_for_position

# User's config file
import config


# Global variables
wlan = None

# set the random seed, so messages are randomized
random.seed()

def ensure_wifi_connected():
    # check if the Wi-Fi interface is connected
    if not config.WIFI_ENABLED:
        print("WIFI not enabled; change your config if you want wifi capabilities enabled.")
        return
    print("ensure_wifi_connected")
    import network
    global wlan
    if wlan is None:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.disconnect()
    if not wlan.isconnected():
        print(f"Connecting to Wi-Fi SSID: {config.WIFI_SSID}")
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

        # connect to the Wi-Fi network:
        while not wlan.isconnected():
            time.sleep(0.5)

        # sync current time via NTP
        ntpclient.settime()
        print(f"Connected to Wi-Fi SSID: {config.WIFI_SSID}")
        time.sleep(0.5)
    
def statistically_has_water(water_sensor):
    for x in range(0, 3):
        water_in_bucket = not water_sensor.value()
        if not water_in_bucket:
            return False
        time.sleep(0.5)
    return True
        
    
def main():
    water_sensor = None
    if config.WATER_SENSOR_LOW_ENABLED:
        water_sensor = Pin(config.WATER_SENSOR_LOW, Pin.IN, Pin.PULL_DOWN)

    soil_sensors = [Moisture(channel=1), Moisture(channel=2), Moisture(channel=3), Moisture(channel=4),
                    Moisture(channel=5), Moisture(channel=6), Moisture(channel=7), Moisture(channel=8)]
    pumps = [Pump(channel=1), Pump(channel=2), Pump(channel=3), Pump(channel=4),
             Pump(channel=5), Pump(channel=6), Pump(channel=7), Pump(channel=8)]


    time.sleep(0.1)
    while True:
        try:
            ensure_wifi_connected()
        except Exception:
            # Potentially no wi-fi
            pass

        soil_moistures = []
        for position, soil_sensor in enumerate(soil_sensors):
            try:
                soil_moisture = soil_sensor.moisture
                soil_moistures.append(soil_moisture)
                has_water = water_sensor and statistically_has_water(water_sensor)
                print(f"Position {position } reservoir has water {has_water} and moisture value {soil_moisture}")
                if has_water and soil_moisture >= get_moisture_threshold_for_position(position):
                    print(f"position: {position}")
                    pumps[position].dose(1, 30.0)
                    time.sleep(1)
            except Exception as e:
                print(f"Exception: {e}")

        print(f"Completed iteration; soil_moistures = {soil_moistures}")
