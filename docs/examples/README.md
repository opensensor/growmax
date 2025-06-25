# 💡 GrowMax Examples

Real-world configuration examples for different use cases. Each example includes complete configuration files and setup instructions.

## 🌿 Basic Examples

### [Single Plant Setup](single-plant.md)
Perfect for beginners - monitor and water one plant automatically.
- **Complexity**: Beginner
- **Features**: Basic moisture monitoring, single pump
- **Hardware**: GrowMax board + Pico + 1 pump

### [Multi-Plant Garden](multi-plant-garden.md)
Full 8-channel setup with individual moisture thresholds per plant.
- **Complexity**: Intermediate
- **Features**: 8 moisture sensors, individual thresholds
- **Hardware**: GrowMax board + Pico + 8 pumps

## 🏡 Home Automation

### [Smart Indoor Garden](smart-indoor-garden.md)
WiFi-enabled system with remote monitoring and cloud data logging.
- **Complexity**: Intermediate
- **Features**: WiFi, cloud logging, remote monitoring
- **Hardware**: GrowMax board + Pico W + sensors

### [Apartment Herb Garden](apartment-herb-garden.md)
Compact setup optimized for small spaces and herb growing.
- **Complexity**: Beginner
- **Features**: Optimized for herbs, compact design
- **Hardware**: GrowMax board + Pico + 4 pumps

## 🏭 Advanced Systems

### [Greenhouse Monitoring](greenhouse-monitoring.md)
Complete environmental monitoring with CO2, pH, temperature, and humidity.
- **Complexity**: Advanced
- **Features**: CO2 sensor, pH monitoring, environmental logging
- **Hardware**: GrowMax board + Pico W + multiple sensors + display

### [High-Power Irrigation](high-power-irrigation.md)
Using relay boards to control large pumps and irrigation systems.
- **Complexity**: Advanced
- **Features**: Relay board integration, high-power pumps
- **Hardware**: GrowMax board + Pico + relay board + large pumps


## 🎯 Specialized Applications

### [Succulent Care Station](succulent-care.md)
Optimized for drought-tolerant plants with infrequent watering cycles.
- **Complexity**: Beginner
- **Features**: Extended dry periods, minimal watering
- **Hardware**: GrowMax board + Pico + minimal pumps

### [Seedling Propagation](seedling-propagation.md)
High-frequency, low-volume watering for seed starting and propagation.
- **Complexity**: Intermediate
- **Features**: Frequent light watering, humidity monitoring
- **Hardware**: GrowMax board + Pico + misting system

### [Vacation Plant Care](vacation-care.md)
Reliable long-term automation for when you're away from home.
- **Complexity**: Intermediate
- **Features**: Extended operation, safety features, remote monitoring
- **Hardware**: GrowMax board + Pico W + large reservoir

## 🔧 Configuration Patterns

### [Testing and Development](testing-config.md)
Safe configuration for testing and development without risking plants.
- **Purpose**: Development and testing
- **Features**: Short cycles, safety overrides, verbose logging

### [Minimal Power Setup](minimal-power.md)
Optimized for battery operation and minimal power consumption.
- **Purpose**: Battery/solar operation
- **Features**: Power optimization, sleep modes, minimal features

### [Maximum Features](maximum-features.md)
Showcase configuration using all available GrowMax features.
- **Purpose**: Demonstration and testing
- **Features**: All sensors, display, WiFi, cloud logging, relays

## 📊 Comparison Chart

| Example | Complexity | Plants | Sensors | Display | WiFi | Cloud | Relays |
|---------|------------|--------|---------|---------|------|-------|--------|
| Single Plant | Beginner | 1 | Moisture | ❌ | ❌ | ❌ | ❌ |
| Multi-Plant | Intermediate | 8 | Moisture | ❌ | ❌ | ❌ | ❌ |
| Smart Indoor | Intermediate | 4-8 | Moisture | ❌ | ✅ | ✅ | ❌ |
| Greenhouse | Advanced | 8 | All | ✅ | ✅ | ✅ | ❌ |
| High-Power | Advanced | 8 | Moisture | ❌ | ❌ | ❌ | ✅ |

## 🚀 Getting Started

1. **Choose an example** that matches your needs and experience level
2. **Review the hardware requirements** to ensure you have everything needed
3. **Follow the setup instructions** in each example
4. **Customize the configuration** for your specific plants and environment
5. **Test thoroughly** before deploying for autonomous operation

## 💡 Tips for Success

- **Start simple** - begin with basic examples and add features gradually
- **Test incrementally** - verify each feature works before adding the next
- **Monitor closely** - watch your system for the first few days of operation
- **Document changes** - keep notes on what works for your specific setup
- **Safety first** - always enable water level sensors and use conservative pump durations

## 🔗 Related Documentation

- **[⚙️ Configuration Reference](../configuration-reference.md)** - Complete settings guide
- **[🚀 Quick Start Guide](../quick-start.md)** - Basic setup instructions
- **[🔍 Troubleshooting](../troubleshooting.md)** - Solve common issues
- **[🔧 Hardware Setup Guide](../instructions.md)** - Assembly and connections

---

**Ready to build your automated garden? Pick an example and get started! 🌱**
