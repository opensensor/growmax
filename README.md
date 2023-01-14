# growmax
Micropython routines for GrowMax plant watering automation boards by OpenSensor.io


# Installation
To install the ``growmax`` package on a Pico or Pico W, first install the appropriate firmware for Micropython that is for your device.
* Pico: https://micropython.org/download/rp2-pico/
* Pico W:  https://micropython.org/download/rp2-pico-w/

Ensure that you have Thonny IDE installed; for more information visit:  https://thonny.org/

Launch Thonny IDE with your device connected.

Go to Tools -> Manage Packages and search for ``growmax``
Install the latest version of ``growmax``.

Now create a new file and save it to your device as ``main.py``
In this file invoke the main routine of growmax:
```
from growmax.main import main

main() 
```

Next you need to create your config file.
* Open the sample config file from the pico device, it is at ``/lib/growmax/config.py``
* Now save this file to the root of your pico device as ``config.py``
* Modify any relevant config values to suit your needs for automatic plant watering.

# Configuration

* `WATER_SENSOR_LOW_ENABLED` Defaults `True`. Checks the low water level sensor before invoking the pumps.  Note: as a safety precaution, when this is disabled the pumps will not turn on to prevent pump burn out.
* `WATER_SENSOR_LOW` Defaults `21`.  Which GPIO port has the Optomax water level sensor for low levels?  Supported `growmax` board ports are 21 and 22 

# Verification
Test the routine by running the created ``main.py`` in Thonny IDE.  You should see output in the terminal and the program should not have any errors.

Once you have verified the pico runs the code properly, your device is now plug and play ready.  
Simply supply 5V USB voltage by plugging the pico growmax board into a common USB wall wart and the pico will boot the ``main`` routine.

# Power and Safety
The ``growmax`` is designed with the pico power requirements in mind.   When modifying the application logic, it is important to realize:
* Pico max current is ~300 mA; when using the onboard pump ports and mosfets: ensure the pumps you source are 5V and draw less than 200 mA.
* Should you need to control higher powered pumps and equipment, it is recommended to pair with an I2C relay board for such use cases.
* The pico operates at 3.3V logic levels, however the pumps and water sensor ports are powered by the 5V VSYS.  
* The water sensor ports are designed for the Optomax liquid sensor and have voltage dividers for an expected 4V -> 3.3V input back to the pico. 