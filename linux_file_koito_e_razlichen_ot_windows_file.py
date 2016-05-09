import re

class File:
    
    def __init__(self, file_name):
        a = re.match(r"(?P<name>\S+)\.(?P<extension>\w+)", file_name)
        self.name = a.group("name")
        self.extension = a.group("extension")
        self.contents = ""
        