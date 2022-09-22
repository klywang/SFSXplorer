#!/usr/bin/python
# 
# Walter F. de Azevedo Jr.
# February 16, 2020
# https://azevedolab.net
#
# References:
#
# Morris G, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A. Automated docking using a
# Lamarckian genetic algorithm and an empirical binding free energy function. J Comput Chem. 1998; # 19:1639-1662. 
#
# Zar JH (1972) Significance Testing of the Spearman Rank Correlation Coefficient. J Am Stat Assoc 67(339):578-580
#
# Define Stats class
class Stats(object):
    """Class to carry out statistical analysis of energy terms"""

    # Define constructor method
    def __init__(self,stats_in):
        """Constructor method"""

        # Set up attribute
        self.stats_in = stats_in

    # Define read_stats_in()
    def read_stats_in(self):
        """Method to read stats.in"""
        
        # Import libraries
        import csv
        import sys
                            
        # Try open stats.in file
        try:
            fo = open(self.stats_in,"r")
            csv = csv.reader(fo)
        except IOError:
            sys.exit("\nIOError! I can't find ",self.stats_input," file!")
        
        # Looping through sfs.in
        for line in csv:
            if line[0] == "#":
                continue
            elif line[0] == "data_in":
                self.file_in = str(line[1])
            elif line[0] == "data_out":
                self.file_out = str(line[1])
            elif line[0] == "dir_in":
                self.dir_in = str(line[1])
            elif line[0] == "dir_out":
                self.dir_out = str(line[1])
            elif line[0] == "exp_string":
                self.exp_string = str(line[1])
                
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
        
        # Find index of exp_string
        self.index_experimental = self.headers.index(self.exp_string)
        
        # Show message
        print("\nString "+self.exp_string+" in column: ",self.index_experimental)
        
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
        # pie1 = np.transpose(pie_in[:,1:]) # you transpose it and slice it row and column
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
    def sort_it(self,my_array):
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
        
        
        # Get explanatory variable headers with highest Spearman's correlation
        for i in range(1,self.index_experimental):
            aux = np.where(abs_array == sorted_array1[i])
        
            #print(aux[0][0])
            #input("BUM")
            self.exp_var_headers.append(self.headers[int(aux[0][0])+1])

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

            # Get explanatory variable data
            for j in range(len(self.pie2go[:,i-1:i])):
                for k in range(len(self.pie2go[j-1:j,:])):
                    line_out += ","+str(self.pie2go[k,i-1:i])
            
            # Write line
            fo1.write(str(line_out))  # 2018 12 06
            line_out = []
        
        # Close file
        fo1.close()

    # Define calc_ESS() method
    def calc_ESS(self,x,y_pred):
        """Calculate Explained Sum of Squares (ESS)"""

        # Import library
        import numpy as np

        # Get number of data points
        n = len(x)

        # Set up array with zeros
        aux = np.zeros(n,dtype=float)

        # Calculate mean of x
        mean_y_in = np.mean(x)

        # Looping through data points y_pred
        for i in range(n):
            aux[i] = (y_pred[i] - mean_y_in)**2

        # Calculates Explained Sum of Squares (ESS)
        self.ess = np.sum(aux)

    # Define calc_RSS() method
    def calc_RSS(self,x,y_pred):
        """Calculate Residual Sum of Squares (RSS)"""

        # Import library
        import numpy as np

        # Get number of data points
        n = len(x)

        # Set up array with zeros
        aux = np.zeros(n,dtype=float)

        # Calculate aux
        for i in range(n):
            aux[i] = (x[i] - y_pred[i])**2

        # Calculates Residual Sum of Squares (RSS)
        self.rss = np.sum(aux)

    # Define rho method
    def rho(self,x,y):
        """Method to calculate Spearman's rank correlation coefficient"""
        
        # Import library
        from scipy import stats
        
        # Calculate Spearman rank correlation coefficient and p-values
        s,pvalue = stats.spearmanr(x,y)
        
        # Return Spearman rank correlation coefficient and p-value
        return s,pvalue

    # Define pearson_corr method
    def pearson_corr(self,x,y):
        """Method to calculate Pearson's correlation coefficient"""

        # Import library
        from scipy import stats

        # Calculate Pearson correlation coefficient and p-value
        r,pvalue =  stats.pearsonr(x,y)

        # Return Pearson correlation coefficient and p-value
        return r,pvalue

    # Define additional_metrics() method
    def additional_metrics(self,x,y_pred):
        """Method to carry out additional statistical analysis"""

        # Import libraries
        import numpy as np
        from sklearn.metrics import mean_squared_error

        # Call calc_RSS method
        self.calc_RSS(x,y_pred)

        # Call calc_ESS method
        self.calc_ESS(x,y_pred)

        # Basic statistics
        n = len(y_pred)                             # Number of data points
        mse = mean_squared_error(x, y_pred)         # Mean squared error (mse)
        rmse = np.sqrt(mse)                         # RMSE
        sd = np.std(x,ddof=1)                       # Standard deviation
                                                    # https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.std.html

        # Return parameters
        return mse,rmse,sd
        
    # Define process_it() method
    def process_it(self):
        """Method to generate a file with statistical analysis of the predictive power"""
        
        # Import library
        import numpy as np
        
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
        r2_array = np.zeros(n_cols)
        p_v2_array = np.zeros(n_cols)
        mse_array = np.zeros(n_cols)
        rmse_array = np.zeros(n_cols)
        sd_array = np.zeros(n_cols)
        
        # Set up empty list
        y = []
        
        # To get experimental values (slicing the self.pie2go)
        for i in range(n_rows):
            y.append(float(self.pie2go[i,n_cols-1:n_cols]))
        
        # Looping through data (new slices of the pei)
        for i in range(n_cols):
        
            # Set up empty list
            x = []
        
            # Get explanatory variable data
            for j in range(n_rows):
                x.append(float(self.pie2go[j,i:i+1]))
                
            # Invoke rho() method
            rho_array[i],p_v1_array[i] = self.rho(x,y)

            # Invoke pearson_corr() method
            r_array[i],p_v2_array[i] = self.pearson_corr(x,y)
            r2_array[i] = r_array[i]**2
            
            # Invoke additional_metrics(y) method
            mse_array[i],rmse_array[i],sd_array[i] = self.additional_metrics(x,y)
        
        # Show data results (write first line)
        fo1.write("Energy Term,rho,p-value1,r,p-value2,r2,MSE,RMSE,SD\n")
        
        # Looping through statitical analysis
        for i in range(n_cols-1):
            if i < n_cols-1:
                fo1.write(self.headers[i+1]+","+str( rho_array[i])+","+str(p_v1_array[i])+\
                ","+str(r_array[i])+","+str(p_v2_array[i])+","+str(r2_array[i])+\
                ","+str(mse_array[i])+","+str(rmse_array[i])+","+str(sd_array[i])+"\n")
            else:
                fo1.write(self.headers[i+1]+","+str( rho_array[i])+","+str(p_v1_array[i])+\
                ","+str(r_array[i])+","+str(p_v2_array[i])+","+str(r2_array[i])+\
                +","+str(mse_array[i])+","+str(rmse_array[i])+","+str(sd_array[i]))
        
        # Invoke sort_it() method
        self.sort_it(rho_array)
        
        # Close file
        fo1.close()
        
        # Show message
        print("\nStatistical analysis written in ",self.dir_out+self.file_out)