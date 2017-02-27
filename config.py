import sys
import getopt
import configparser

args = list(sys.argv)



cfg = open('test.cfg', 'r+')
#cfgfile = 'test.cfg'
settings = configparser.ConfigParser()
settings._interpolation = configparser.ExtendedInterpolation()
settings.read('test.cfg')


#configs = list(settings.sections())
#print(len(configs))

def sections():
	return (settings.sections())



def get(section, param):
	return (settings.get(section, param))


def get_float(section, param):
	return (settings.getfloat(section, param))



def add_section(section):
	settings.add_section(section)


def write():
	settings.write(open('test.cfg', 'w'))


def set(section, param, value):
	settings.set(section, param, value)


def remove(section):
	settings.remove_section(section)
	


def create(section):
	add_section(section)
	device = input('Device: ')
	set(section, 'device', device)
	if device == 'expander':
		address = input('Address: ')
		set(section, 'address', address)
		port = input('Port: ')
		set(section, 'port', port)
		mode = input('Mode: ')
		set(section, 'mode', mode)


		for i in range(8):
			name = input('Name' + str(i) + ': ')
			set(section, 'name' + str(i), name)
	else:

		address = input('Address: ')
		set(section, 'address', address)
		name = input('Name: ')
		set(section, 'name', name)

		target = input('Target: ')
		set(section, 'target', target)

		target_address = input('Target_Address: ')
		set(section, 'target_address', target_address)




	default = input('Default: ')
	set(section, 'default', default)

	should = input('Should: ')
	set(section, 'should', should)	
	set(section, 'value', '')





if len(args) > 1:
	if args[1] == '-add':
		add_section(args[2])
		write()	
	elif args[1] == '-list':
		print(sections())
	elif args[1] == '-get':
		print(get(args[2], args[3]))
	elif args[1] == '-set':
		set(args[2], args[3], args[4])
		write()
	elif args[1] == '-remove':
		remove(args[2])
		write()
	elif args[1] == '-create':
		create(args[2])
		write()
	elif args[1] == '-get_float':
		print(get_float(args[2], args[3]))


#print(args)
#print(args[1])
