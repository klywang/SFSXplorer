#!/usr/bin/env python
# Program to copy dataset taking only directories listed in the chklig.in file
#
# Dr. Walter F. de Azevedo Jr.
# https://azevedolab.net
# Porto Alegre, April 12th 2019.
#
# Define class CopyDatset()
class CopyDataset(object):
    """A class to copy dataset"""	

    # Define the constructor method
    def __init__(self,chklig_in,src,dest):
        """Constructor method"""

        # Set up attributes
        self.chklig_in = chklig_in
        self.src = src
        self.dest = dest
        
    # Define copy_dir() method
    def copy_dir(self):
        """Method to copy directories listed in chklig.in"""

        # Import libraries
        import csv
        import shutil
		
        # Open chklig.in
        self.fo0 = open(self.chklig_in,"r")
        self.csv0 = csv.reader(self.fo0)
        
        # Assign zero to count_dir
        count_dir = 0
        
        # Looping through csv0
        for line in self.csv0:
    
            # Check "CHKLIG" keywork to get ligand data
            if line[0] == "CHKLIG":
                print("Copying directory "+str(line[1])+"...")
                my_src = self.src+"/"+str(line[1])+"/"
                my_dest = self.dest+"/"+str(line[1])+"/"
                shutil.copytree(my_src,my_dest, symlinks=False, ignore=None)
                count_dir += 1
        
        # Close file
        self.fo0.close()
        
        # Show message
        print("Number of directories copied to "+self.dest,count_dir)
        print("\nDone!")