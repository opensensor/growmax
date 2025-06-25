# 🏭 Greenhouse Monitoring Station

Complete environmental monitoring system with CO2, pH, temperature, humidity, and visual display. Perfect for serious gardeners and greenhouse operations.

## 📋 What You'll Need

### Hardware
- GrowMax board from [opensensor.io](https://opensensor.io)
- **Raspberry Pi Pico W** (WiFi required for cloud logging)
- 8x small water pumps (5V, <200mA each)
- 1x Optomax water level sensor
- **Adafruit SCD4X CO2 sensor** (SCD40 or SCD41)
- **Atlas Scientific pH probe and EZO-pH circuit**
- **OLED Display** (SSD1327 128x128 or SH1107 128x64)
- **PIR Motion Sensor** for display activation
- Water reservoir (large capacity recommended)
- Tubing and fittings
- 5V power supply (higher capacity for multiple pumps)

### Software Requirements
- OpenSensor.io account for cloud data logging
- WiFi network (2.4GHz)

## 🔧 Complete Configuration

Create this `config.py` file on your device:

```python
import machine

# Hardware Configuration
GROWMAX_MCU = "RP2040"

# Soil Moisture & Watering - Individual thresholds for different plant types
SOIL_WET_THRESHOLD = [
    8,   # Position 1: Leafy greens (lettuce, spinach)
    10,  # Position 2: Herbs (basil, parsley)
    12,  # Position 3: Tomatoes
    15,  # Position 4: Peppers (prefer drier)
    8,   # Position 5: Cucumbers (need moisture)
    10,  # Position 6: Herbs (oregano, thyme)
    12,  # Position 7: Eggplant
    14   # Position 8: Beans (moderate moisture)
]

PUMP_WHEN_DRY = False         # Safety: only pump when water detected
PUMP_CYCLE_DURATION = 25      # 25 seconds for greenhouse plants

# Water Level Safety
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22         # GPIO pin for water sensor
WATER_SENSOR_HIGH_ENABLED = False
WATER_SENSOR_HIGH = 21

# I2C Relay Board - Disabled for this example (using onboard pumps)
RELAY_BOARD_ENABLED = False
RELAY_BOARD_I2C_CHANNEL = 0
RELAY_BOARD_NUM_RELAYS = 4
RELAY_BOARD_I2C_ADDRESS = 0x27
AUTO_REFILL_RELAY_POSITION = None
AUTO_REFILL_DURATION = 45

# Environmental Sensors
ADAFRUIT_SCD4X_ENABLED = True
ADAFRUIT_SCD4X_I2C_CHANNEL = 0  # QWIIC_I2C0

# Atlas Scientific pH Monitoring
ATLAS_PH_METER_ENABLED = True
ATLAS_PH_I2C_CHANNEL = 0
ATLAS_PH_METER_ADDRESS = None   # Auto-detect

# Display Configuration
DISPLAY = "SSD1327_I2C"         # 128x128 grayscale OLED
DISPLAY_I2C_CHANNEL = 1         # QWIIC_I2C1 (separate from sensors)
DISPLAY_I2C_ADDRESS = None      # Auto-detect
DISPLAY_SWITCH = 15             # GPIO pin for PIR motion sensor
DISPLAY_SWITCH_CLASS = "MotionSensor"
DISPLAY_SWITCH_DURATION_MS = 30000  # 30 seconds display timeout
DISPLAY_SWITCH_PULL = None
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING

# WiFi Configuration
WIFI_ENABLED = True
WIFI_SSID = "YourGreenhouseWiFi"
WIFI_PASSWORD = "YourWiFiPassword"

# OpenSensor.io Cloud Integration
OPEN_SENSOR_COLLECT_DATA = True
OPEN_SENSOR_API_KEY = "your-opensensor-api-key"  # Get from opensensor.io/members/profile
DEVICE_NAME = "Greenhouse-Monitor-01"
OPEN_SENSOR_RETRIEVE_COMMANDS = False  # Set to True for remote control
```

## 🌱 Setup Instructions

### 1. Hardware Assembly

#### I2C Sensor Connections (QWIIC_I2C0)
- **SCD4X CO2 Sensor**: Connect to I2C0 (SDA=GP4, SCL=GP5)
- **Atlas pH Circuit**: Connect to same I2C0 bus

#### Display Connection (QWIIC_I2C1)
- **OLED Display**: Connect to I2C1 (SDA=GP6, SCL=GP7)

#### Motion Sensor
- **PIR Sensor**: Connect to GPIO 15
- **Power**: 3.3V and GND
- **Output**: To GPIO 15

#### Plant Connections
1. **Install moisture sensors** in all 8 positions
2. **Connect pumps** to all 8 pump ports
3. **Set up tubing** from each pump to respective plants
4. **Place water level sensor** in large reservoir

### 2. Software Setup

1. **Install MicroPython firmware** on Pico W
2. **Install GrowMax library** via Thonny IDE
3. **Create OpenSensor.io account**:
   - Visit [opensensor.io/members/profile](https://opensensor.io/members/profile)
   - Get your API key
   - Update `OPEN_SENSOR_API_KEY` in config
4. **Copy configuration** to `config.py` on device
5. **Create main.py**:
   ```python
   from growmax.routine import main
   
   main()
   ```

### 3. Sensor Calibration

#### pH Probe Calibration
The Atlas Scientific pH probe requires calibration:

```python
# Run this calibration script once
from growmax.atlas_ph.calibration import calibrate_ph

# Follow the prompts to calibrate with pH 4.0, 7.0, and 10.0 solutions
calibrate_ph()
```

#### CO2 Sensor Setup
The SCD4X sensor auto-calibrates but needs 2-3 minutes to stabilize after power-on.

## 📊 What You'll Monitor

### Real-Time Display
The OLED display cycles through:
1. **Plant Status**: Moisture levels and pump activity
2. **Environmental Data**: CO2, temperature, humidity
3. **pH Readings**: Water/nutrient solution pH
4. **System Status**: WiFi, memory, uptime

### Cloud Data Logging
All data is automatically logged to OpenSensor.io:
- **Soil moisture** for all 8 positions
- **CO2 levels** (ppm)
- **Temperature and humidity**
- **pH readings**
- **Pump activity** and duration
- **Water level status**

### Data Analysis
Access your data at [opensensor.io](https://opensensor.io) to:
- **Track trends** over time
- **Identify optimal conditions** for each plant type
- **Set up alerts** for critical conditions
- **Export data** for further analysis

## 🎯 Understanding Your Greenhouse Data

### CO2 Levels (ppm)
- **400-600**: Outdoor ambient levels
- **600-1000**: Good for plant growth
- **1000-1500**: Optimal for many plants
- **1500+**: May need ventilation

### pH Levels
- **5.5-6.0**: Optimal for most vegetables
- **6.0-6.5**: Good for herbs and leafy greens
- **6.5-7.0**: Suitable for most plants
- **<5.5 or >7.5**: May need adjustment

### Temperature & Humidity
- **Temperature**: 65-75°F (18-24°C) optimal for most plants
- **Humidity**: 50-70% ideal for greenhouse conditions

## 🔧 Advanced Features

### Motion-Activated Display
The display only turns on when motion is detected, saving power:
- **PIR sensor** detects movement
- **Display activates** for 30 seconds
- **Automatic shutoff** when no motion

### Individual Plant Thresholds
Each plant position has its own moisture threshold:
```python
SOIL_WET_THRESHOLD = [
    8,   # Position 1: Moisture-loving plants
    15,  # Position 2: Drought-tolerant plants
    # ... customize for your specific plants
]
```

### Remote Monitoring
With WiFi enabled, you can:
- **Monitor remotely** via opensensor.io dashboard
- **Receive alerts** for critical conditions
- **Control pumps remotely** (experimental feature)

## 📈 Optimization Tips

### Plant Placement Strategy
- **Position 1-4**: High-moisture plants (leafy greens, herbs)
- **Position 5-8**: Moderate to low-moisture plants (tomatoes, peppers)

### Watering Schedule Optimization
Monitor your data to optimize:
- **Pump duration** based on plant response
- **Moisture thresholds** for each plant type
- **Seasonal adjustments** as plants grow

### Environmental Control
Use the data to optimize:
- **Ventilation timing** based on CO2 levels
- **Heating/cooling** based on temperature trends
- **Humidity control** for optimal growing conditions

## 🚨 Alerts and Monitoring

### Critical Conditions to Watch
- **Low water level**: Immediate attention needed
- **Extreme pH**: May harm plants
- **High CO2**: Ventilation needed
- **Temperature extremes**: Climate control needed

### Setting Up Alerts
Configure alerts in your opensensor.io dashboard for:
- Water level below threshold
- pH outside optimal range
- CO2 levels too high
- Temperature outside comfort zone

## 🔧 Troubleshooting

### CO2 Sensor Issues
- **No readings**: Check I2C connections, wait for warm-up
- **Erratic readings**: Ensure good ventilation around sensor
- **Calibration**: Sensor auto-calibrates over time

### pH Sensor Issues
- **Unstable readings**: Recalibrate probe
- **No readings**: Check BNC connection, verify probe in solution
- **Drift**: Regular calibration needed (monthly)

### Display Issues
- **Blank display**: Check I2C connections and address
- **Motion not working**: Verify PIR sensor connections
- **Display stays on**: Check motion sensor sensitivity

### WiFi Connectivity
- **Connection fails**: Verify 2.4GHz network, check credentials
- **Intermittent connection**: Check signal strength, router settings
- **Data not uploading**: Verify API key, check internet connection

## 📊 Sample Output

When running, you'll see output like:
```
Position 1 reservoir has water True and moisture value 8/8
Position 2 reservoir has water True and moisture value 12/10
Position 2
Position 3 reservoir has water True and moisture value 15/12
Position 3
CO2: 850 ppm, Temp: 72.5°F, Humidity: 65%
pH: 6.2
Completed iteration; soil_moisture's = [8, 12, 15, 18, 7, 11, 14, 16]
```

## 🎉 Success Indicators

Your greenhouse monitoring system is working when:
- ✅ All 8 moisture sensors provide readings
- ✅ CO2, temperature, and humidity data appears
- ✅ pH readings are stable and reasonable
- ✅ Display shows data and responds to motion
- ✅ Data appears in opensensor.io dashboard
- ✅ Plants are watered automatically based on individual needs

## 🚀 Next Steps

### Expand Your System
- **Add relay board** for high-power equipment control
- **Install ventilation fans** controlled by CO2 levels
- **Add heating/cooling** based on temperature data
- **Implement nutrient dosing** based on pH readings

### Data Analysis
- **Track growth patterns** over time
- **Optimize watering schedules** based on plant response
- **Correlate environmental conditions** with plant health
- **Set up automated alerts** for critical conditions

## 📚 Related Examples

- **[High-Power Irrigation](high-power-irrigation.md)** - Add relay control for larger pumps
- **[Smart Indoor Garden](smart-indoor-garden.md)** - Simpler WiFi setup
- **[Single Plant Setup](single-plant.md)** - Start with basics

---

**Congratulations! You now have a professional-grade greenhouse monitoring system! 🏭🌱**

*Your greenhouse will automatically maintain optimal conditions for each plant while providing detailed environmental data for analysis and optimization.*
