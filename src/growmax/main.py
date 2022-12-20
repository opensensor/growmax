import network
import ntpclient
import random
import time

from machine import Pin

# Custom imports
import config
from moisture import Moisture
import pump

#
# Global variables
#
wlan = None
soil_is_dry = False


# set the random seed, so messages are randomized
random.seed()

water_sensor = None
if config.WATER_SENSOR_LOW_ENABLED:
    water_sensor = Pin(config.WATER_SENSOR_LOW, Pin.IN, Pin.PULL_DOWN)

soil_sensors = [Moisture(channel=1), Moisture(channel=2), Moisture(channel=3), Moisture(channel=4), Moisture(channel=5), Moisture(channel=6), Moisture(channel=7), Moisture(channel=8)]
pumps = [pump.Pump(channel=1), pump.Pump(channel=2), pump.Pump(channel=3), pump.Pump(channel=4), pump.Pump(channel=5), pump.Pump(channel=6), pump.Pump(channel=7), pump.Pump(channel=8)]

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect()
time.sleep(0.1)


def ensure_wifi_connected():
    # check if the Wi-Fi interface is connected
    print("ensure_wifi_connected")
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
        
    

while True:
    try:
        ensure_wifi_connected()
    except Exception:
        # Potentially no wi-fi
        pass

    soil_moisturues = []
    for position, soil_sensor in enumerate(soil_sensors):
        try:
            soil_moisture = soil_sensor.moisture
            soil_moisturues.append(soil_moisture)
            has_water = water_sensor and statistically_has_water(water_sensor)
            print(has_water)
            if soil_moisture >= config.SOIL_WET_THRESHOLD and has_water:
                print(f"position: {position}")
                # soil was NOT dry, but is dry now
                soil_is_dry = True
                pumps[position].dose(1, 30.0)
                time.sleep(1)
        except Exception as e:
            print(e)

    print(f"soil_moistures = {soil_moisturues}")
