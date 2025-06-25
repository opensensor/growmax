# 💪 High-Power Irrigation System

Using I2C relay boards to control large pumps, solenoid valves, and motorized ball valves for professional irrigation systems. This setup goes beyond the onboard pump limitations to handle serious watering needs.

## 📋 What You'll Need

### Hardware
- **GrowMax board** from [opensensor.io](https://opensensor.io)
- **Raspberry Pi Pico or Pico W** (WiFi recommended for monitoring)
- **I2C Relay Board** (4 or 8 channel)
- **High-power pumps** or **solenoid valves** (>200mA)
- **Motorized ball valves** (optional, for auto-refill)
- **External power supply** for pumps/valves (12V/24V typical)
- **Water level sensors** (critical for safety)
- **OLED Display** (SSD1327 or SH1107)
- **Display activation sensor** (PIR, capacitive touch, or button)
- Large water reservoir
- Professional tubing and fittings

### Safety Equipment
- **Flow meters** (recommended)
- **Pressure relief valves**
- **Manual shutoff valves**
- **Overflow protection**

## 🚨 Important Safety Warning

**⚠️ FLOODING RISK WARNING ⚠️**

When using motorized ball valves for auto-refill systems:
- **YOU ARE RESPONSIBLE** for any over-watering or flooding
- **OpenSensor.io is NOT responsible** for water damage
- **Always use multiple safety measures** (flow meters, timers, overflow protection)
- **Test thoroughly** before leaving unattended
- **Consider insurance implications** of automated water systems

## 🔧 Complete Configuration

Create this `config.py` file on your device:

```python
import machine

# Hardware Configuration
GROWMAX_MCU = "RP2040"

# Soil Moisture & Watering - Conservative thresholds for high-power system
SOIL_WET_THRESHOLD = [
    12,  # Position 1: Large vegetable plants
    15,  # Position 2: Fruit trees (drier)
    10,  # Position 3: Flower beds
    18,  # Position 4: Drought-tolerant plants
    12,  # Position 5: Herb garden
    14,  # Position 6: Shrubs
    16,  # Position 7: Cacti/succulents
    11   # Position 8: Lawn area
]

# IMPORTANT: Disable onboard pumps when using relay board
PUMP_WHEN_DRY = False         # Safety: only pump when water detected
PUMP_CYCLE_DURATION = 60      # Longer cycles for larger areas

# Water Level Safety - CRITICAL for high-power systems
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22         # Primary water level sensor
WATER_SENSOR_HIGH_ENABLED = False
WATER_SENSOR_HIGH = 21

# I2C Relay Board Configuration
RELAY_BOARD_ENABLED = True
RELAY_BOARD_I2C_CHANNEL = 0   # QWIIC_I2C0
RELAY_BOARD_NUM_RELAYS = 8    # 8-channel relay board
RELAY_BOARD_I2C_ADDRESS = 0x27

# Auto-Refill with Motorized Ball Valve (USE WITH EXTREME CAUTION)
AUTO_REFILL_RELAY_POSITION = 8    # Relay 8 controls motorized ball valve
AUTO_REFILL_DURATION = 30         # Conservative 30-second refill cycles

# Environmental Sensors
ADAFRUIT_SCD4X_ENABLED = False    # Focus on core irrigation functionality
ATLAS_PH_METER_ENABLED = False

# Display Configuration with Multiple Activation Options
DISPLAY = "SSD1327_I2C"           # 128x128 grayscale OLED
DISPLAY_I2C_CHANNEL = 1           # QWIIC_I2C1
DISPLAY_I2C_ADDRESS = None        # Auto-detect

# Display Activation Options (choose one):

# Option 1: PIR Motion Sensor
DISPLAY_SWITCH = 15               # GPIO pin for PIR sensor
DISPLAY_SWITCH_CLASS = "MotionSensor"
DISPLAY_SWITCH_DURATION_MS = 20000  # 20 seconds

# Option 2: Capacitive Touch Sensor (uncomment to use)
# DISPLAY_SWITCH = 16               # GPIO pin for touch sensor
# DISPLAY_SWITCH_CLASS = None       # Direct pin reading
# DISPLAY_SWITCH_DURATION_MS = 15000
# DISPLAY_SWITCH_PULL = None
# DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_RISING

# Option 3: Physical Button (uncomment to use)
# DISPLAY_SWITCH = 17               # GPIO pin for button
# DISPLAY_SWITCH_CLASS = None       # Direct pin reading
# DISPLAY_SWITCH_DURATION_MS = 10000
# DISPLAY_SWITCH_PULL = machine.Pin.PULL_UP
# DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING

DISPLAY_SWITCH_PULL = None
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING

# WiFi Configuration (recommended for monitoring)
WIFI_ENABLED = True
WIFI_SSID = "YourIrrigationNetwork"
WIFI_PASSWORD = "YourPassword"

# Cloud Integration for Remote Monitoring
OPEN_SENSOR_COLLECT_DATA = True
OPEN_SENSOR_API_KEY = "your-api-key"
DEVICE_NAME = "High-Power-Irrigation"
OPEN_SENSOR_RETRIEVE_COMMANDS = False  # Set True for remote control
```

## 🔌 Relay Board Wiring

### Relay Assignments
```python
# Suggested relay assignments:
# Relay 1: Zone 1 irrigation (vegetable garden)
# Relay 2: Zone 2 irrigation (fruit trees)
# Relay 3: Zone 3 irrigation (flower beds)
# Relay 4: Zone 4 irrigation (drought-tolerant area)
# Relay 5: Zone 5 irrigation (herb garden)
# Relay 6: Zone 6 irrigation (shrubs)
# Relay 7: Zone 7 irrigation (specialty plants)
# Relay 8: Auto-refill motorized ball valve
```

### Power Supply Considerations
- **Relay Logic**: 3.3V from GrowMax board (via I2C)
- **Relay Coils**: May need 5V external supply
- **Controlled Equipment**: 12V/24V separate supply
- **Isolation**: Relays provide electrical isolation for safety

## 🌱 Hardware Setup

### 1. Relay Board Connection
1. **Connect I2C**: Use QWIIC connector to relay board
2. **Power relay board**: May need external 5V supply
3. **Set I2C address**: Check jumpers/switches on relay board

### 2. High-Power Equipment
1. **Solenoid Valves**: Connect to relay NO (Normally Open) contacts
2. **Motorized Ball Valve**: Connect to dedicated relay (Relay 8)
3. **Power Supplies**: Separate 12V/24V supply for valves
4. **Fusing**: Add appropriate fuses for each circuit

### 3. Display Setup
Choose your preferred activation method:

#### PIR Motion Sensor
- **Connection**: GPIO 15, 3.3V, GND
- **Placement**: Near display for easy activation
- **Sensitivity**: Adjust potentiometer as needed

#### Capacitive Touch Sensor
- **Connection**: GPIO 16, 3.3V, GND
- **Mounting**: Behind non-conductive surface
- **Sensitivity**: Adjustable via onboard controls

#### Physical Button
- **Connection**: GPIO 17, GND (with internal pull-up)
- **Type**: Momentary push button
- **Mounting**: Weatherproof enclosure recommended

### 4. Safety Systems
1. **Water Level Sensors**: Multiple sensors recommended
2. **Flow Meters**: Monitor actual water usage
3. **Manual Overrides**: Physical shutoff valves
4. **Overflow Protection**: Drainage and alarms

## 💧 Auto-Refill System Setup

### Motorized Ball Valve Configuration
```python
# Auto-refill settings (USE WITH CAUTION)
AUTO_REFILL_RELAY_POSITION = 8    # Dedicated relay for ball valve
AUTO_REFILL_DURATION = 30         # Conservative duration

# Safety considerations:
# - Start with very short durations (10-15 seconds)
# - Monitor first several refill cycles
# - Install overflow protection
# - Consider flow meters for monitoring
# - Have manual shutoff readily accessible
```

### Safety Recommendations
1. **Start Conservative**: 10-15 second refill cycles initially
2. **Monitor Closely**: Watch first 10+ refill cycles
3. **Install Overflow**: Drainage and alarm systems
4. **Flow Monitoring**: Track actual water usage
5. **Manual Backup**: Always have manual shutoff available
6. **Insurance**: Check coverage for automated water systems

## 🖥️ Display Activation Options

### PIR Motion Sensor (Default)
```python
DISPLAY_SWITCH = 15
DISPLAY_SWITCH_CLASS = "MotionSensor"
DISPLAY_SWITCH_DURATION_MS = 20000  # 20 seconds
```
**Best for**: Outdoor installations, hands-free operation

### Capacitive Touch Sensor
```python
DISPLAY_SWITCH = 16
DISPLAY_SWITCH_CLASS = None
DISPLAY_SWITCH_DURATION_MS = 15000
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_RISING
```
**Best for**: Clean installations, weather protection

### Physical Button
```python
DISPLAY_SWITCH = 17
DISPLAY_SWITCH_CLASS = None
DISPLAY_SWITCH_PULL = machine.Pin.PULL_UP
DISPLAY_SWITCH_TRIGGER = machine.Pin.IRQ_FALLING
```
**Best for**: Reliable operation, simple interface

## 📊 System Monitoring

### Real-Time Display
The OLED shows:
1. **Zone Status**: Which irrigation zones are active
2. **Moisture Levels**: All 8 sensor readings
3. **Relay Status**: Which relays are currently on
4. **Water Level**: Reservoir status
5. **Auto-Refill**: Last refill time and duration

### Cloud Monitoring
Track via opensensor.io:
- **Water usage** per zone
- **Irrigation frequency** and duration
- **System uptime** and reliability
- **Auto-refill activity** and volumes

## 🔧 Testing and Commissioning

### Initial Testing (No Water)
1. **Test relay activation**: Verify each relay switches
2. **Check display**: Ensure activation methods work
3. **Verify I2C communication**: All devices respond
4. **Test safety systems**: Water level sensors, overrides

### Water System Testing
1. **Manual valve testing**: Operate each zone manually
2. **Short cycle testing**: 5-10 second irrigation cycles
3. **Auto-refill testing**: Very short refill cycles (5 seconds)
4. **Monitor for leaks**: Check all connections

### Full System Commissioning
1. **Gradual duration increase**: Slowly increase cycle times
2. **Monitor plant response**: Adjust thresholds as needed
3. **Optimize scheduling**: Based on plant and weather data
4. **Document settings**: Record working configurations

## 🚨 Safety Protocols

### Daily Checks
- **Visual inspection** of all connections
- **Water level verification**
- **Check for leaks** or unusual operation

### Weekly Maintenance
- **Clean sensors** and connections
- **Test manual overrides**
- **Review usage data** for anomalies

### Emergency Procedures
1. **Water leak detected**: Immediate manual shutoff
2. **System malfunction**: Disconnect power, manual mode
3. **Sensor failure**: Switch to manual operation
4. **Power outage**: Verify system state on restoration

## 📈 Optimization Tips

### Zone Management
- **Group similar plants** in same zones
- **Adjust timing** based on sun exposure
- **Consider soil types** when setting thresholds

### Water Conservation
- **Monitor usage patterns** via cloud data
- **Adjust for weather** conditions
- **Use moisture data** to optimize frequency

### System Reliability
- **Redundant sensors** for critical measurements
- **Regular maintenance** schedules
- **Backup power** for critical systems

## 🔧 Troubleshooting

### Relay Issues
- **No relay activation**: Check I2C connections, power supply
- **Intermittent operation**: Verify relay board power requirements
- **Wrong relay activating**: Check address settings, wiring

### High-Power Equipment
- **Valves not opening**: Check power supply, relay contacts
- **Partial operation**: Verify voltage requirements
- **Overheating**: Check current ratings, add cooling

### Auto-Refill Problems
- **Continuous refill**: Check water level sensor, duration settings
- **No refill**: Verify relay operation, valve power
- **Overflow**: Reduce duration, check overflow protection

## 📚 Related Examples

- **[Greenhouse Monitoring](greenhouse-monitoring.md)** - Add environmental sensors
- **[Smart Indoor Garden](smart-indoor-garden.md)** - Simpler WiFi setup
- **[Single Plant Setup](single-plant.md)** - Start with basics

---

**⚠️ IMPORTANT DISCLAIMER ⚠️**

**High-power irrigation systems can cause significant water damage if not properly installed and monitored. Users are solely responsible for:**
- **Proper installation** and safety measures
- **Adequate overflow protection** and drainage
- **Regular monitoring** and maintenance
- **Any water damage** or flooding that may occur

**OpenSensor.io provides the tools but assumes no responsibility for water damage, flooding, or other consequences of automated irrigation systems.**

---

**You now have a professional-grade irrigation system! 💪💧**

*Monitor closely, start conservatively, and always prioritize safety over convenience.*
