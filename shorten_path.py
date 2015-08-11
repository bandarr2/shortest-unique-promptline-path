#!/usr/bin/env python
#test1
# Import
import sys
import os
import subprocess

def main(argv):
    # Read the path value (argument)
    input_path = argv[0]

    # Split path
    path_splits = input_path.split('/')
    
    # Delete first split (empty) 
    del path_splits[0]

    # Loop though path splits
    for split in xrange(0, len(path_splits) ):
        # Create the intermediate path
        temp_path =  "/" + "/".join(path_splits[0:split])
        
        #Get list of directories in the intermediate path
        dirs = next(os.walk(temp_path))[1]
        
        print "Exploring Dir: " + temp_path
        print "That Contains: ", dirs
        print "To Compare with: " + path_splits[split]
        print "----------------------------------------------"
    # Test Output

# Create function to get shortest unique string
if __name__ == "__main__":
    main(sys.argv[1:])
