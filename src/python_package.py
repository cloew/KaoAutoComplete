import os

class PythonPackage:
    """ Represents a Python Package """
    
    def __init__(self, path, parent=None):
        """ Initialize the Python Package with the path to it """
        self.parent = parent
        self.path = path
        self.name = os.path.basename(path)
        
        self.childPackages = {}
        
    def addChildPackage(self, child):
        """ Add child """
        self.childPackages[child.name] = child
        
    @property
    def package_name(self):
        """ Return the qualified package name """
        if self.parent is None:
            return self.name
        else:
            return "{0}.{1}".format(self.parent.package_name, self.name)
        
    def __cmp__(self, other):
        """ Compare self to other """
        if self.package_name == other.package_name:
            return 0
        elif self.package_name < other.package_name:
            return -1
        else:
            return 1
        
    def __repr__(self):
        """ Return the Package String Representation """
        return self.package_name