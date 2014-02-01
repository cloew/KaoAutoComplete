from python_package import PythonPackage

from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.Python.python_helper import IsPythonDirectory

import os, sys

def main(args):
    """ Run the main file """
    packages = []
    importPaths = sys.path
    
    for path in importPaths:
        if IsDirectory(path):
            for filename in os.listdir(path):
                filename = os.path.join(path, filename)
                if IsPythonDirectory(filename):
                    packages.append(PythonPackage(filename))
                # elif os.path.splitext(filename)[1] == '.py':
                    # print "File is a Python File:",  os.path.basename(filename)
                    
                    
    packages.sort()
    for package in packages:
        print package

if __name__ == "__main__":
    main(sys.argv[1:])