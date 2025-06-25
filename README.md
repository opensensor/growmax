# 🌱 GrowMax - Smart Plant Watering Automation

**Micropython library for automated plant watering and environmental monitoring**

[![GitHub Stars](https://img.shields.io/github/stars/opensensor/growmax?style=social)](https://github.com/opensensor/growmax)
[![PyPI Version](https://img.shields.io/pypi/v/growmax)](https://pypi.org/project/growmax/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Transform your plant care with intelligent automation! GrowMax provides everything you need to build a sophisticated plant monitoring and watering system using affordable microcontrollers.

![GrowMax Board with Screen and CO2 Sensor](https://github.com/opensensor/growmax/blob/main/images/growmax_install_with_screen.jpg)

## 🚀 Why Choose GrowMax?

- **🎯 Plug & Play**: Get started in minutes with pre-configured settings
- **🔧 Highly Configurable**: 20+ configuration options for any setup
- **📊 Multi-Sensor Support**: Soil moisture, pH, CO2, water level monitoring
- **💧 Smart Watering**: Automated pumping with safety features
- **📱 Remote Monitoring**: WiFi connectivity with cloud data collection
- **🖥️ Visual Feedback**: OLED display support with motion activation
- **⚡ Power Efficient**: Designed for 24/7 operation
- **🛡️ Safety First**: Built-in water level checks and pump protection

## 🛒 Get Your Hardware

Purchase GrowMax boards and complete kits at **[opensensor.io](https://opensensor.io)**

## ⚡ Quick Start

### 1. Install Firmware
Choose your microcontroller:
- **Raspberry Pi Pico**: [Download Firmware](https://micropython.org/download/rp2-pico/)
- **Raspberry Pi Pico W**: [Download Firmware](https://micropython.org/download/rp2-pico-w/)
- **ESP32S3 (BananaPi)**: [See ESP32S3 Setup Guide](docs/bpi_esp32s3.md)

### 2. Install GrowMax Library
1. Install [Thonny IDE](https://thonny.org/)
2. Connect your device and launch Thonny
3. Go to **Tools → Manage Packages**
4. Search for `growmax` and install the latest version

### 3. Create Your Main Program
Create `main.py` on your device:
```python
from growmax.routine import main

main()
```

### 4. Configure Your System
1. Copy `/lib/growmax/config.py` to your device root as `config.py`
2. Customize settings for your setup (see [Configuration Guide](docs/configuration-reference.md))
3. Run `main.py` in Thonny to test

### 5. Deploy
Connect 5V USB power - your system is now autonomous! 🎉

## 📖 Documentation

| Guide | Description |
|-------|-------------|
| [🚀 Quick Start](docs/quick-start.md) | Get running in 10 minutes |
| [⚙️ Configuration Reference](docs/configuration-reference.md) | Complete settings guide |
| [🔧 Hardware Setup](docs/instructions.md) | Assembly and connections |
| [💡 Examples](docs/examples/) | Real-world use cases |
| [🔍 Troubleshooting](docs/troubleshooting.md) | Common issues & solutions |
| [📚 API Reference](docs/api-reference.md) | Technical documentation |

## 🌟 Key Features

### 💧 Smart Watering System
- **8-channel soil moisture monitoring** with individual thresholds
- **Automated pump control** with configurable duration
- **Water level safety checks** prevent dry pumping
- **High-power pump support** via I2C relay boards

### 📊 Environmental Monitoring
- **CO2 monitoring** with Adafruit SCD4X sensors
- **pH measurement** using Atlas Scientific probes
- **Temperature and humidity** tracking
- **Real-time data logging** to OpenSensor.io cloud

### 🖥️ Display & Interface
- **OLED display support** (SSD1327, SH1107)
- **Motion-activated display** for power efficiency
- **Real-time status updates** showing all sensor readings
- **Visual pump and sensor status** indicators

### 🌐 Connectivity & Remote Control
- **WiFi connectivity** for remote monitoring
- **Cloud data collection** with opensensor.io integration
- **Remote pump control** (experimental feature)
- **Device management** through web dashboard

## 🔧 Basic Configuration

Here are the most commonly used settings:

```python
# Soil moisture threshold (0-28, lower = wetter)
SOIL_WET_THRESHOLD = 10

# Enable water level safety check
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22  # GPIO pin

# Pump settings
PUMP_WHEN_DRY = False  # Safety: only pump when water detected
PUMP_CYCLE_DURATION = 30  # seconds

# WiFi for remote monitoring
WIFI_ENABLED = True
WIFI_SSID = "YourNetwork"
WIFI_PASSWORD = "YourPassword"
```

See the [complete configuration guide](docs/configuration-reference.md) for all 20+ options.

## 🏗️ Example Setups

### 🌿 Basic Single Plant
Perfect for beginners - monitor and water one plant automatically.

### 🏡 Home Garden (8 Plants)
Full 8-channel setup with individual moisture thresholds per plant.

### 🏭 Greenhouse Monitoring
Advanced setup with CO2, pH, temperature monitoring and cloud logging.

### 💪 High-Power Irrigation
Using relay boards to control large pumps and irrigation systems.

[View detailed examples →](docs/examples/)

## ⚡ Power & Safety

**Important Safety Information:**
- **Pico Power Limit**: 300mA max current (shared 5V rail)
- **Onboard Pumps**: Use 5V pumps drawing <200mA each
- **Higher Power Applications**: Require I2C relay boards (not direct connection)
- **Water Sensors**: Designed for Optomax liquid sensors with 4V→3.3V conversion
- **Always Enable Water Level Checks**: Prevents pump damage from dry running

## 🆘 Need Help?

- **📖 Documentation**: Check our [comprehensive guides](docs/)
- **🐛 Issues**: Report bugs on [GitHub Issues](https://github.com/opensensor/growmax/issues)
- **💬 Community**: Join discussions on [opensensor.io](https://opensensor.io)
- **📧 Support**: Contact us through opensensor.io

## 🤝 Contributing

We welcome contributions! Whether it's:
- 🐛 Bug reports and fixes
- 📖 Documentation improvements
- ✨ New features and sensors
- 💡 Example projects and use cases

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by [OpenSensor.io](https://opensensor.io)**

*Automate your garden, monitor your plants, grow smarter! 🌱*
