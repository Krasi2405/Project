from Directories import *

class Directory:
	
	def __init__(self, name, path):
		self.directories = Directories()
		self.file_list = []
		self.name = name
		self.path = path
		
	def __str__(self):
		return self.name
	
	def print_directories(self):
		directories = []
		for x in self.directories.directory_list:
			directories.append(x.name)
		
		print(' '.join(directories))
		
	def add_directory(self, name):
		self.directories.add_directory(Directory(name, "{}\\{}".format(self.path, self.name)))
		
	def get_directory(self, a_directory, name):
		for x in a_directory.directories.directory_list:
			if x.name == name:
				return x
	