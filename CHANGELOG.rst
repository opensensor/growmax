Growmax v1.1.7
==============================
* Add initial support for Atlas Scientific digital pH meters. Plus some general refactoring.

Growmax v1.1.6
==============================
* Add optional support for alternative MCU ESP32S3_BPI https://wiki.banana-pi.org/BPI-PicoW-S3 with config option ``GROWMAX_MCU``.

Growmax v1.1.5
==============================
* Move networking logic into ``utils.wifi`` and made the ``routine.main`` more safe for devices without networking support.

Growmax v1.1.4
==============================
* Add support for sh1107 I2C displays -- set the config ``DISPLAY = "SH1107_I2C"`` to use this kind of display.

Growmax v1.1.3
==============================
* Reduce usage of f-strings to improve memory usage.

Growmax v1.1.2
==============================
* Add 5 second sleep in ``main`` routine to provide enough time to get accurate moisture readings during fast loop cycles.

Growmax v1.1.1
==============================
* Add try/except handling around new display logic, along with additional garbage collection.

Growmax v1.1.0
==============================
* Support for I2C displays and supporting switches to enable/disable the display.
* Initial supported display: ssd1327 (Ex: Adafruit 4741)
* Renamed ``main.py`` to ``routine.py`` to avoid issues with having two files opened named ``main.py`` in Thonny IDE.
* Swap default values for ``WATER_SENSOR_HIGH`` and ``WATER_SENSOR_LOW`` to better match physical orientation of the board.

Growmax v1.0.9
==============================
* Improve measuring accuracy of the Grow moisture sensor ports by increasing the cycle measurement time.

Growmax v1.0.8
==============================
* No significant changes (testing pypi publish hook).

Growmax v1.0.7
==============================
* Corrected import of ``ujson`` -- required to be installed from pypi, when using opensensor API data reporting.

Growmax v1.0.6
==============================
* Safety enhancements and trying to resolve issue with adafruit SCD-4x sensor and long I2C cable on wall power.

Growmax v1.0.5
==============================
* Adjusted opensensor.io API for CO2 parameter

Growmax v1.0.4
==============================
* Initial support for adafruit SCD-4x sensors.
* Add support for data reporting on adafruit scd4x.

Growmax v1.0.3
==============================
* Allows configuring a list of moisture sensor values as an array (different pump thresholds per sensor).

Growmax v1.0.2
==============================
* Importing from ``growmax.main`` no longer invokes the main routine as a side effect.
* Adding initial README.

Growmax v1.0.1
==============================
* Corrected imports

Growmax v1.0.0
==============================
* Initial Release