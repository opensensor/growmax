# 🔧 Hardware Setup Guide

Complete assembly and connection instructions for your GrowMax plant watering system.

## 📋 Before You Start

### Required Tools
- Small screwdriver set
- Wire strippers (if making custom connections)
- Multimeter (for troubleshooting)
- Computer with USB port

### Safety Precautions
- **Disconnect power** before making connections
- **Check voltage levels** - use 5V for pumps, 3.3V for sensors
- **Avoid water near electronics** - keep connections dry
- **Test connections** before final assembly

## 🏗️ Board Assembly

### 1. GrowMax Board Setup
1. **Unpack your GrowMax board** from opensensor.io
2. **Inspect for damage** - check for bent pins or loose components
3. **Identify connection points**:
   - 8x pump ports (labeled P1-P8)
   - 8x moisture sensor ports (labeled M1-M8)
   - 2x water level sensor ports (GPIO 21, 22)
   - 2x QWIIC I2C connectors
   - Power input (5V USB)

### 2. Microcontroller Installation
1. **Choose your MCU**:
   - **Raspberry Pi Pico**: Basic functionality
   - **Raspberry Pi Pico W**: WiFi capabilities
   - **ESP32S3 BananaPi**: Advanced features (see [ESP32S3 guide](bpi_esp32s3.md))

2. **Install firmware** (see [Quick Start Guide](quick-start.md))

3. **Mount MCU on GrowMax board**:
   - Align pins carefully
   - Press firmly until seated
   - Ensure no bent pins

## 💧 Water System Setup

### Pump Installation
1. **Select appropriate pumps**:
   - **Voltage**: 5V DC only
   - **Current**: <200mA per pump
   - **Type**: Submersible or inline pumps work well

2. **Connect pumps to board**:
   - **Red wire**: Positive terminal
   - **Black wire**: Negative terminal
   - **Secure connections** to prevent loosening

3. **Test pump operation**:
   ```python
   from growmax.pump import Pump
   pump = Pump(channel=1)
   pump.dose(1, 5)  # Run pump 1 for 5 seconds
   ```

### Water Level Sensors
1. **Use Optomax sensors** (recommended):
   - Designed for GPIO 21/22 voltage levels
   - Built-in voltage dividers on board

2. **Connection**:
   - **GPIO 22**: Low water level sensor (primary)
   - **GPIO 21**: High water level sensor (future use)

3. **Placement**:
   - **Low sensor**: Near bottom of reservoir
   - **Secure mounting** to prevent movement
   - **Test in water** to verify operation

### Tubing and Water Flow
1. **Select tubing**:
   - **Size**: Match pump outlet (typically 4-6mm)
   - **Material**: Food-safe silicone or vinyl
   - **Length**: Minimize to reduce pump load

2. **Route tubing**:
   - **Avoid kinks** and sharp bends
   - **Secure with clips** to prevent movement
   - **Test water flow** before final installation

3. **Drip points**:
   - **Position near plant roots**
   - **Use drip stakes** for targeted watering
   - **Avoid leaves** to prevent fungal issues

## 🌱 Sensor Installation

### Moisture Sensors
1. **Sensor placement**:
   - **Depth**: 2-3 inches into soil
   - **Location**: Near plant roots, not touching pot edges
   - **Angle**: Slight angle prevents water pooling

2. **Connection to board**:
   - **Channels 1-8**: Correspond to pump channels
   - **Firm connection**: Ensure sensors are fully seated
   - **Test readings**: Verify sensors respond to moisture changes

3. **Calibration**:
   - **Dry soil**: Note reading (typically 20-28)
   - **Wet soil**: Note reading (typically 0-10)
   - **Set thresholds** based on plant needs

### Environmental Sensors (Optional)

#### CO2 Sensor (Adafruit SCD4X)
1. **Connection**:
   - **I2C Bus**: Connect to QWIIC_I2C0 or QWIIC_I2C1
   - **Power**: 3.3V (provided by QWIIC connector)

2. **Placement**:
   - **Plant level**: Near plant canopy
   - **Good airflow**: Avoid dead air spaces
   - **Away from direct sunlight**

3. **Configuration**:
   ```python
   ADAFRUIT_SCD4X_ENABLED = True
   ADAFRUIT_SCD4X_I2C_CHANNEL = 0
   ```

#### pH Sensor (Atlas Scientific)
1. **Components needed**:
   - **EZO-pH circuit board**
   - **pH probe** with BNC connector
   - **Calibration solutions** (pH 4.0, 7.0, 10.0)

2. **Connection**:
   - **I2C Bus**: Connect to QWIIC connector
   - **Probe**: Connect to BNC port on EZO-pH board

3. **Calibration required**:
   ```python
   from growmax.atlas_ph.calibration import calibrate_ph
   calibrate_ph()
   ```

## 🖥️ Display Setup (Optional)

### Supported Displays
- **SSD1327**: 128x128 grayscale OLED
- **SH1107**: 128x64 monochrome OLED

### Connection
1. **I2C Connection**:
   - **Recommended**: Use QWIIC_I2C1 (separate from sensors)
   - **Power**: 3.3V from QWIIC connector

2. **Configuration**:
   ```python
   DISPLAY = "SSD1327_I2C"  # or "SH1107_I2C"
   DISPLAY_I2C_CHANNEL = 1
   DISPLAY_I2C_ADDRESS = None  # Auto-detect
   ```

### Motion Sensor (Optional)
1. **PIR Sensor Setup**:
   - **Connection**: Any available GPIO pin
   - **Power**: 3.3V and GND
   - **Sensitivity**: Adjust potentiometer as needed

2. **Configuration**:
   ```python
   DISPLAY_SWITCH = 15  # GPIO pin number
   DISPLAY_SWITCH_CLASS = "MotionSensor"
   DISPLAY_SWITCH_DURATION_MS = 10000  # 10 seconds
   ```

## 🔌 I2C Relay Board (Advanced)

### When to Use Relay Boards
- **High-power pumps** (>200mA)
- **Solenoid valves** for irrigation
- **External equipment** (fans, heaters, lights)
- **Auto-refill systems**

### Connection
1. **I2C Connection**:
   - **QWIIC Connector**: Use available I2C bus
   - **Address**: Check board documentation (typically 0x27)

2. **Power Requirements**:
   - **Logic**: 3.3V from QWIIC
   - **Relay power**: May need external 5V supply
   - **Load power**: Separate supply for controlled equipment

3. **Configuration**:
   ```python
   RELAY_BOARD_ENABLED = True
   RELAY_BOARD_I2C_CHANNEL = 0
   RELAY_BOARD_NUM_RELAYS = 4  # or 8
   RELAY_BOARD_I2C_ADDRESS = 0x27
   ```

## ⚡ Power Considerations

### Power Requirements
- **Pico**: ~50mA base consumption
- **Pumps**: Up to 200mA each (8 pumps = 1.6A max)
- **Sensors**: ~10-50mA each
- **Display**: ~20-100mA
- **Total**: Plan for 2-3A capacity

### Power Supply Selection
1. **USB Power**:
   - **5V 2A minimum** for basic setups
   - **5V 3A recommended** for full 8-pump systems
   - **Quality matters**: Use reputable brands

2. **Power Distribution**:
   - **USB input**: Powers entire system
   - **5V rail**: Pumps and some sensors
   - **3.3V rail**: Logic and most sensors

### Safety Features
- **Overcurrent protection**: Built into GrowMax board
- **Water level checking**: Prevents dry pump operation
- **Conservative defaults**: Safe pump durations

## 🔧 Testing and Validation

### Initial Power-On Test
1. **Connect USB power** (no pumps connected yet)
2. **Check LED indicators** on board
3. **Connect to Thonny** and verify communication
4. **Install GrowMax library**

### Sensor Testing
1. **Moisture sensors**:
   ```python
   from growmax.moisture import Moisture
   for i in range(1, 9):
       sensor = Moisture(channel=i)
       print(f"Channel {i}: {sensor.moisture}")
   ```

2. **Water level sensor**:
   ```python
   from machine import Pin
   sensor = Pin(22, Pin.IN, Pin.PULL_DOWN)
   print(f"Water detected: {sensor.value()}")
   ```

### Pump Testing
1. **Individual pump test**:
   ```python
   from growmax.pump import Pump
   pump = Pump(channel=1)
   pump.dose(1, 3)  # 3-second test
   ```

2. **Check water flow** and verify no leaks

### System Integration Test
1. **Load complete configuration**
2. **Run main program** in test mode
3. **Monitor all readings** for several cycles
4. **Verify pump activation** when thresholds are met

## 📊 Pin Reference

### GrowMax Board Connections
| Function | GPIO Pin | Notes |
|----------|----------|-------|
| Moisture 1-8 | ADC Channels | Built-in on board |
| Pump 1-8 | PWM Channels | Built-in MOSFET drivers |
| Water Low | 22 | Voltage divider included |
| Water High | 21 | Voltage divider included |
| I2C0 SDA | 4 | QWIIC_I2C0 |
| I2C0 SCL | 5 | QWIIC_I2C0 |
| I2C1 SDA | 6 | QWIIC_I2C1 |
| I2C1 SCL | 7 | QWIIC_I2C1 |

### Available GPIO for Custom Use
- **GPIO 15**: Motion sensor, buttons
- **GPIO 16-20**: Available for custom sensors
- **GPIO 26-28**: ADC capable pins

## 🚨 Troubleshooting Hardware Issues

### No Power/Communication
- **Check USB cable** - use data cable, not charging-only
- **Try different USB port** on computer
- **Verify firmware** installation
- **Check for short circuits**

### Pump Issues
- **No pumping**: Check connections, verify pump specs
- **Weak flow**: Check tubing for kinks, prime pump
- **Continuous running**: Check water sensor, verify thresholds

### Sensor Problems
- **No readings**: Check connections, clean sensor probes
- **Erratic readings**: Check for interference, loose connections
- **Wrong readings**: Calibrate sensors, check placement

### I2C Device Issues
- **Device not found**: Check connections, verify address
- **Communication errors**: Check for bus conflicts, power issues
- **Intermittent operation**: Check cable quality, connection security

## 📚 Next Steps

Once your hardware is assembled and tested:

1. **Follow [Quick Start Guide](quick-start.md)** for software setup
2. **Choose an [example configuration](examples/)** that matches your needs
3. **Customize settings** in [Configuration Reference](configuration-reference.md)
4. **Deploy and monitor** your automated system

## 🆘 Getting Help

If you encounter hardware issues:
- **Check [Troubleshooting Guide](troubleshooting.md)** for common solutions
- **Visit [opensensor.io](https://opensensor.io)** for support
- **Post on GitHub Issues** with detailed hardware information

---

**Your hardware is now ready for automated plant care! 🌱⚡**

*Proceed to software configuration to complete your GrowMax system setup.*
