# 🚀 Quick Start Guide

Get your GrowMax system running in 10 minutes! This guide covers the essential steps to set up basic plant watering automation.

## 📋 What You'll Need

### Hardware
- **GrowMax board** from [opensensor.io](https://opensensor.io)
- **Raspberry Pi Pico or Pico W** (or ESP32S3 BananaPi)
- **Micro USB cable** for programming and power
- **Water reservoir** (bottle, container, etc.)
- **Small water pump** (5V, <200mA)
- **Optomax water level sensor** (optional but recommended)
- **Tubing** for water connections

### Software
- **Computer** (Windows, Mac, or Linux)
- **Internet connection** for downloading firmware and packages

## ⚡ Step 1: Install Firmware (3 minutes)

### For Raspberry Pi Pico/Pico W:
1. **Download firmware:**
   - Pico: [micropython.org/download/rp2-pico](https://micropython.org/download/rp2-pico/)
   - Pico W: [micropython.org/download/rp2-pico-w](https://micropython.org/download/rp2-pico-w/)

2. **Flash firmware:**
   - Hold BOOTSEL button while connecting USB
   - Drag downloaded `.uf2` file to RPI-RP2 drive
   - Device will reboot automatically

### For ESP32S3 BananaPi:
See our [detailed ESP32S3 setup guide](bpi_esp32s3.md) - requires additional steps.

## 💻 Step 2: Install Software (2 minutes)

1. **Download and install Thonny IDE:**
   - Visit [thonny.org](https://thonny.org/)
   - Download for your operating system
   - Install with default settings

2. **Connect to your device:**
   - Launch Thonny
   - Connect your GrowMax board via USB
   - Bottom-right corner should show "MicroPython (Raspberry Pi Pico)"
   - If not, go to **Run → Configure interpreter** and select your device

## 📦 Step 3: Install GrowMax Library (1 minute)

1. **Install from PyPI:**
   - In Thonny, go to **Tools → Manage packages**
   - Search for `growmax`
   - Click **Install** on the latest version
   - Wait for installation to complete

## 🔧 Step 4: Basic Configuration (2 minutes)

1. **Copy default config:**
   - In Thonny file browser, navigate to `/lib/growmax/config.py`
   - Right-click and select **Copy**
   - Navigate to device root directory
   - Right-click and **Paste**
   - Rename to `config.py` (remove the path)

2. **Edit basic settings:**
   ```python
   # Essential settings for first run
   SOIL_WET_THRESHOLD = 12        # Start with drier threshold
   PUMP_WHEN_DRY = False         # Safety first!
   PUMP_CYCLE_DURATION = 15      # Short cycles initially
   WATER_SENSOR_LOW_ENABLED = True  # Enable if you have sensor
   WATER_SENSOR_LOW = 22         # GPIO pin for water sensor
   ```

## 🌱 Step 5: Create Main Program (1 minute)

1. **Create main.py:**
   - In Thonny, create a new file
   - Add this code:
   ```python
   from growmax.routine import main
   
   main()
   ```
   - Save as `main.py` to your device root

## 🧪 Step 6: Test Your Setup (1 minute)

1. **Run the program:**
   - Click the **Run** button in Thonny
   - Watch the output in the terminal

2. **What you should see:**
   ```
   Position 1 reservoir has water True and moisture value 15/12
   Position 2 reservoir has water True and moisture value 8/12
   Position 3 reservoir has water True and moisture value 20/12
   ...
   ```

3. **Understanding the output:**
   - **Position**: Plant position (1-8)
   - **Reservoir has water**: Water sensor status
   - **Moisture value**: Current reading / threshold
   - **Higher numbers = drier soil**

## 🎯 Step 7: Fine-Tune Settings

### Adjust Moisture Thresholds
Based on your test run, adjust thresholds in `config.py`:

```python
# If plants are too wet, increase threshold
SOIL_WET_THRESHOLD = 15

# If plants are too dry, decrease threshold  
SOIL_WET_THRESHOLD = 8

# Different thresholds per plant
SOIL_WET_THRESHOLD = [10, 12, 8, 15, 10, 12, 18, 10]
```

### Test Pump Duration
```python
# Start short and increase as needed
PUMP_CYCLE_DURATION = 10  # Very short for testing
PUMP_CYCLE_DURATION = 20  # Typical for small plants
PUMP_CYCLE_DURATION = 30  # Typical for larger plants
```

## 🔌 Step 8: Deploy for Autonomous Operation

1. **Final test:**
   - Run your program one more time
   - Verify all settings work correctly
   - Check that pumps activate when soil is dry

2. **Deploy:**
   - Disconnect from computer
   - Connect 5V USB power supply
   - Your system is now autonomous! 🎉

## ✅ Success Checklist

- [ ] Firmware installed and device connects to Thonny
- [ ] GrowMax library installed successfully
- [ ] Config file copied and customized
- [ ] Main program created and runs without errors
- [ ] Moisture readings make sense for your plants
- [ ] Water sensor detects water level (if installed)
- [ ] Pumps activate when soil is dry
- [ ] System runs autonomously on USB power

## 🚨 Safety Reminders

- **Always enable water level sensor** if you have one
- **Start with short pump cycles** (10-15 seconds)
- **Monitor first few watering cycles** to ensure proper amounts
- **Use 5V pumps drawing <200mA** for onboard pump ports
- **Never leave pumps running unattended** until you've verified proper operation

## 🆘 Quick Troubleshooting

### Device won't connect to Thonny
- Try different USB cable
- Check device appears in Device Manager (Windows)
- Reinstall firmware if needed

### GrowMax package won't install
- Check internet connection
- Try restarting Thonny
- Manually download and install if needed

### No moisture readings
- Check sensor connections
- Verify sensors are properly inserted in soil
- Try different GPIO pins if using custom sensors

### Pumps not working
- Check `PUMP_WHEN_DRY` setting
- Verify water sensor is working
- Check pump power connections
- Ensure pump draws <200mA

### Plants getting too much/little water
- Adjust `SOIL_WET_THRESHOLD` values
- Modify `PUMP_CYCLE_DURATION`
- Check soil sensor placement depth

## 🎉 What's Next?

Now that you have basic watering working, explore advanced features:

- **[📊 Add Environmental Sensors](configuration-reference.md#environmental-sensors)** - CO2, pH monitoring
- **[🖥️ Add a Display](configuration-reference.md#display-configuration)** - Real-time status display
- **[🌐 Enable WiFi](configuration-reference.md#wifi--cloud-integration)** - Remote monitoring
- **[🔌 Add Relay Board](configuration-reference.md#i2c-relay-board-integration)** - Control high-power equipment
- **[💡 See Examples](examples/)** - Real-world configurations

## 📚 Additional Resources

- **[⚙️ Complete Configuration Guide](configuration-reference.md)** - All 20+ options explained
- **[🔧 Hardware Setup Guide](instructions.md)** - Detailed assembly instructions
- **[🔍 Troubleshooting Guide](troubleshooting.md)** - Solve common issues
- **[📖 API Reference](api-reference.md)** - Technical documentation

---

**Congratulations! Your plants are now on autopilot! 🌱✨**

*Need help? Check our [troubleshooting guide](troubleshooting.md) or visit [opensensor.io](https://opensensor.io) for support.*
