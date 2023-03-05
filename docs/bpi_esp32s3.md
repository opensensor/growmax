# Banana PI ESP32S3 Setup Instructions

The [BPI-PicoW-S3](https://wiki.banana-pi.org/BPI-PicoW-S3) is a pico form-factor ESP32S3 MCU that is compatible with the growmax boards.

The device ships with CircuitPython and to get micropython setup to work with growmax requires a few steps.


## MCU Setup

The MCU setup is a bit more complicated than a standard RP2040 MCU, but with a bit of work it's no problem.

It is more fidgety to get micropython setup, in part because there is no button for the boot pins, so you have to hold a wire over the two BOOTO pads when plugging in the device.
Also, the uf2 drag-and-drop is broken and leads to file corruption, so use of esptools is required.

The steps are to erase the device and flash it with the appropriate micropython bin file using esptool.

## Clone esptool and download micropython .bin file

`esptool` is available on GitHub:  https://github.com/espressif/esptool

Cloning a git repository is outside the scope of this document, but plenty of good resources exist.

The appropriate micropython .bin file can be downloaded here:  https://micropython.org/download/GENERIC_S3/


## Erase device and install micropython

Plug in the device with the BOOTO pas shorted (I used a wire for this, it might take a few tries)

These instructions assume windows, for linux it would be a different port and determining which port would be different.

To determine the port for Windows open Device Manager and look at the Ports COM.  
It helps to check this before and after you plug in the banana-pi device to determine which COM port shows up as new.

Once you have `esptool` and know your COM port, erase the device flash replacing `COM10` with your port number:

    $ python esptool.py --baud 9600 --port COM10 --chip esp32s3 erase_flash

Once you achieve success erasing the device, you'll want to flash it with the appropriate micropython .bin file you downloaded in the prior step.

    $ python esptool.py --port COM10 write_flash 0x1000 ~/Downloads/GENERIC_S3-20220618-v1.19.1.uf2
    esptool.py v4.6-dev
    Serial port COM10
    Connecting...
    Detecting chip type... ESP32-S3
    Chip is ESP32-S3 (revision v0.1)
    Features: WiFi, BLE
    Crystal is 40MHz
    MAC: 48:27:e2:0d:7b:00
    Uploading stub...
    Running stub...
    Stub running...
    Configuring flash size...
    Flash will be erased from 0x00001000 to 0x0028ffff...
    Compressed 2682368 bytes to 987895...
    Writing at 0x0013f02a... (47 %)
    Wrote 2682368 bytes (987895 compressed) at 0x00001000 in 17.9 seconds (effective 1196.2 kbit/s)...
    Hash of data verified.
    
    Leaving...
    Hard resetting via RTS pin...


## Installing growmax in Thonny IDE

At this point you should be able to switch the Thonny interpreter to generic micropython esp32 and install `growmax` from pypi the same way you would for the rp2040 via `Tools -> Manage Packages`.
