from Directories import *
from linux_file_koito_e_razlichen_ot_windows_file import *

class Directory:
	
	def __init__(self, name, path, parent_directory = None):
		self.directories = Directories()
		self.file_list = []
		self.name = name
		self.path = path
		self.parent_directory = parent_directory
		
	def __str__(self):
		return self.name
	
	def print_contents(self):
		contents = []
		for x in self.directories.directory_list:
			contents.append(x.name)
		for x in self.file_list:
			contents.append("{}.{}".format(x.name, x.extension))
		print('  '.join(contents))	
		
	def add_directory(self, name):
		self.directories.add_directory(Directory(name, "{}\\{}".format(self.path, name),self))
		
	def add_file(self, name):
		self.file_list.append(File(name))
		
	def get_directory(self, name):
		for x in self.directories.directory_list:
			if x.name == name:
				return x
				
	