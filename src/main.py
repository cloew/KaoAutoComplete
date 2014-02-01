from python_package import PythonPackage

from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.Python.python_helper import IsPythonDirectory

import os, sys

def loadPythonPackages(directory, parent=None):
    """ Load Python Packages in the given directory """
    packages = []
    for filename in os.listdir(directory):
        filename = os.path.join(directory, filename)
        if IsPythonDirectory(filename):
            package = PythonPackage(filename, parent=parent)
            packages.append(package)
            packages += loadPythonPackages(filename, parent=package)
    return packages

def main(args):
    """ Run the main file """
    packages = []
    importPaths = sys.path
    
    for path in importPaths:
        if IsDirectory(path):
            packages += loadPythonPackages(path)
                # elif os.path.splitext(filename)[1] == '.py':
                    # print "File is a Python File:",  os.path.basename(filename)
                    
                    
    packages.sort()
    for package in packages:
        print package

if __name__ == "__main__":
    main(sys.argv[1:])