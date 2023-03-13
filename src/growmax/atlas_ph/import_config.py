from machine import UART, Pin
import utime

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

uart.init(9600, bits=8, parity=None, stop=1)
uart.write(''.encode())
# Use your config values from the export command in place of these values
uart.write('Import,A0990D466666\r'.encode())
uart.write('Import,46C3842A3EC3\r'.encode())
uart.write('Import,010102000080\r'.encode())
uart.write('Import,400000E040F6\r'.encode())
uart.write('Import,282041019458\r'.encode())
utime.sleep(1.0)

print(uart.readline())
