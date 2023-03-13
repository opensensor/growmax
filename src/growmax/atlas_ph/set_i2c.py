from machine import UART, Pin

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

uart.init(9600, bits=8, parity=None, stop=1)
uart.write(''.encode())
uart.write('I2C,99\r'.encode())
