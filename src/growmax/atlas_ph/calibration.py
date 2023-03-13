from machine import UART, Pin
import utime

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

uart.init(9600, bits=8, parity=None, stop=1)
uart.write(''.encode())
uart.write('Factory\r'.encode())

utime.sleep(5.0)

# This routine is meant to be used with the device in default UART mode.
calibrated_mid = False
while not calibrated_mid:
    for x in range(0, 30):
        print(uart.readline())
        utime.sleep(1.0)
    print("Calibrate Mid?")
    calibrate = input()
    if calibrate == "Y":
        calibrated_mid = True

uart.write('Cal,mid,7.00\r'.encode())
utime.sleep(2.0)


calibrated_low = False
while not calibrated_low:
    for x in range(0, 30):
        print(uart.readline())
        utime.sleep(1.0)
    print("Calibrate Low?")
    calibrate = input()
    if calibrate == "Y":
        calibrated_low = True

uart.write('Cal,low,4.00\r'.encode())
utime.sleep(2.0)


calibrated_high = False
while not calibrated_high:
    for x in range(0, 30):
        print(uart.readline())
        utime.sleep(1.0)
    print("Calibrate High?")
    calibrate = input()
    if calibrate == "Y":
        calibrated_high = True

uart.write('Cal,high,10.00\r'.encode())
utime.sleep(2.0)


while True:  # Print readings continuously at the end
    print(uart.readline())
    utime.sleep(1.0)
