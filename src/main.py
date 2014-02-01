from python_package import PythonPackage

from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.Python.python_helper import IsPythonDirectory

import os, sys

def findPackage(name, packages):
    """ Find the package with the given name """
    pieces = name.split('.')
    for piece in pieces[:-1]:
        if piece in packages:
            packages = packages[piece].childPackages
        else:
            return None
    
    if pieces[-1] in packages:
        return packages[pieces[-1]]
    else:
        return None

def loadPythonPackages(directory, parent=None):
    """ Load Python Packages in the given directory """
    packages = {}
    for filename in os.listdir(directory):
        filename = os.path.join(directory, filename)
        if IsPythonDirectory(filename):
            package = PythonPackage(filename, parent=parent)
            if parent is not None:
                parent.addChildPackage(package)
            packages[package.name] = package
            loadPythonPackages(filename, parent=package)
    return packages

def main(args):
    """ Run the main file """
    packages = {}
    importPaths = sys.path
    
    for path in importPaths:
        if IsDirectory(path):
            packages.update(loadPythonPackages(path))
                # elif os.path.splitext(filename)[1] == '.py':
                    # print "File is a Python File:",  os.path.basename(filename)
                    
    name = args[0]
    package = findPackage(name, packages)
    if package is not None:
        print "Package:", package, "has child packages"
        for child in package.childPackages:
            print child
    else:
        print "Couldn't find package:", name

if __name__ == "__main__":
    main(sys.argv[1:])