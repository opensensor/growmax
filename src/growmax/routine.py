import gc
import random
import utime
from machine import Pin

from growmax.moisture import Moisture
from growmax.pump import Pump
from growmax.utils.configs import get_moisture_threshold_for_position
from growmax.utils.displays import boot_sequence, display_basic_stats, display_ph_reading
from growmax.utils.water import statistically_has_water
from growmax.utils.wifi import ensure_wifi_connected

# User's config file
import config

# set the random seed, so messages are randomized
random.seed()


def main():
    boot_sequence()

    water_sensor = None
    if config.WATER_SENSOR_LOW_ENABLED:
        water_sensor = Pin(config.WATER_SENSOR_LOW, Pin.IN, Pin.PULL_DOWN)
    scd40x = None
    atlas_ph = None

    soil_sensors = [Moisture(channel=1), Moisture(channel=2), Moisture(channel=3), Moisture(channel=4),
                    Moisture(channel=5), Moisture(channel=6), Moisture(channel=7), Moisture(channel=8)]
    pumps = [Pump(channel=1), Pump(channel=2), Pump(channel=3), Pump(channel=4),
             Pump(channel=5), Pump(channel=6), Pump(channel=7), Pump(channel=8)]

    while True:
        utime.sleep(5.0)
        try:
            ensure_wifi_connected()
            utime.sleep(0.5)
        except Exception:
            # Potentially no wi-fi
            pass

        if config.ADAFRUIT_SCD4X_ENABLED and scd40x is None:
            from growmax.utils.sensors import init_adafruit_scd4x
            scd40x = init_adafruit_scd4x(config.ADAFRUIT_SCD4X_I2C_CHANNEL)

        if hasattr(config, "ATLAS_PH_METER_ENABLED") and config.ATLAS_PH_METER_ENABLED:
            from growmax.atlas_ph.i2c import AtlasPHI2C
            atlas_ph = AtlasPHI2C(config.ATLAS_PH_I2C_CHANNEL)

        soil_moistures = []
        for position, soil_sensor in enumerate(soil_sensors):
            try:
                pump_position = str(position + 1)
                soil_moisture = soil_sensor.moisture
                soil_moistures.append(soil_moisture)
                has_water = water_sensor and statistically_has_water(water_sensor)
                moisture_config = get_moisture_threshold_for_position(position)
                print("Position ", pump_position,
                      " reservoir has water ", has_water,
                      " and moisture value ", soil_moisture, "/", moisture_config)
                display_basic_stats(has_water, pump_position, soil_moisture, moisture_config)
                if (config.PUMP_WHEN_DRY or has_water) and soil_moisture >= moisture_config:
                    print("position: ", pump_position)
                    pumps[position].dose(1, config.PUMP_CYCLE_DURATION)
                utime.sleep(2)
            except Exception as e:
                print("Exception: ", str(e))

        if scd40x:
            if config.OPEN_SENSOR_COLLECT_DATA:
                from growmax.utils.api import read_and_report_adafruit_scd4x
                read_and_report_adafruit_scd4x(scd40x)
            else:
                from growmax.utils.sensors import read_adafruit_scd4x
                read_adafruit_scd4x(scd40x)
        if atlas_ph:
            ph_reading = atlas_ph.obtain_ph_reading()
            display_ph_reading(ph_reading)
            utime.sleep(3)

        print("Completed iteration; soil_moisture's = ", str(soil_moistures))
        print("Free mem before garbage collection: ", str(gc.mem_free()))
        gc.collect()
        print("Free mem after garbage collection: ", str(gc.mem_free()))
