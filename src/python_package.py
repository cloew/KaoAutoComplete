import os

class PythonPackage:
    """ Represents a Python Package """
    
    def __init__(self, path):
        """ Initialize the Python Package with the path to it """
        self.path = path
        self.name = os.path.basename(path)
        
    def __cmp__(self, other):
        """ Compare self to other """
        if self.name == other.name:
            return 0
        elif self.name < other.name:
            return -1
        else:
            return 1
        
    def __repr__(self):
        """ Return the Package String Representation """
        return self.name