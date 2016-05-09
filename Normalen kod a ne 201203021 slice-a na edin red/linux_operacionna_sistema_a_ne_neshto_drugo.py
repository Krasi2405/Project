from directory import *
from Directories import *
import re


			
def get_type(argument):
	print(type(argument))

name = "Krasi"
# name = input("What is your name")
home = Directory(name, "\\{}".format(name))
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
	except:
		needed_list = [""]
	try:
		optionals_list = c.group("optional").split(" ")
	except:
		optionals_list = [""]
	
	
	for x in needed_list:
		if command == x or x == "":
			needed_list.remove(x)
			
	for x in optionals_list:
		if command == x or x == "":
			optionals_list.remove(x)
	
	for x in needed_list:
		for y in optionals_list:
			if x == y:
				del optionals_list[optionals_list.index(y)]
	
	# Moving around and looking into the directories.
	if command == "mkdir":
		current_directory.add_directory(needed_list[0])
	elif command == "ls":
		current_directory.print_contents()
	elif command == "cd":
		try:
			if optionals_list[0] == "../":
				current_directory = current_directory.parent_directory
		except IndexError:
			current_directory = current_directory.get_directory(needed_list[0])
		terminal_sign = "{}#>".format(current_directory.path)
	# Working with files.
	elif command == "touch":
		current_directory.add_file(optionals_list[0])
	else:
		print("Command not recognized.")
		
		
	