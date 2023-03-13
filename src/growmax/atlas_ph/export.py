from machine import UART, Pin
import utime

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

uart.init(9600, bits=8, parity=None, stop=1)
uart.write(''.encode())
uart.write('Export,?\r'.encode())
print(uart.readline())
utime.sleep(1.0)
while True:
    uart.write('Export\r'.encode())
    utime.sleep(1.0)
    print(uart.readline())
