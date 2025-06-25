# 🌿 Single Plant Setup

Perfect for beginners who want to automate watering for one plant. This example demonstrates the basic functionality of GrowMax with minimal complexity.

## 📋 What You'll Need

### Hardware
- GrowMax board from [opensensor.io](https://opensensor.io)
- Raspberry Pi Pico (or Pico W)
- 1x small water pump (5V, <200mA)
- 1x Optomax water level sensor (recommended)
- Water reservoir (bottle or container)
- Tubing for water connections
- Micro USB cable and 5V power supply

### Plant Considerations
This setup works well for:
- **Houseplants**: Pothos, snake plants, rubber plants
- **Herbs**: Basil, mint, parsley
- **Small vegetables**: Cherry tomatoes, peppers
- **Flowering plants**: African violets, begonias

## 🔧 Configuration

Create this `config.py` file on your device:

```python
import machine

# Hardware Configuration
GROWMAX_MCU = "RP2040"

# Soil Moisture & Watering - Using only position 1
SOIL_WET_THRESHOLD = 12        # Start conservative (drier)
PUMP_WHEN_DRY = False         # Safety: only pump when water detected
PUMP_CYCLE_DURATION = 20      # 20 seconds - adjust based on plant size

# Water Level Safety
WATER_SENSOR_LOW_ENABLED = True
WATER_SENSOR_LOW = 22         # GPIO pin for water sensor

# Disable unused features for simplicity
RELAY_BOARD_ENABLED = False
ADAFRUIT_SCD4X_ENABLED = False
ATLAS_PH_METER_ENABLED = False
DISPLAY = None

# WiFi disabled for basic setup
WIFI_ENABLED = False
WIFI_SSID = ""
WIFI_PASSWORD = ""

# Cloud features disabled
OPEN_SENSOR_COLLECT_DATA = False
OPEN_SENSOR_API_KEY = None
DEVICE_NAME = "Single-Plant-Setup"
OPEN_SENSOR_RETRIEVE_COMMANDS = False
```

## 🌱 Setup Instructions

### 1. Hardware Assembly
1. **Mount your GrowMax board** with the Pico attached
2. **Connect the water pump** to pump port 1 on the GrowMax board
3. **Install moisture sensor** in position 1 (insert 2-3 inches into soil)
4. **Connect water level sensor** to GPIO 22 (place in reservoir)
5. **Set up tubing** from pump to plant, ensuring good water flow

### 2. Software Setup
1. **Install MicroPython firmware** on your Pico
2. **Install GrowMax library** via Thonny IDE
3. **Copy the configuration** above to `config.py` on your device
4. **Create main.py**:
   ```python
   from growmax.routine import main
   
   main()
   ```

### 3. Initial Testing
1. **Run the program** in Thonny IDE
2. **Check the output** - you should see something like:
   ```
   Position 1 reservoir has water True and moisture value 15/12
   Position 2 reservoir has water True and moisture value 0/12
   Position 3 reservoir has water True and moisture value 0/12
   ...
   ```
3. **Verify readings**:
   - Position 1 should show actual moisture readings
   - Positions 2-8 will show 0 (no sensors connected)
   - Water sensor should show `True` when reservoir has water

## 🎯 Fine-Tuning Your Setup

### Adjusting Moisture Threshold
The `SOIL_WET_THRESHOLD` determines when your plant gets watered:

```python
# For plants that like it moist (ferns, peace lilies)
SOIL_WET_THRESHOLD = 8

# For average houseplants (pothos, rubber plants)
SOIL_WET_THRESHOLD = 12

# For plants that prefer drier soil (snake plants, succulents)
SOIL_WET_THRESHOLD = 18
```

**Testing Tips:**
- Start with a higher number (drier) and adjust down if needed
- Water your plant manually, then check the moisture reading
- The reading when soil is "just right" is your target threshold

### Adjusting Pump Duration
The `PUMP_CYCLE_DURATION` controls how long the pump runs:

```python
# Small plants or seedlings
PUMP_CYCLE_DURATION = 10

# Medium houseplants
PUMP_CYCLE_DURATION = 20

# Large plants or dry soil
PUMP_CYCLE_DURATION = 30
```

**Safety Notes:**
- Always start with shorter durations
- Monitor the first few watering cycles
- Adjust based on how much water your plant actually needs

## 📊 Understanding the Output

When your system runs, you'll see output like this:

```
Position 1 reservoir has water True and moisture value 15/12
Position 1
Completed iteration; soil_moisture's = [15, 0, 0, 0, 0, 0, 0, 0]
Free mem before garbage collection: 89456
Free mem after garbage collection: 91232
```

**What this means:**
- **Position 1**: Your plant's sensor position
- **reservoir has water True**: Water level sensor detects water
- **moisture value 15/12**: Current reading (15) vs threshold (12)
- **Position 1** (on its own line): Pump activated because 15 > 12
- **soil_moisture's = [15, 0, 0, ...]**: Array of all 8 sensor readings

## 🚨 Safety Features

This configuration includes important safety features:

### Water Level Protection
```python
WATER_SENSOR_LOW_ENABLED = True  # Always keep this True
PUMP_WHEN_DRY = False           # Never pump when reservoir is empty
```

### Conservative Pump Settings
```python
PUMP_CYCLE_DURATION = 20        # Start short, increase if needed
```

## 🔧 Troubleshooting

### Plant Not Getting Watered
1. **Check moisture threshold** - may be too low (try increasing the number)
2. **Verify water in reservoir** - ensure water level sensor detects water
3. **Check pump connections** - ensure pump is connected to port 1
4. **Test pump manually**:
   ```python
   from growmax.pump import Pump
   pump = Pump(channel=1)
   pump.dose(1, 5)  # Run for 5 seconds
   ```

### Plant Getting Too Much Water
1. **Reduce pump duration** - try 10-15 seconds
2. **Increase moisture threshold** - higher numbers = drier soil before watering
3. **Check sensor placement** - ensure it's in the root zone, not too deep

### No Moisture Readings
1. **Check sensor connections** - ensure sensor is properly seated
2. **Verify sensor placement** - insert 2-3 inches into soil
3. **Clean sensor probes** - remove any buildup or corrosion

## 🎉 Success Indicators

Your setup is working correctly when:
- ✅ Moisture readings change as soil dries out
- ✅ Pump activates when soil reaches threshold
- ✅ Plant receives appropriate amount of water
- ✅ Water level sensor prevents dry pumping
- ✅ System runs continuously without errors

## 🚀 Next Steps

Once your single plant setup is working well, consider:

### Add WiFi Monitoring
```python
WIFI_ENABLED = True
WIFI_SSID = "YourNetwork"
WIFI_PASSWORD = "YourPassword"
```

### Enable Cloud Logging
```python
OPEN_SENSOR_COLLECT_DATA = True
OPEN_SENSOR_API_KEY = "your-api-key"  # From opensensor.io
```

### Expand to Multiple Plants
See our [Multi-Plant Garden](multi-plant-garden.md) example.

### Add Environmental Sensors
Check out the [Greenhouse Monitoring](greenhouse-monitoring.md) example.

## 📚 Related Examples

- **[Multi-Plant Garden](multi-plant-garden.md)** - Scale up to 8 plants
- **[Smart Indoor Garden](smart-indoor-garden.md)** - Add WiFi and cloud features
- **[Apartment Herb Garden](apartment-herb-garden.md)** - Optimized for herbs

---

**Congratulations! You've automated your first plant! 🌱✨**

*Your plant will now be watered automatically whenever the soil gets dry. Monitor it for the first few days to ensure everything is working perfectly.*
