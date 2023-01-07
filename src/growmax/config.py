# Wi-Fi SSID and password
WIFI_ENABLED = False
WIFI_SSID = "SSID"
WIFI_PASSWORD = ""


# Threshold value for moisture sensor (range 0-28)
# Note: you may set value per plant by assigning an array length 8, Ex: [7, 7, 10, 8, 9, 12, 13, 10]
SOIL_WET_THRESHOLD = 10

# Water Sensor Pins
# (GP21 and GP22 ports have voltage dividers 4V -> ~3.3V to pair with Optomax Digital Liquid Level Sensors)
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 21
WATER_SENSOR_HIGH_ENABLED = False  # Not yet implemented
WATER_SENSOR_HIGH = 22  # Not yet implemented