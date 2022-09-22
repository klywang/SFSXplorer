# Program to split binding data from chklig.in file considering the source 
# of binding data. This program splits original chklig.in file into three files:
# chklig_BindingDB.in, chklig_BMOAD.in, and chklig_PDBbind.in.
# Note: Binding affinity values expressed as ranges and with symbols > <
# are not considered as valid data.
#
# To run this code you need to have the chklig.in file in the SAnDReS
# format (Xavier et al., 2016). In the main program you have to specify
# the directory where all .csv files are. These .csv files bring the
# binding affinity data downloaded from the Protein Data Bank. All files
# including this code should be in the same directory.
#
# Reference:
# Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, 
# Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of 
# Docking Results and Development of Scoring Functions. Comb Chem High 
# Throughput Screen. 2016; 19(10): 801–812. 
# PMID: 27686428 DOI: 10.2174/1386207319666160927111347
# https://www.ncbi.nlm.nih.gov/pubmed/27686428
#
# Dr. Walter F. de Azevedo Jr.
# July 26, 2019.
# azevedolab.net
#
# Define Binding_Affinity() class
class Binding_Affinity(object):
    """Class to read csv data and split them for different databases"""

    # Define constructor method
    def __init__(self,project_dir):
        self.project_dir = project_dir

    # Define read_chklig() method
    def read_chklig(self):
        """Method to read chklig.in file"""
        # Import library
        import csv

        foo1 = open(self.project_dir+"chklig.in","r")
        self.csv001 = csv.reader(foo1)

        # Get first line
        for line in self.csv001:
            aux_line0 = str(line)
            aux_line1 = aux_line0.replace("[","")
            aux_line2 = aux_line1.replace("'","")
            self.first_line = aux_line2.replace("]","")
            break

    # Define read_BindingDB() method
    def read_BindingDB(self):
        """Method to read Binding DB data"""

        # Import library
        import csv

        # Function to reverse string
        def reverse(s):
            str = ""
            for i in s:
                str = i + str
            return str

        # Set up empty list
        self.list_out_BDB = []

        # Looping through self.csv001
        for line0 in self.csv001:
            if "CHKLIG" in line0:

                # Read csv file with binding affinity data
                foo2 = open(self.project_dir+line0[1].lower()+".csv","r")
                self.csv002 = csv.reader(foo2)

                # Set up index_0 to 0
                index_ = 0

                # Looping through self.csv002
                for line1 in self.csv002:
                    for line2 in line1:
                        if "(BDB)" in str(line2):
                            index_BDB = line2.index("(BDB)")

                            if "#" in line2[index_:index_BDB]:
                                count = 0
                                for line3 in reverse(line2[:index_BDB]):
                                    count += 1
                                    if line3 == "#":
                                        index_ = index_BDB - count+1
                                        break

                            if "-" not in line2[index_+1:index_BDB] and \
                            "<" not in line2[index_:index_BDB]:
                                # print(line0[1],line2[index_:index_BDB])

                                # Some editing
                                line_out = str(line0[0])+","+str(line0[1])\
                                +","+str(line0[2])+","+str(line0[3])\
                                +","+str(line0[4])+","+line2[index_:index_BDB]
                                print(line_out)
                                self.list_out_BDB.append(str(line_out))
                                break


    # Define read_BMOAD() method
    def read_BMOAD(self):
        """Method to read BMOAD data"""

        # Import library
        import csv

        # Function to reverse string
        def reverse(s):
            str = ""
            for i in s:
                str = i + str
            return str

        # Set up empty list
        self.list_out_BMOAD = []

        # Looping through self.csv001
        for line0 in self.csv001:
            if "CHKLIG" in line0:

                # Read csv file with binding affinity data
                foo_BMOAD = open(self.project_dir+line0[1].lower()+".csv","r")
                self.csv_BMOAD = csv.reader(foo_BMOAD)

                # Set up index_0 to 0
                index_ = 0

                # Looping through self.csv_BMOAD
                for line1 in self.csv_BMOAD:
                    for line2 in line1:
                        if "(BMOAD_" in str(line2):
                            index_BMOAD = line2.index("(BMOAD_")

                            if "#" in line2[index_:index_BMOAD]:
                                count = 0
                                for line3 in reverse(line2[:index_BMOAD]):
                                    count += 1
                                    if line3 == "#":
                                        index_ = index_BMOAD - count+1
                                        break

                            if "-" not in line2[index_+1:index_BMOAD] and \
                            "<" not in line2[index_:index_BMOAD]:
                                
                                # Some editing
                                line_out = str(line0[0])+","+str(line0[1])\
                                +","+str(line0[2])+","+str(line0[3])\
                                +","+str(line0[4])+","+line2[index_:index_BMOAD]
                                print(line_out)
                                self.list_out_BMOAD.append(str(line_out))
                                break


    # Define read_PDBbind() method
    def read_PDBbind(self):
        """Method to read PDBbind data"""

        # Import library
        import csv

        # Function to reverse string
        def reverse(s):
            str = ""
            for i in s:
                str = i + str
            return str

        # Set up empty list
        self.list_out_PDBbind = []

        # Looping through self.csv001
        for line0 in self.csv001:
            if "CHKLIG" in line0:

                # Read csv file with binding affinity data
                foo_PDBbind = open(self.project_dir+line0[1].lower()+".csv","r")
                self.csv_PDBbind = csv.reader(foo_PDBbind)

                # Set up index_0 to 0
                index_ = 0

                # Looping through self.csv_PDBbind
                for line1 in self.csv_PDBbind:
                    for line2 in line1:
                        if "(PDBbind)" in str(line2):
                            index_PDBbind = line2.index("(PDBbind)")

                            if "#" in line2[index_:index_PDBbind]:
                                count = 0
                                for line3 in reverse(line2[:index_PDBbind]):
                                    count += 1
                                    if line3 == "#":
                                        index_ = index_PDBbind - count+1
                                        break

                            if "-" not in line2[index_+1:index_PDBbind] and \
                            "<" not in line2[index_:index_PDBbind]:
                                
                                # Some editing
                                line_out = str(line0[0])+","+str(line0[1])\
                                +","+str(line0[2])+","+str(line0[3])\
                                +","+str(line0[4])+","\
                                +line2[index_:index_PDBbind]
                                print(line_out)
                                self.list_out_PDBbind.append(str(line_out))
                                break
        
    # Define write_BindingDB() method
    def write_BindingDB(self):
        """Method to write a previously read binding affinity data(BindingDB)"""
        
        foo3 = open(self.project_dir+"chklig_BindingDB.in","w")
        foo3.write(self.first_line+"\n")
        for line in self.list_out_BDB:
            print(line)
            foo3.write(line+"\n")

        foo3.close()
        print("\n\nNumber of structures with BindingDB data: ",
        len(self.list_out_BDB))

    # Define write_BMOAD() method
    def write_BMOAD(self):
        """Method to write a previously read binding affinity data (BMOAD)"""
        
        foo3 = open(self.project_dir+"chklig_BMOAD.in","w")
        foo3.write(self.first_line+"\n")
        for line in self.list_out_BMOAD:
            print(line)
            foo3.write(line+"\n")

        foo3.close()
        print("\n\nNumber of structures with BMOAD data: ",
        len(self.list_out_BMOAD))
    
    # Define write_PDBbind() method
    def write_PDBbind(self):
        """Method to write a previously read binding affinity data (PDBbind)"""
        
        foo3 = open(self.project_dir+"chklig_PDBbind.in","w")
        foo3.write(self.first_line+"\n")
        for line in self.list_out_PDBbind:
            print(line)
            foo3.write(line+"\n")

        foo3.close()
        print("\n\nNumber of structures with PDBbind data: ",
        len(self.list_out_PDBbind))