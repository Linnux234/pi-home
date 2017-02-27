import smbus
import config
import os
import time
#import thread


bus = smbus.SMBus(1)
sections = list(config.sections())


def setup(): 
#	sections = list(config.sections())
	#print(sections)

#	print(len(sections))


	for i in range(len(sections)):
		c = i - 1
		device = config.get(sections[c], 'device')
#		print(device)
		if device == 'expander':
			address = int(config.get(sections[c], 'address'),base=16)
			port = int(config.get(sections[c], 'port'),base=16)
			mode = int(config.get(sections[c], 'mode'),base=16)
			default = config.get(sections[c], 'default')
			bus_define(address, mode)
			set = bus_write(address, port, int(default,base=2))
			if set == 1:
				config.set(sections[c], 'value', default)	
				config.write()
				print("ok")

#			print(port)
#			print(default)
			


def temp():
	print('temp')
	for i in range(len(sections)):
		c = i - 1
		device = config.get(sections[c], 'device')
		if device == 'temp':
			name = config.get(sections[c], 'name')
			should = float(config.get(sections[c], 'should'))
			target = config.get(sections[c], 'target')
			target_address = int(config.get(sections[c], 'target_address'))
			print(should)		
			
			value = config.get_float(sections[c], 'value')
			print(value)
			if value >= should:
				print('genug')
				value = getvalue(target)
				value[target_address] = '0'
				
			elif value < should:
				print('nicht genug') 
				value = getvalue(target)                  
				value[target_address] = '1'
			print(target)
			print(target_address)
			print(value[target_address])
			print(value)
			set = ''.join(value)
			config.set(target, 'should', set)
		#	bus_write(address, port, int(set



     #       temfile.close()



def expander():
	print('expander')
	for i in range(len(sections)):
		c = i - 1
		device = config.get(sections[c], 'device')
		if device == 'expander':
			address = int(config.get(sections[c], 'address'),base=16)
			port = int(config.get(sections[c], 'port'),base=16)
			should = config.get(sections[c], 'should')	
			value = config.get(sections[c], 'value')
			if should == value:
				print("None")
			else:
				set = bus_write(address, port, int(should,base=2))
				if set == 1:
					config.set(sections[c], 'value', should)
					config.write()
					print("Done")

		
def tempvalue():
	
	try:
		tempfile = open('sys/bus/w1/devices/' + str(name) + 'w1_slave')
		line = tempfile.readline()
		if re.match(r"[0-9a-f{2} ){9}: crc=[0-9a-f]{2} YES", line):			
			line = tempfile.readline()
			m =  re.match(r"[0-9a-f{2} ){9}t=([+-]?[0-9]+)",line)
			if m:
				value = float(m.group(2)) / 1000.0
				config.set(section[c], 'value', value)
	except (IOError):
		print("File not found")


def getvalue(section):
	value = config.get(section, 'value')
	print(value)
	bin = list(value)
	print(bin)
	return bin

	

def bus_define(address, mode):
	bus.write_byte_data(address, mode, 0x00)


def bus_write(address, port, value):
#	print(value)

	bus.write_byte_data(address, port, value)
	state = bus_read(address, port)
#	print(state)

	if value == state:
		print("OK")
		return 1
	else:
		print("Error")
		return 0

## Fehlermeldung fürs Webinterface
## Spannung wegschalten??
def bus_read(address, port):
	value = bus.read_byte_data(address,port)
	return value

setup()
temp()
expander()
#print("end")

# thread.start_new_thread()

