import smbus
import time
import sys
from flask import Flask, render_template

app = Flask(__name__)

bus = smbus.SMBus(1)
address = 0x48

@app.route("/")
def index():
	return render_template('yl40-ajax.html')

@app.route("/ain/<int:ain_addr>", methods=['POST', 'GET'])
def analog_in(ain_addr):
	#192.168.0.9:5000/ain/0
	bus.write_byte(address, 0x40 + ain_addr)
	bus.read_byte(address)
	aread = bus.read_byte(address)
	return '%d' % (aread)

@app.route("/aout/<int:val>", methods=['POST','GET'])
def analog_out(val):
	#192.168.0.9:5000/aout/0
	bus.write_byte_data(address, 0x40, val)
	return '%d' % (val)

@app.route("/motor/<int:angle>", methods=['POST', 'GET'])
def motor(angle):
	print angle
	return '%d' % (angle)


if __name__ == "__main__":
	app.debug=True
	app.run(host="0.0.0.0")

