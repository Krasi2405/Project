from directory import *
from Directories import *
import re


			
def get_type(argument):
	print(type(argument))

name = "Krasi"
# name = input("What is your name")

home = Directory(name, name)
current_directory = home
terminal_sign = "{}#>".format(current_directory.path)

while True:
	command = ""
	needed_list = []
	optionals_list = []
	cmd = input(terminal_sign)
	a = re.search(r"(?P<command>\w+)", cmd)
	b = re.search(r"(?P<needed> (\w+)+)", cmd)
	c = re.search(r"(?P<optional> (\D+)+)", cmd)
	command = a.group("command")
	try:
		needed_list = b.group("needed").split(" ")
		needed_list.pop(0)
		optionals_list = c.group("optional").split(" ")
		optionals_list.pop(0)
	except AttributeError:
		pass
		
	for x in needed_list:
		for y in optionals_list:
			if x == y:
				del optionals_list[optionals_list.index(y)]

	if command == "mkdir":
		current_directory.add_directory(needed_list[0])
	elif command == "ls":
		current_directory.print_directories()
	elif command == "cd":
		print(needed_list)
		current_directory = current_directory.get_directory(current_directory, needed_list[0])
		terminal_sign = "{}#>".format(current_directory.path)
		
		
	