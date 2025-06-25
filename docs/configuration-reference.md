# ⚙️ Configuration Reference

This guide covers all configuration options available in GrowMax. Copy the default config from `/lib/growmax/config.py` to your device root as `config.py` and customize as needed.

## 🎯 Quick Configuration

For most users, these are the essential settings to get started:

```python
# Basic moisture and pump settings
SOIL_WET_THRESHOLD = 10          # Lower = wetter soil (0-28)
PUMP_WHEN_DRY = False           # Safety: only pump when water detected
PUMP_CYCLE_DURATION = 30        # Pump duration in seconds

# Water level safety
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22           # GPIO pin for water sensor

# WiFi (optional)
WIFI_ENABLED = True
WIFI_SSID = "YourNetwork"
WIFI_PASSWORD = "YourPassword"
```

## 🖥️ Hardware Configuration

### Microcontroller Selection
```python
GROWMAX_MCU = "RP2040"  # Options: "RP2040", "ESP32S3_BPI"
```
- **RP2040**: Raspberry Pi Pico/Pico W (default)
- **ESP32S3_BPI**: BananaPi ESP32S3 boards

## 💧 Soil Moisture & Watering

### Moisture Thresholds
```python
# Single threshold for all plants
SOIL_WET_THRESHOLD = 10

# Individual thresholds per plant (positions 1-8)
SOIL_WET_THRESHOLD = [7, 7, 10, 8, 9, 12, 13, 10]
```

**Understanding Values:**
- **Range**: 0-28 (lower numbers = wetter soil)
- **Typical Values**:
  - `5-8`: Very wet (succulents, cacti)
  - `8-12`: Moderate moisture (most houseplants)
  - `12-18`: Drier soil (herbs, some vegetables)
  - `18+`: Very dry (drought-tolerant plants)

### Pump Control
```python
PUMP_WHEN_DRY = False           # Safety setting
PUMP_CYCLE_DURATION = 30        # Pump duration in seconds
```

**Safety Recommendations:**
- **Always keep `PUMP_WHEN_DRY = False`** unless you have a specific need
- **Start with shorter durations** (15-30 seconds) and adjust based on results
- **Monitor first few cycles** to ensure proper watering amounts

## 🚰 Water Level Monitoring

### Low Water Sensor
```python
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22           # GPIO pin (21 or 22 recommended)
```

### High Water Sensor (Future Feature)
```python
WATER_SENSOR_HIGH_ENABLED = False  # Not yet implemented
WATER_SENSOR_HIGH = 21             # Reserved for future use
```

**Hardware Notes:**
- **GPIO 21 & 22**: Have built-in voltage dividers (4V → 3.3V)
- **Optomax Sensors**: Designed specifically for these sensors
- **Safety**: Always enable low water sensor to prevent pump damage

## 🔌 I2C Relay Board Integration

### Basic Relay Setup
```python
RELAY_BOARD_ENABLED = True
RELAY_BOARD_I2C_CHANNEL = 0     # 0 for QWIIC_I2C0, 1 for QWIIC_I2C1
RELAY_BOARD_NUM_RELAYS = 4      # 4 or 8 relay board
RELAY_BOARD_I2C_ADDRESS = 0x27  # I2C address of relay board
```

### Auto-Refill System
```python
AUTO_REFILL_RELAY_POSITION = 1  # Relay position (1-8), None to disable
AUTO_REFILL_DURATION = 45       # Refill duration in seconds
```

**Use Cases:**
- **High-Power Pumps**: Control pumps >200mA safely
- **Solenoid Valves**: Control irrigation systems
- **Auto-Refill**: Automatically refill reservoir when low
- **Motorized Ball Valves**: For auto-refill from main water line
- **External Equipment**: Fans, lights, heaters

**⚠️ IMPORTANT SAFETY WARNING ⚠️**

When using motorized ball valves for auto-refill systems:
- **YOU ARE RESPONSIBLE** for any over-watering or flooding
- **OpenSensor.io is NOT responsible** for water damage
- **Always use multiple safety measures** (flow meters, timers, overflow protection)
- **Test thoroughly** before leaving unattended
- **Consider insurance implications** of automated water systems

## 📊 Environmental Sensors

### CO2 Monitoring (Adafruit SCD4X)
```python
ADAFRUIT_SCD4X_ENABLED = True
ADAFRUIT_SCD4X_I2C_CHANNEL = 0  # 0 for QWIIC_I2C0, 1 for QWIIC_I2C1
```

**Supported Sensors:**
- SCD40: ±40ppm accuracy
- SCD41: ±40ppm accuracy, extended range

### pH Monitoring (Atlas Scientific)
```python
ATLAS_PH_METER_ENABLED = True
ATLAS_PH_I2C_CHANNEL = 0
ATLAS_PH_METER_ADDRESS = None   # Auto-detect or specify address
```

**Features:**
- Professional-grade pH measurement
- Automatic temperature compensation
- Calibration support
- Data logging integration

## 🖥️ Display Configuration

### Display Selection
```python
DISPLAY = "SSD1327_I2C"         # Options: "SSD1327_I2C", "SH1107_I2C", None
DISPLAY_I2C_CHANNEL = 0         # I2C channel
DISPLAY_I2C_ADDRESS = None      # Auto-detect or specify
```

**Supported Displays:**
- **SSD1327**: 128x128 grayscale OLED
- **SH1107**: 128x64 monochrome OLED

### Display Activation Options

GrowMax supports multiple ways to activate the display:

#### PIR Motion Sensor (Default)
```python
DISPLAY_SWITCH = 15             # GPIO pin for PIR sensor
DISPLAY_SWITCH_CLASS = "MotionSensor"
DISPLAY_SWITCH_DURATION_MS = 10000     # Display on duration
DISPLAY_SWITCH_PULL = None
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING
```

#### Capacitive Touch Sensor
```python
DISPLAY_SWITCH = 16             # GPIO pin for touch sensor
DISPLAY_SWITCH_CLASS = None     # Direct pin reading
DISPLAY_SWITCH_DURATION_MS = 15000     # Display on duration
DISPLAY_SWITCH_PULL = None
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_RISING
```

#### Physical Button
```python
DISPLAY_SWITCH = 17             # GPIO pin for button
DISPLAY_SWITCH_CLASS = None     # Direct pin reading
DISPLAY_SWITCH_DURATION_MS = 10000     # Display on duration
DISPLAY_SWITCH_PULL = machine.Pin.PULL_UP  # Internal pull-up
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING
```

**Power Saving Benefits:**
- Display turns on only when activated
- Configurable timeout duration
- Reduces power consumption significantly
- Multiple activation methods for different use cases

## 🌐 WiFi & Cloud Integration

### WiFi Connection
```python
WIFI_ENABLED = True
WIFI_SSID = "YourNetworkName"
WIFI_PASSWORD = "YourPassword"
```

### OpenSensor.io Integration
```python
OPEN_SENSOR_COLLECT_DATA = True
OPEN_SENSOR_API_KEY = "your-api-key"    # Get from opensensor.io/members/profile
DEVICE_NAME = "GrowMax-Garden-01"       # Friendly device name
OPEN_SENSOR_RETRIEVE_COMMANDS = False   # Experimental remote control
```

**Cloud Features:**
- **Data Logging**: All sensor readings stored in cloud
- **Remote Monitoring**: View data from anywhere
- **Historical Analysis**: Track trends over time
- **Alerts**: Get notified of issues (future feature)

## 🔧 Advanced Configuration Examples

### Multi-Plant Garden Setup
```python
# Different thresholds for different plant types
SOIL_WET_THRESHOLD = [
    8,   # Position 1: Fern (likes moisture)
    12,  # Position 2: Pothos (moderate)
    6,   # Position 3: Peace Lily (very moist)
    15,  # Position 4: Snake Plant (dry)
    10,  # Position 5: Spider Plant (moderate)
    8,   # Position 6: Philodendron (moist)
    18,  # Position 7: Succulent (very dry)
    12   # Position 8: Rubber Plant (moderate)
]

# Shorter pump cycles for smaller plants
PUMP_CYCLE_DURATION = 20
```

### Greenhouse Monitoring Station
```python
# Enable all sensors
ADAFRUIT_SCD4X_ENABLED = True
ATLAS_PH_METER_ENABLED = True
DISPLAY = "SSD1327_I2C"

# Cloud logging for analysis
OPEN_SENSOR_COLLECT_DATA = True
WIFI_ENABLED = True

# Motion-activated display
DISPLAY_SWITCH = 15
DISPLAY_SWITCH_CLASS = "MotionSensor"
```

### High-Power Irrigation System
```python
# Use relay board for large pumps
RELAY_BOARD_ENABLED = True
RELAY_BOARD_NUM_RELAYS = 8

# Auto-refill from main water line
AUTO_REFILL_RELAY_POSITION = 8
AUTO_REFILL_DURATION = 60

# Conservative watering
PUMP_WHEN_DRY = False
PUMP_CYCLE_DURATION = 45
```

## 🚨 Safety Guidelines

### Critical Safety Settings
```python
# ALWAYS enable water level checking
WATER_SENSOR_LOW_ENABLED = True

# NEVER pump when reservoir is dry (unless you have unlimited water)
PUMP_WHEN_DRY = False

# Start with shorter pump cycles
PUMP_CYCLE_DURATION = 15  # Increase gradually as needed
```

### Power Considerations
- **Onboard Pumps**: Max 200mA each (Pico limitation)
- **Total Current**: Keep under 300mA total
- **High-Power Equipment**: Always use relay boards
- **Water Sensors**: Use GPIO 21/22 for proper voltage levels

## 🔍 Troubleshooting Configuration

### Common Issues

**Plants not watering:**
- Check `SOIL_WET_THRESHOLD` - may be too low
- Verify `WATER_SENSOR_LOW_ENABLED = True`
- Ensure water reservoir has water

**Pumps running too long:**
- Reduce `PUMP_CYCLE_DURATION`
- Check for pump blockages
- Verify soil sensor placement

**WiFi not connecting:**
- Double-check `WIFI_SSID` and `WIFI_PASSWORD`
- Ensure 2.4GHz network (not 5GHz)
- Check signal strength

**Display not working:**
- Verify `DISPLAY_I2C_ADDRESS` if specified
- Check I2C connections
- Try different `DISPLAY_I2C_CHANNEL`

### Testing Configuration
```python
# Test mode - disable pumping for safe testing
PUMP_WHEN_DRY = False
PUMP_CYCLE_DURATION = 5  # Very short for testing

# Enable verbose output
WIFI_ENABLED = False  # Disable to focus on core functionality
```

## 📝 Configuration Template

Here's a complete template with common settings:

```python
import machine

# Hardware Configuration
GROWMAX_MCU = "RP2040"

# Soil Moisture & Watering
SOIL_WET_THRESHOLD = 10
PUMP_WHEN_DRY = False
PUMP_CYCLE_DURATION = 30

# Water Level Safety
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22
WATER_SENSOR_HIGH_ENABLED = False
WATER_SENSOR_HIGH = 21

# I2C Relay Board (optional)
RELAY_BOARD_ENABLED = False
RELAY_BOARD_I2C_CHANNEL = 0
RELAY_BOARD_NUM_RELAYS = 4
RELAY_BOARD_I2C_ADDRESS = 0x27
AUTO_REFILL_RELAY_POSITION = None
AUTO_REFILL_DURATION = 45

# Environmental Sensors (optional)
ADAFRUIT_SCD4X_ENABLED = False
ADAFRUIT_SCD4X_I2C_CHANNEL = 0

ATLAS_PH_METER_ENABLED = False
ATLAS_PH_I2C_CHANNEL = 0
ATLAS_PH_METER_ADDRESS = None

# Display (optional)
DISPLAY = None
DISPLAY_I2C_CHANNEL = 0
DISPLAY_I2C_ADDRESS = None
DISPLAY_SWITCH = None
DISPLAY_SWITCH_CLASS = None
DISPLAY_SWITCH_DURATION_MS = 10000
DISPLAY_SWITCH_PULL = None
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING

# WiFi & Cloud (optional)
WIFI_ENABLED = False
WIFI_SSID = "YourNetwork"
WIFI_PASSWORD = "YourPassword"

OPEN_SENSOR_COLLECT_DATA = False
OPEN_SENSOR_API_KEY = None
DEVICE_NAME = "GrowMax-Device"
OPEN_SENSOR_RETRIEVE_COMMANDS = False
```

---

**Next Steps:**
- [🚀 Quick Start Guide](quick-start.md) - Get up and running
- [💡 Examples](examples/) - See real-world configurations
- [🔍 Troubleshooting](troubleshooting.md) - Solve common issues
