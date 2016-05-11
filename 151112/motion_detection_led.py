import smbus
import time
import sys

bus = smbus.SMBus(1)
address = 0x48

if len(sys.argv) == 2:
	i = int(sys.argv[1])
	input_addr = 0x40 + i
else:
	input_addr = 0x40

while True:
	bus.write_byte(address, input_addr)
	bus.read_byte(address)
	aread = bus.read_byte(address)
	print aread
	bus.write_byte_data(address, 0x40, aread)
	time.sleep(0.2)

