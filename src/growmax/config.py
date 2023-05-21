import machine

# Support for RP2040 enabled by default (regardless of value)
# Also supported:  ESP32S3_BPI
GROWMAX_MCU = "RP2040"

# Threshold value for moisture sensor (range 0-28)
# Note: you may set value per plant by assigning an array length 8, Ex: [7, 7, 10, 8, 9, 12, 13, 10]
SOIL_WET_THRESHOLD = 10

# Water Sensor Pins
# (GP21 and GP22 ports have voltage dividers 4V -> ~3.3V to pair with Optomax Digital Liquid Level Sensors)
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22
WATER_SENSOR_HIGH_ENABLED = False  # Not yet implemented
WATER_SENSOR_HIGH = 21  # Not yet implemented

# Pump settings
PUMP_WHEN_DRY = False
PUMP_CYCLE_DURATION = 30  # seconds -- avoid long pump times as it does not check if reservoir is low while pumping!


# Auxiliary Sensors settings
ADAFRUIT_SCD4X_ENABLED = False
ADAFRUIT_SCD4X_I2C_CHANNEL = 0  # 0 for QWIIC_I2C0 or 1 for QWIIC_I2C1

# Atlas Scientific pH sensors
ATLAS_PH_METER_ENABLED = False
ATLAS_PH_I2C_CHANNEL = 0
ATLAS_PH_METER_ADDRESS = None

# I2C Displays
DISPLAY = None   # To enable a display, define an import from growmax.displays, Ex: "SSD1327_I2C", "SH1107_I2C"
DISPLAY_I2C_CHANNEL = 0  # 0 for QWIIC_I2C0 or 1 for QWIIC_I2C1
DISPLAY_I2C_ADDRESS = None  # The address of the display
DISPLAY_SWITCH = None  # Set GPIO Pin of the input switch or None to disable
DISPLAY_SWITCH_CLASS = None  # When set to None, Pin is used directly with interrupt.  Also available: "MotionSensor"
DISPLAY_SWITCH_DURATION_MS = 10000  # When using MotionSensor, this sets how long to turn on display for in ms
DISPLAY_SWITCH_PULL = None  # When using pin directly: Set to be None, machine.Pin.PULL_UP or machine.Pin.PULL_DOWN
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING

# Wi-Fi SSID and password
WIFI_ENABLED = False
WIFI_SSID = "SSID"
WIFI_PASSWORD = ""

# Data collection w/ api.opensensor.io (early alpha testing)
OPEN_SENSOR_COLLECT_DATA = False
OPEN_SENSOR_API_KEY = None  # Register your device for a key at https://opensensor.io/members/profile
DEVICE_NAME = ""
OPEN_SENSOR_RETRIEVE_COMMANDS = False  # Experimental feature to retrieve commands from the cloud
