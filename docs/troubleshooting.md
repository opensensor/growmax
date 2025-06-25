# 🔍 Troubleshooting Guide

Having issues with your GrowMax system? This guide covers the most common problems and their solutions.

## 🚨 Emergency Issues

### 🚰 Plants Being Over-Watered
**Immediate Action:**
1. **Disconnect power** to stop pumping
2. **Check `PUMP_CYCLE_DURATION`** - reduce to 5-10 seconds
3. **Increase `SOIL_WET_THRESHOLD`** - higher numbers = drier soil needed before watering
4. **Verify sensor placement** - sensors should be in root zone, not too deep

### 💧 Water Reservoir Empty, Pumps Still Running
**Immediate Action:**
1. **Disconnect power** immediately
2. **Check water level sensor** connections
3. **Verify `WATER_SENSOR_LOW_ENABLED = True`**
4. **Never set `PUMP_WHEN_DRY = True`** unless you have unlimited water supply

## 🔧 Hardware Issues

### Device Won't Connect to Computer

**Symptoms:** Thonny can't find device, no serial connection

**Solutions:**
1. **Try different USB cable** - data cables, not just charging cables
2. **Check Device Manager (Windows):**
   - Look for "USB Serial Device" or "Raspberry Pi Pico"
   - If missing, try different USB port
3. **Reinstall firmware:**
   - Hold BOOTSEL button while connecting
   - Flash firmware again
4. **Driver issues:**
   - Windows: Install Raspberry Pi Pico drivers
   - Mac/Linux: Usually work automatically

### Moisture Sensors Not Reading

**Symptoms:** All readings show 0 or very high numbers

**Solutions:**
1. **Check sensor connections:**
   - Ensure sensors are properly seated in board
   - Look for loose connections
2. **Verify sensor placement:**
   - Insert sensors 2-3 inches into soil
   - Avoid touching metal parts with fingers
   - Keep sensors away from fertilizer deposits
3. **Test individual sensors:**
   ```python
   from growmax.moisture import Moisture
   sensor = Moisture(channel=1)  # Test channel 1
   print(sensor.moisture)
   ```
4. **Clean sensors:**
   - Gently clean metal probes with soft cloth
   - Remove any corrosion or buildup

### Water Level Sensor Not Working

**Symptoms:** Always shows "has water False" or "has water True"

**Solutions:**
1. **Check GPIO pin configuration:**
   ```python
   WATER_SENSOR_LOW_ENABLED = True
   WATER_SENSOR_LOW = 22  # Use GPIO 21 or 22
   ```
2. **Verify sensor type:**
   - Use Optomax liquid level sensors
   - Other sensors may need different GPIO pins
3. **Test sensor manually:**
   ```python
   from machine import Pin
   sensor = Pin(22, Pin.IN, Pin.PULL_DOWN)
   print(sensor.value())  # Should change when sensor touches water
   ```
4. **Check wiring:**
   - Ensure proper connections to GPIO 21 or 22
   - These pins have built-in voltage dividers

### Pumps Not Working

**Symptoms:** No pumping action, or pumps run but no water flows

**Solutions:**
1. **Check power requirements:**
   - Use 5V pumps only
   - Ensure pump draws <200mA
   - Check pump specifications
2. **Verify pump connections:**
   - Ensure proper wiring to pump ports
   - Check for loose connections
3. **Test pump manually:**
   ```python
   from growmax.pump import Pump
   pump = Pump(channel=1)
   pump.dose(1, 5)  # Run for 5 seconds
   ```
4. **Check tubing:**
   - Ensure no kinks or blockages
   - Prime pump if needed
   - Check that intake is submerged

## 💻 Software Issues

### GrowMax Package Won't Install

**Symptoms:** Error installing from PyPI in Thonny

**Solutions:**
1. **Check internet connection:**
   - Ensure computer has internet access
   - Try different network if needed
2. **Restart Thonny:**
   - Close and reopen Thonny IDE
   - Try installation again
3. **Manual installation:**
   - Download package manually from PyPI
   - Install using Thonny's file manager
4. **Clear package cache:**
   - Tools → Manage packages → Clear cache

### Config File Errors

**Symptoms:** Import errors, syntax errors in config

**Solutions:**
1. **Check file location:**
   - Config file must be named `config.py`
   - Must be in device root directory (not in folders)
2. **Verify syntax:**
   ```python
   # Correct syntax
   SOIL_WET_THRESHOLD = 10
   WIFI_SSID = "NetworkName"
   
   # Common errors to avoid
   SOIL_WET_THRESHOLD = 10,  # Remove comma
   WIFI_SSID = NetworkName   # Missing quotes
   ```
3. **Reset to defaults:**
   - Copy fresh config from `/lib/growmax/config.py`
   - Make changes gradually

### Program Crashes or Freezes

**Symptoms:** Program stops running, memory errors, device resets

**Solutions:**
1. **Check memory usage:**
   - Disable unnecessary features first
   - Monitor memory in program output
2. **Simplify configuration:**
   ```python
   # Minimal config for testing
   WIFI_ENABLED = False
   DISPLAY = None
   ADAFRUIT_SCD4X_ENABLED = False
   ATLAS_PH_METER_ENABLED = False
   ```
3. **Check for infinite loops:**
   - Look for blocking code in custom modifications
   - Ensure proper error handling

## 🌐 WiFi and Connectivity Issues

### WiFi Won't Connect

**Symptoms:** "WiFi connection failed" messages

**Solutions:**
1. **Check network settings:**
   ```python
   WIFI_ENABLED = True
   WIFI_SSID = "YourExactNetworkName"  # Case sensitive!
   WIFI_PASSWORD = "YourExactPassword"
   ```
2. **Network compatibility:**
   - Use 2.4GHz networks only (not 5GHz)
   - Avoid networks with special characters
   - Try mobile hotspot for testing
3. **Signal strength:**
   - Move device closer to router
   - Check for interference
4. **Router settings:**
   - Ensure WPA2/WPA3 security (not WEP)
   - Check MAC address filtering
   - Verify DHCP is enabled

### Cloud Data Not Uploading

**Symptoms:** No data appearing on opensensor.io dashboard

**Solutions:**
1. **Check API configuration:**
   ```python
   OPEN_SENSOR_COLLECT_DATA = True
   OPEN_SENSOR_API_KEY = "your-actual-api-key"  # From opensensor.io profile
   DEVICE_NAME = "YourDeviceName"
   ```
2. **Verify API key:**
   - Log into opensensor.io/members/profile
   - Copy API key exactly (no extra spaces)
3. **Check internet connectivity:**
   - Ensure WiFi is working
   - Test with simple web request

## 🖥️ Display Issues

### Display Not Working

**Symptoms:** Blank screen, no display output

**Solutions:**
1. **Check display configuration:**
   ```python
   DISPLAY = "SSD1327_I2C"  # or "SH1107_I2C"
   DISPLAY_I2C_CHANNEL = 0
   DISPLAY_I2C_ADDRESS = None  # Auto-detect
   ```
2. **Verify I2C connections:**
   - Check SDA/SCL wiring
   - Ensure proper power connections
3. **Test I2C address:**
   ```python
   # Scan for I2C devices
   from machine import I2C, Pin
   i2c = I2C(0, sda=Pin(4), scl=Pin(5))
   print(i2c.scan())  # Should show device addresses
   ```
4. **Try different I2C channel:**
   ```python
   DISPLAY_I2C_CHANNEL = 1  # Try channel 1 instead of 0
   ```

### Motion Sensor Not Activating Display

**Symptoms:** Display never turns on with motion

**Solutions:**
1. **Check motion sensor configuration:**
   ```python
   DISPLAY_SWITCH = 15  # GPIO pin number
   DISPLAY_SWITCH_CLASS = "MotionSensor"
   DISPLAY_SWITCH_DURATION_MS = 10000  # 10 seconds
   ```
2. **Test motion sensor:**
   ```python
   from machine import Pin
   motion = Pin(15, Pin.IN)
   print(motion.value())  # Should change with motion
   ```
3. **Adjust sensitivity:**
   - Check motion sensor hardware settings
   - Try different GPIO pin

## 📊 Sensor Issues

### CO2 Sensor Not Reading

**Symptoms:** No CO2 readings, sensor errors

**Solutions:**
1. **Check sensor configuration:**
   ```python
   ADAFRUIT_SCD4X_ENABLED = True
   ADAFRUIT_SCD4X_I2C_CHANNEL = 0
   ```
2. **Verify I2C connections:**
   - Ensure proper SDA/SCL wiring
   - Check power connections (3.3V)
3. **Sensor warm-up:**
   - SCD4X sensors need 2-3 minutes to stabilize
   - Wait before expecting accurate readings

### pH Sensor Not Working

**Symptoms:** No pH readings, calibration issues

**Solutions:**
1. **Check Atlas Scientific configuration:**
   ```python
   ATLAS_PH_METER_ENABLED = True
   ATLAS_PH_I2C_CHANNEL = 0
   ATLAS_PH_METER_ADDRESS = None  # Auto-detect
   ```
2. **Verify probe connections:**
   - Ensure BNC connector is tight
   - Check probe is in solution
3. **Calibration required:**
   - pH probes need regular calibration
   - Use pH 4.0, 7.0, and 10.0 calibration solutions

## 🔌 Relay Board Issues

### Relays Not Switching

**Symptoms:** High-power equipment not turning on/off

**Solutions:**
1. **Check relay configuration:**
   ```python
   RELAY_BOARD_ENABLED = True
   RELAY_BOARD_I2C_CHANNEL = 0
   RELAY_BOARD_NUM_RELAYS = 4  # Match your board
   RELAY_BOARD_I2C_ADDRESS = 0x27
   ```
2. **Verify I2C address:**
   - Check relay board documentation
   - Common addresses: 0x27, 0x20, 0x21
3. **Test relay manually:**
   ```python
   from growmax.utils.relays import initialize_relay_board
   relay_board = initialize_relay_board()
   relay_board.turn_on(1)  # Turn on relay 1
   ```
4. **Check power requirements:**
   - Ensure relay board has adequate power
   - Some boards need external power supply

## 🔧 Advanced Troubleshooting

### Memory Issues

**Symptoms:** "MemoryError" or frequent crashes

**Solutions:**
1. **Monitor memory usage:**
   ```python
   import gc
   print("Free memory:", gc.mem_free())
   gc.collect()  # Force garbage collection
   ```
2. **Reduce memory usage:**
   - Disable unused features
   - Reduce sensor polling frequency
   - Simplify display output

### Performance Issues

**Symptoms:** Slow response, long delays between readings

**Solutions:**
1. **Optimize configuration:**
   - Reduce number of active sensors
   - Increase sleep intervals
   - Disable WiFi if not needed
2. **Check for blocking operations:**
   - Long pump cycles
   - Network timeouts
   - Sensor initialization delays

### Custom Modifications Not Working

**Symptoms:** Custom code causes errors or unexpected behavior

**Solutions:**
1. **Test incrementally:**
   - Add one modification at a time
   - Test each change thoroughly
2. **Check imports:**
   - Ensure all required modules are available
   - Verify custom module paths
3. **Error handling:**
   ```python
   try:
       # Your custom code here
       pass
   except Exception as e:
       print(f"Custom code error: {e}")
   ```

## 🆘 Getting Help

### Before Asking for Help

1. **Check this troubleshooting guide** thoroughly
2. **Review your configuration** against the examples
3. **Test with minimal configuration** to isolate issues
4. **Note exact error messages** and when they occur

### Where to Get Help

- **📖 Documentation**: [Complete guides](../README.md#documentation)
- **🐛 GitHub Issues**: [Report bugs](https://github.com/opensensor/growmax/issues)
- **💬 Community**: [opensensor.io forums](https://opensensor.io)
- **📧 Direct Support**: Contact through opensensor.io

### Information to Include When Asking for Help

1. **Hardware setup:**
   - Microcontroller type (Pico, Pico W, ESP32S3)
   - GrowMax board version
   - Connected sensors and displays

2. **Software versions:**
   - MicroPython firmware version
   - GrowMax package version
   - Thonny IDE version

3. **Configuration:**
   - Your `config.py` file (remove sensitive info like WiFi passwords)
   - Any custom modifications

4. **Error details:**
   - Exact error messages
   - When the error occurs
   - Steps to reproduce

5. **What you've tried:**
   - Solutions attempted from this guide
   - Any temporary workarounds found

## 🔄 Reset Procedures

### Soft Reset (Recommended First)
1. **Reset configuration:**
   - Copy fresh `config.py` from `/lib/growmax/config.py`
   - Make minimal changes for testing

2. **Restart program:**
   - Stop current program in Thonny
   - Run again with fresh configuration

### Hard Reset (If Needed)
1. **Reinstall firmware:**
   - Flash fresh MicroPython firmware
   - Reinstall GrowMax package

2. **Start from scratch:**
   - Follow [Quick Start Guide](quick-start.md) step by step
   - Add features one at a time

---

**Remember: Most issues are configuration-related and can be solved by carefully reviewing your settings against the examples in this guide.**

*Still stuck? Don't hesitate to reach out for help at [opensensor.io](https://opensensor.io)!*
