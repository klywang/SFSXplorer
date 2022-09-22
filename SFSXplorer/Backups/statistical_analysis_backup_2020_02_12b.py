#!/usr/bin/python
# 
# Walter F. de Azevedo Jr.
# February 8, 2019
# https://azevedolab.net
#
# Reference:
# Morris G, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A. Automated docking using a
# Lamarckian genetic algorithm and an empirical binding free energy function. J Comput Chem. 1998; # 19:1639-1662. 
#
# Define StatsAnalysis class
class StatsAnalysis(object):
    """Class to carry out statistical analysis of energy terms"""

    # Define constructor method
    def __init__(self,file_in,file_out,dir_in,dir_out,n_vars):
        """Constructor method"""

        # Set up attributes
        self.file_in = file_in
        self.file_out = file_out
        self.dir_in = dir_in
        self.dir_out = dir_out
        self.n_vars = n_vars

    # Define read_headers() method
    def read_headers(self):
        """Method to read headers from a CSV file"""

        # Import library
        import csv

        # Open CSV file
        fo1 = open(self.dir_in+self.file_in)
        csv1 = csv.reader(fo1)

        # Read first line
        for line in csv1:
            self.headers = line
            break

        # Close file
        fo1.close()

    # Define read_it() method
    def read_it(self):
        """Method to read CSV file and return arrays"""

        # Import library
        import numpy as np

        # Open CSV file
        pie_in = np.genfromtxt(self.dir_in+self.file_in, skip_header = 1, delimiter=",")

        # Get rid of the pie's first slice
        #pie1 = np.transpose(pie_in[:,1:]) # You transpose it and slice it row and column
        pie1 = pie_in[:,1:]   # Without transposing it

        # Get the number of rows and columns
        n_rows, n_cols = pie1.shape

        # Set up a zeros array
        self.pie2go = np.zeros((n_rows, n_cols))

        # Slicing the pie1
        for c in range(n_cols):
            for r in range(n_rows):
                self.pie2go[r,c] = pie1[r,c]
    
    # Define sort_it() method
    def sort_it(self,my_array,n_vars):
        """Method to sort array"""
        
        # Import library
        import numpy as np
        
        # Set up empty list with explanatory variables
        self.exp_var_headers = []
        
        # Set up empty list for indeces
        index_out = []
        
        # To convert to absolute values first
        abs_array = np.absolute(my_array)
        
        sorted_array0 = np.sort(abs_array)  # Absolute values
        sorted_array1 = sorted_array0[::-1] # Invert it
        
        # Get explanatory variable headers with highest Spearaman's correlation
        for i in range(1,self.n_vars+1):
            aux = np.where(abs_array == sorted_array1[i])
            self.exp_var_headers.append(self.headers[int(aux[0])+1])

        # Get indeces for explanatory variables
        for line1 in self.exp_var_headers:
            for line2 in self.headers:
                if line1 == line2:
                    index_out.append(self.headers.index(line1))
                    break
        
        # Open file to store columns of selected explanatory variables
        fo1 = open("best.csv","w")
        
        # Set up empty string for line_out
        line_out = ""
        
        # Getting columns of selected explanatory variables
        for i in index_out:
        #for j in range(len(self.pie2go[:,i-1:i])):
            #print(self.headers[i])
            #line_out += self.headers[i]
            # Get explanatory variable data
            for j in range(len(self.pie2go[:,i-1:i])):
                for k in range(len(self.pie2go[j-1:j,:])):
            #for i in index_out:
                #print(float(self.pie2go[j,i-1:i]))
                    line_out += ","+str(self.pie2go[k,i-1:i])
            #line_out += line_out+"\n"
            #line_out = line_out.replace("[","")
            #line_out = line_out.replace("]","")
            #print(line_out)
            fo1.write(str(line_out))  # 2018 12 06
            line_out = []
        
        # Close file
        fo1.close()

        
        
    # Define process_it() method
    def process_it(self):
        """Method to generate a file with statistical analysis of the predictive power"""
        
        # Import libraries
        import numpy as np
        from SFSXplorer import stats_9 as st
        
        # Open file to store statistical analysis
        fo1 = open(self.dir_out+self.file_out,"w")
        
        # Invoke read_read_headers() method
        self.read_headers()
    
        # Get number of rows and columns
        n_rows, n_cols = self.pie2go.shape
        
        # Set up zeros arrays
        rho_array = np.zeros(n_cols)
        p_v1_array = np.zeros(n_cols)
        r_array = np.zeros(n_cols)
        p_v2_array = np.zeros(n_cols)
        
        # Set up empty list
        Y = []
        
        # To get experimental values (slicing the self.pie2go)
        for i in range(n_rows):
            Y.append(float(self.pie2go[i,n_cols-1:n_cols]))
        
        # Looping through data (new slices of the pei)
        for i in range(n_cols):
        
            # Set up empty list
            x = []
        
            # Get explanatory variable data
            for j in range(n_rows):
                x.append(float(self.pie2go[j,i:i+1]))
        
            # Instantiate an object of the StatsAnalys() class
            st1 = st.StatsAnalysis(x,Y)
        
            # Invoke rho() method
            rho_array[i],p_v1_array[i] = st1.rho()

            # Invoke pearson_corr() method
            r_array[i],p_v2_array[i] = st1.pearson_corr()
        
        # Show data results (write first line)
        print("\nEnergy Term\t       rho\t  p-value1\tr\t  p-value2")
        fo1.write("Energy Term,rho,p-value1,r,p-value2\n")
        
        # Looping through statitical analysis
        for i in range(n_cols-1):
            print("{0:8}\t{1:12,.3f}{2:12,.4f}{3:12,.3f}{4:12,.4f}".format(self.headers[i+1],
                rho_array[i],p_v1_array[i],r_array[i],p_v2_array[i]))
            if i < n_cols-1:
                fo1.write(self.headers[i+1]+","+str( rho_array[i])+","+str(p_v1_array[i])+\
                ","+str(r_array[i])+","+str(p_v2_array[i])+"\n")
            else:
                fo1.write(self.headers[i+1]+","+str( rho_array[i])+","+str(p_v1_array[i])+\
                ","+str(r_array[i])+","+str(p_v2_array[i]))
        
        
        self.sort_it(rho_array,self.n_vars)
        
        # Close file
        fo1.close()
        