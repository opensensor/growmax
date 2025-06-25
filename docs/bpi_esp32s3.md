# 🔧 ESP32S3 BananaPi Setup Guide

Complete setup instructions for using the BPI-PicoW-S3 with GrowMax boards. This ESP32S3-based microcontroller provides WiFi and Bluetooth capabilities in a Pico-compatible form factor.

## 📋 What You'll Need

### Hardware
- **BPI-PicoW-S3** board ([BananaPi Wiki](https://wiki.banana-pi.org/BPI-PicoW-S3))
- **GrowMax board** from [opensensor.io](https://opensensor.io)
- **USB-C cable** for programming and power
- **Computer** with Python installed

### Software Requirements
- **Python 3.7+** installed on your computer
- **esptool** for flashing firmware
- **Thonny IDE** for development

## 🚨 Important Notes

The ESP32S3 setup requires additional steps compared to the standard Raspberry Pi Pico:
- **No drag-and-drop firmware installation** - must use esptool
- **Different boot process** - uses BOOT button instead of BOOTSEL
- **Comes with CircuitPython** - needs to be replaced with MicroPython

## ⚡ Step 1: Install Required Tools

### Install esptool
```bash
# Install esptool via pip
pip install esptool

# Verify installation
esptool.py version
```

### Download MicroPython Firmware
1. Visit [micropython.org/download/GENERIC_S3](https://micropython.org/download/GENERIC_S3/)
2. Download the latest **GENERIC_S3** firmware (.bin file)
3. Note the download location for later use

## 🔧 Step 2: Prepare the Device

### Enter Boot Mode
1. **Hold the BOOT button** on the BPI-PicoW-S3
2. **Connect USB-C cable** while holding BOOT button
3. **Release BOOT button** after connection is established
4. Device should now be in download mode

### Identify COM Port

#### Windows
1. **Open Device Manager**
2. **Expand "Ports (COM & LPT)"**
3. **Look for new COM port** (e.g., COM3, COM10)
4. **Note the port number** for later use

#### macOS/Linux
```bash
# List available ports
ls /dev/tty.*

# Look for something like /dev/ttyUSB0 or /dev/ttyACM0
```

## 🔥 Step 3: Flash MicroPython Firmware

### Erase Existing Firmware
```bash
# Replace COM10 with your actual port
esptool.py --chip esp32s3 --port COM10 erase_flash
```

**Expected output:**
```
esptool.py v4.6
Serial port COM10
Connecting....
Chip is ESP32-S3 (revision v0.1)
Features: WiFi, BLE
Crystal is 40MHz
Erasing flash (this may take a while)...
Chip erase completed successfully in 10.5s
Hard resetting via RTS pin...
```

### Flash MicroPython
```bash
# Replace COM10 with your port and update the firmware path
esptool.py --chip esp32s3 --port COM10 --baud 460800 write_flash -z 0x0 GENERIC_S3-20231005-v1.21.0.bin
```

**Expected output:**
```
esptool.py v4.6
Serial port COM10
Connecting....
Chip is ESP32-S3 (revision v0.1)
Features: WiFi, BLE
Crystal is 40MHz
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x00000000 to 0x0028ffff...
Compressed 2682368 bytes to 987895...
Writing at 0x00100000... (100 %)
Wrote 2682368 bytes (987895 compressed) at 0x00000000 in 45.2 seconds (effective 475.1 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

## 💻 Step 4: Setup Development Environment

### Configure Thonny IDE
1. **Launch Thonny IDE**
2. **Go to Run → Configure interpreter**
3. **Select "MicroPython (ESP32)"**
4. **Choose your COM port**
5. **Click OK**

### Test Connection
1. **Click the STOP button** in Thonny to connect
2. **You should see the MicroPython REPL**:
   ```
   MicroPython v1.21.0 on 2023-10-05; Generic ESP32S3 module with ESP32S3
   Type "help()" for more information.
   >>>
   ```

### Install GrowMax Library
1. **Go to Tools → Manage packages**
2. **Search for "growmax"**
3. **Click Install** on the latest version
4. **Wait for installation to complete**

## 🔧 Step 5: Configure for GrowMax

### Update Configuration
Create your `config.py` file with ESP32S3 settings:

```python
import machine

# Hardware Configuration - Important!
GROWMAX_MCU = "ESP32S3_BPI"  # Set to ESP32S3_BPI for BananaPi

# Rest of your configuration...
SOIL_WET_THRESHOLD = 10
PUMP_WHEN_DRY = False
PUMP_CYCLE_DURATION = 20

# Water Level Safety
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22

# WiFi Configuration (ESP32S3 advantage)
WIFI_ENABLED = True
WIFI_SSID = "YourNetwork"
WIFI_PASSWORD = "YourPassword"

# Other settings as needed...
```

### Create Main Program
```python
from growmax.routine import main

main()
```

## 🧪 Step 6: Test Your Setup

### Basic Functionality Test
1. **Run your main program** in Thonny
2. **Check for proper output**:
   ```
   Position 1 reservoir has water True and moisture value 15/10
   Position 2 reservoir has water True and moisture value 8/10
   ...
   ```
3. **Verify WiFi connection** (if enabled)
4. **Test pump operation** if connected

### Troubleshooting Connection Issues

#### Device Not Recognized
- **Try different USB cable** - ensure it's a data cable
- **Check drivers** - may need ESP32 USB drivers on Windows
- **Try different USB port**

#### Flash Process Fails
- **Ensure BOOT button was held** during connection
- **Try lower baud rate**: `--baud 115200` instead of 460800
- **Check cable quality** - poor cables cause flash failures

#### Thonny Can't Connect
- **Reset the device** - disconnect and reconnect USB
- **Try different interpreter** - "MicroPython (generic)" instead of ESP32
- **Check COM port** - may have changed after flashing

## 🌟 ESP32S3 Advantages

### Built-in WiFi
- **No additional hardware** needed for connectivity
- **Better WiFi performance** than Pico W
- **Dual-band support** (2.4GHz and 5GHz)

### More Memory
- **Larger RAM** for complex applications
- **More flash storage** for additional features
- **Better performance** for sensor-heavy setups

### Advanced Features
- **Bluetooth support** (future GrowMax features)
- **More GPIO pins** for expansion
- **Hardware encryption** for secure communications

## ⚠️ Important Differences from Pico

### Power Considerations
- **Same 5V rail limitations** apply
- **Pumps still limited to <200mA each**
- **Use I2C relay boards** for higher power applications

### Pin Compatibility
- **Most pins work the same** as Pico
- **Some advanced features** may use different pins
- **Check GrowMax board documentation** for any ESP32S3-specific notes

## 🚀 Next Steps

Once your ESP32S3 is set up:

1. **Follow the [Quick Start Guide](quick-start.md)** for basic configuration
2. **Enable WiFi features** for remote monitoring
3. **Explore [examples](examples/)** that take advantage of WiFi capabilities
4. **Consider cloud logging** with opensensor.io integration

## 🔧 Advanced Configuration

### WiFi Optimization
```python
# ESP32S3-specific WiFi settings
WIFI_ENABLED = True
WIFI_SSID = "YourNetwork"
WIFI_PASSWORD = "YourPassword"

# Enable cloud features
OPEN_SENSOR_COLLECT_DATA = True
OPEN_SENSOR_API_KEY = "your-api-key"
DEVICE_NAME = "ESP32S3-GrowMax"
```

### Memory Management
```python
# ESP32S3 has more memory, but still good practice
import gc
gc.collect()  # Force garbage collection
print("Free memory:", gc.mem_free())
```

## 🆘 Getting Help

### Common Issues
- **Flash failures**: Usually cable or driver issues
- **Connection problems**: Check COM port and drivers
- **WiFi issues**: Verify network compatibility (2.4GHz)

### Support Resources
- **[Troubleshooting Guide](troubleshooting.md)** - Common solutions
- **[BananaPi Wiki](https://wiki.banana-pi.org/BPI-PicoW-S3)** - Hardware documentation
- **[opensensor.io](https://opensensor.io)** - GrowMax support

---

**Congratulations! Your ESP32S3 is now ready for advanced GrowMax applications! 🚀🌱**

*The ESP32S3 provides enhanced capabilities while maintaining full compatibility with GrowMax boards and software.*
