from Directories import *

class Directory:
	
	def __init__(self, name, path, parent_directory = None):
		self.directories = Directories()
		self.file_list = []
		self.name = name
		self.path = path
		self.parent_directory = parent_directory
		
	def __str__(self):
		return self.name
	
	def print_directories(self):
		directories = []
		for x in self.directories.directory_list:
			directories.append(x.name)
		
		print(' '.join(directories))
		
	def add_directory(self, name):
		self.directories.add_directory(Directory(name, "{}\\{}".format(self.path, name),self))
		
	def get_directory(self, name):
		for x in self.directories.directory_list:
			if x.name == name:
				return x
				
	