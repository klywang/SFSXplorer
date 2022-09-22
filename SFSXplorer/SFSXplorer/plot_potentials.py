# Define PlotV() class
class PlotV(object):
    """Class to generate plot of potential energy terms"""

    # Define constructor method
    def __init__(self,file_in,file_out):
        """Constructor method"""

        # Define attributes
        self.file_in = file_in
        self.file_out = file_out

        print("\nGenerating ",self.file_out," plot...",end=" ")

    # Define read_plot_parameters()
    def read_plot_parameters(self):
        """Read plot parameters"""

        # Import libraries
        import csv
        import sys
        import numpy as np

        # Try to open csv file
        try:
            fo1 = open(self.file_in,"r")
            my_csv1 = csv.reader(fo1)
        except IOError:
            sys.exit("IOError! I can't find ",self.file_in," file!")

        # Looping through my_csv1
        for line in my_csv1:
            if line[0] == "#":
                continue
            elif line[0] == "type_plot":
                self.type_plot = line[1]
            elif "title_in" in line:
                self.title_in = line[1]
            elif line[0] == "x_label":
                self.x_label = line[1]
            elif line[0] == "y_label":
                self.y_label = line[1]
            elif line[0] == "r_min":
                self.r_min = float(line[1])
            elif line[0] == "r_max":
                self.r_max = float(line[1])
            elif line[0] == "reqm_i":
                self.reqm_i = float(line[1])
            elif line[0] == "reqm_j":
                self.reqm_j = float(line[1])
            elif line[0] == "epsilon_i":
                self.epsilon_i = float(line[1])
            elif line[0] == "epsilon_j":
                self.epsilon_j = float(line[1])
            elif line[0] == "log_w":
                self.log_w = float(line[1])
            elif line[0] == "tanh_w":
                self.tanh_w = float(line[1])
            elif line[0] == "a_array":
                _1 = float(line[1])
                _2 = float(line[2])
                _3 = int(line[3])
                self.a_array = np.linspace(_1,_2,_3)
            elif line[0] == "e0_array":
                _1 = float(line[1])
                _2 = float(line[2])
                _3 = int(line[3])
                self.e0_array = np.linspace(_1,_2,_3)
            elif line[0] == "k_array":
                _1 = float(line[1])
                _2 = float(line[2])
                _3 = int(line[3])
                self.k_array = np.linspace(_1,_2,_3)
            elif line[0] == "l_array":
                _1 = float(line[1])
                _2 = float(line[2])
                _3 = int(line[3])
                self.l_array = np.linspace(_1,_2,_3)
            elif line[0] == "m_array":
                _1 = int(line[1])
                _2 = int(line[2])
                _3 = int(line[3])
                self.m_array = np.linspace(_1,_2,_3)
            elif line[0] == "n_array":
                _1 = int(line[1])
                _2 = int(line[2])
                _3 = int(line[3])
                self.n_array = np.linspace(_1,_2,_3)
            elif line[0] == "s_array":
                _1 = float(line[1])
                _2 = float(line[2])
                _3 = int(line[3])
                self.s_array = np.linspace(_1,_2,_3)
            else:
                continue

        # Close file
        fo1.close()

    # Define gen_plot() method
    def gen_plot(self):
        """Method to generate plot"""

        # Import libraries
        import numpy as np
        import matplotlib.pyplot as plt

        # Set up array
        self.r = np.arange(self.r_min,self.r_max, 0.01)

        # Check the type of potential to plot
        if self.type_plot == "LJ":

            # Import vdw_9 from SFSXplorer package
            from SFSXplorer import vdw_9 as vd

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            LJ1 = vd.PairwisePot()

            # Invert array
            m_array_inv = np.flip(self.m_array)

            # Looping through m_array_inv (attraction expoent m = 6)
            for m in m_array_inv:

                # Looping through range(m) (repulsion expoent n = 12)
                for n in range(2,int(m)):

                    # To avoid m== n
                    if m != n :

                        # Invoking potential() method using specific data as arguments
                        _,_,self.v = LJ1.potential(self.reqm_i,self.epsilon_i,self.reqm_j,self.epsilon_j,self.r,m,n)

                        # Plot stuff
                        plt.plot(self.r,self.v)

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "HB":

            # Import hb_9 from SFSXplorer package
            from SFSXplorer import hb_9 as hb

            # Instantiating an object of the PairwisePotHB() class and assign it to LJ
            HB1 = hb.PairwisePotHB()

            # Invert array
            m_array_inv = np.flip(self.m_array)

            # Looping through m_array_inv (attraction expoent m = 6)
            for m in m_array_inv:

                # Looping through range(m) (repulsion expoent n = 12)
                for n in range(2,int(m)):

                    # To avoid m== n
                    if m != n :

                        # Invoking potential() method using specific data as arguments
                        _,_,self.v = HB1.potential(self.reqm_i,self.epsilon_i,self.reqm_j,self.epsilon_j,self.r,m,n)

                        # Plot stuff
                        plt.plot(self.r,self.v)

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "ELE1":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array, k_array, a_array, and e0_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:
                        for e0 in self.e0_array:

                            # Calculate electrostatic potential
                            ep = self.log_w*self.epsilon0(self.r,l,k,a,e0) + self.tanh_w*self.epsilon0_tanh(self.r,l,k,a,e0)
                            self.v = q_i*q_j/(self.r*ep)   # Coulomb potential

                            # Plot stuff
                            plt.plot(self.r,self.v)

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "ELE2":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array, k_array, a_array, and e0_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:
                        for e0 in self.e0_array:

                            # Calculate electrostatic potential
                            ep = self.log_w*self.epsilon0(self.r,l,k,a,e0) + self.tanh_w*self.epsilon0_tanh(self.r,l,k,a,e0)
                            self.v = q_i*q_j/(self.r*ep)   # Coulomb potential

                            # Plot stuff
                            plt.plot(self.r,self.v)

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "ELE3":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array, k_array, a_array, and e0_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:
                        for e0 in self.e0_array:

                            # Calculate electrostatic potential
                            ep = self.log_w*self.epsilon0(self.r,l,k,a,e0) + self.tanh_w*self.epsilon0_tanh(self.r,l,k,a,e0)
                            self.v = q_i*q_j/(self.r*ep)   # Coulomb potential

                            # Plot stuff
                            plt.plot(self.r,self.v)

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "EPSILON":

            # Define parameters
            l = 0.003627
            k = 7.7839
            a = -8.5525
            e0 = 78.4
            self.ep1 = self.epsilon0(self.r,l,k,a,e0)

            # Plot stuff
            plt.plot(self.r,self.ep1,label="Logistic $\epsilon$ ($\lambda$="+str(l)+", k="+str(k)+", A="+str(a)+")")

            # Define parameters
            l = 0.001787
            k = 3.4781
            a = -20.929
            self.ep2 = self.epsilon0(self.r,l,k,a,e0)

            # Plot stuff
            plt.plot(self.r,self.ep2,label="Logistic $\epsilon$ ($\lambda$="+str(l)+", k="+str(k)+", A="+str(a)+")")

            # Define parameters
            l = 0.003627
            k = 7.7839
            a = -8.5525
            self.ep3 = self.epsilon0_tanh(self.r,l,k,a,e0)

            # Plot stuff
            plt.plot(self.r,self.ep3,label="Tanh $\epsilon$ ($\lambda$="+str(l)+", k="+str(k)+", A="+str(a)+")")

            # Define parameters
            l = 0.001787
            k = 3.4781
            a = -20.929
            self.ep4 = self.epsilon0_tanh(self.r,l,k,a,e0)

            # Plot stuff
            plt.plot(self.r,self.ep4,label="Tanh $\epsilon$ ($\lambda$="+str(l)+", k="+str(k)+", A="+str(a)+")")

            # Define parameters
            l = 0.003627
            k = 7.7839
            a = -8.5525
            self.ep5 = 0.5*self.epsilon0_tanh(self.r,l,k,a,e0) + 0.5*self.epsilon0(self.r,l,k,a,e0)

            # Plot stuff
            plt.plot(self.r,self.ep5,label="Logistic+Tanh $\epsilon$ ($\lambda$="+str(l)+", k="+str(k)+", A="+str(a)+")")

            # Define parameters
            l = 0.001787
            k = 3.4781
            a = -20.929
            self.ep6 = 0.5*self.epsilon0_tanh(self.r,l,k,a,e0) + 0.5*self.epsilon0(self.r,l,k,a,e0)

            # Plot stuff
            plt.plot(self.r,self.ep6,label="Logistic+Tanh $\epsilon$ ($\lambda$="+str(l)+", k="+str(k)+", A="+str(a)+")")

            # Positioning the legends
            plt.legend(loc='lower right', prop = {"size":9})

            # More plot stuff
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "DESOL":

            # Import solv_9 from SFSXplorer package
            from SFSXplorer import solv_9 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Looping through self.m_array (m = 2)
            for m in self.m_array:

                # Looping through self.n_array (n = 2)
                for n in self.n_array:

                    # Looping through self.s_array (sigma = 3.5 A)
                    for s in self.s_array:

                        # Invoking potential() method using specific data as arguments
                        self.v = Sol1.potential(vol_i,sol_i,vol_j,sol_j,self.r,m,n,s)

                        # Plot stuff
                        plt.plot(self.r,self.v)

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)

            # Show plot
            plt.show()

            # Save plot
            plt.savefig(self.file_out)

        elif self.type_plot == "ALL1":

            # Lennard-Jones Potential

            # Import vdw_9 from SFSXplorer package
            from SFSXplorer import vdw_9 as vd

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            LJ = vd.PairwisePot()

            # Invoking potential() method using specific data as arguments
            _,_,self.v1 = LJ.potential(4.00,0.150,4.00,0.15,self.r,6,12)

            # Hydrogen-bond Potential

            # Import hb_9 from SFSXplorer package
            from SFSXplorer import hb_9 as hb

            # Instantiating an object of the PairwisePotHB() class and assign it to HB
            HB1 = hb.PairwisePotHB()

            # Invoking potential() method using specific data as arguments
            _,_,self.v2 = HB1.potential(1.9,5.0,1.9,5.0,self.r,10,12)

            # Electrostatic potential

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Calculate electrostatic potential with logistic function as epsilon
            l = 0.003627
            k = 7.7839
            A = -8.5525
            e0 = 78.4
            ep = self.log_w*self.epsilon0(self.r,l,k,A,e0) + self.tanh_w*self.epsilon0_tanh(self.r,l,k,A,e0)
            self.v3 = q_i*q_j/(self.r*ep)   # Coulomb potential

            # Desolvatation Potential

            # Import solv_9 from SFSXplorer package
            from SFSXplorer import solv_9 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Invoking potential() method using specific data as arguments
            self.v6 = Sol1.potential(vol_i,sol_i,vol_j,sol_j,self.r,2,2,3.5)

            # Sum potentials without weight
            all_pot = self.v1 + self.v2 + self.v3 + self.v6

            # Plot stuff
            plt.plot(self.r,self.v1,label="Repulsion/Attraction")
            plt.plot(self.r,self.v2,label="Hydrogen Bonds")
            plt.plot(self.r,self.v3,label="Electrostatics (Logistic $\epsilon$)")
            plt.plot(self.r,self.v6,label="Desolvatation")
            plt.plot(self.r,all_pot,label="Summation of Potentials")

            # Positioning the legends
            plt.legend(loc='upper right')

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)
            plt.show()
            plt.savefig(self.file_out)

        elif self.type_plot == "ALL2":

            # Lennard-Jones Potential

            # Import vdw_9 from SFSXplorer package
            from SFSXplorer import vdw_9 as vd

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            LJ = vd.PairwisePot()

            # Invoking potential() method using specific data as arguments
            _,_,self.v1 = LJ.potential(4.00,0.150,4.00,0.15,self.r,6,12)

            # Hydrogen-bond Potential

            # Import hb_9 from SFSXplorer package
            from SFSXplorer import hb_9 as hb

            # Instantiating an object of the PairwisePotHB() class and assign it to HB
            HB1 = hb.PairwisePotHB()

            # Invoking potential() method using specific data as arguments
            _,_,self.v2 = HB1.potential(1.9,5.0,1.9,5.0,self.r,10,12)

            # Electrostatic potential

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Calculate electrostatic potential with tanh function as epsilon
            l = 0.003627
            k = 7.7839
            A = -8.5525
            e0 = 78.4
            ep = self.log_w*self.epsilon0(self.r,l,k,A,e0) + self.tanh_w*self.epsilon0_tanh(self.r,l,k,A,e0)
            self.v4 = q_i*q_j/(self.r*ep)   # Coulomb potential

            # Desolvatation Potential

            # Import solv_9 from SFSXplorer package
            from SFSXplorer import solv_9 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Invoking potential() method using specific data as arguments
            self.v6 = Sol1.potential(vol_i,sol_i,vol_j,sol_j,self.r,2,2,3.5)

            # Sum potentials without weight
            all_pot = self.v1 + self.v2 + self.v4 + self.v6

            # Plot stuff
            plt.plot(self.r,self.v1,label="Repulsion/Attraction")
            plt.plot(self.r,self.v2,label="Hydrogen Bonds")
            plt.plot(self.r,self.v4,label="Electrostatics (Tanh $\epsilon$)")
            plt.plot(self.r,self.v6,label="Desolvatation")
            plt.plot(self.r,all_pot,label="Summation of Potentials")

            # Positioning the legends
            plt.legend(loc='upper right')

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)
            plt.show()
            plt.savefig(self.file_out)

        elif self.type_plot == "ALL3":

            # Lennard-Jones Potential

            # Import vdw_9 from SFSXplorer package
            from SFSXplorer import vdw_9 as vd

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            LJ = vd.PairwisePot()

            # Invoking potential() method using specific data as arguments
            _,_,self.v1 = LJ.potential(4.00,0.150,4.00,0.15,self.r,6,12)

            # Hydrogen-bond Potential

            # Import hb_9 from SFSXplorer package
            from SFSXplorer import hb_9 as hb

            # Instantiating an object of the PairwisePotHB() class and assign it to HB
            HB1 = hb.PairwisePotHB()

            # Invoking potential() method using specific data as arguments
            _,_,self.v2 = HB1.potential(1.9,5.0,1.9,5.0,self.r,10,12)

            # Electrostatic potential

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Calculate electrostatic potential with tanh function as epsilon
            l = 0.003627
            k = 7.7839
            A = -8.5525
            e0 = 78.4
            ep = self.log_w*self.epsilon0(self.r,l,k,A,e0) + self.tanh_w*self.epsilon0_tanh(self.r,l,k,A,e0)
            self.v5 = q_i*q_j/(self.r*ep)   # Coulomb potential

            # Desolvatation Potential

            # Import solv_9 from SFSXplorer package
            from SFSXplorer import solv_9 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Invoking potential() method using specific data as arguments
            self.v6 = Sol1.potential(vol_i,sol_i,vol_j,sol_j,self.r,2,2,3.5)

            # Sum potentials without weight
            all_pot = self.v1 + self.v2 + self.v5 + self.v6

            # Plot stuff
            plt.plot(self.r,self.v1,label="Repulsion/Attraction")
            plt.plot(self.r,self.v2,label="Hydrogen Bonds")
            plt.plot(self.r,self.v5,label="Electrostatics (Logistic+Tanh $\epsilon$)")
            plt.plot(self.r,self.v6,label="Desolvatation")
            plt.plot(self.r,all_pot,label="Summation of Potentials")

            # Positioning the legends
            plt.legend(loc='upper right')

            # More plot stuff
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)
            plt.show()
            plt.savefig(self.file_out)

        # Show message
        print("Done!")

    # Define epsilon0() method
    def epsilon0(self,r,l,k,A,e0):
        """Method to calcule sigmoidal distance-dependent dielectric function """

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        #e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        e0_r = A + B/(1+k*np.exp(-l*B*r))

        # Return result
        return e0_r

    # Define epsilon0_tanh() method
    def epsilon0_tanh(self,r,l,k,A,e0):
        """Method to calcule distance-dependent dielectric function using tanh"""

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        #e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        #e0_r = A + B/(1+k*np.exp(-l*B*r))
        #e0_r = A + B*(1/2+(k/2)*np.tanh(l*B*r/2))
        #e0_r = A + B*(1/2+(1/2)*np.tanh(l*B*r/2)) OK!
        #e0_r = A + B*(1/2+(1/2)*np.tanh(l*B*r/2))
        e0_r = A + B*(np.exp(l*B*r)-k*np.exp(-l*B*r))/(np.exp(l*B*r)+k*np.exp(-l*B*r))

        # Return result
        return e0_r

    # Define epsilon0_arctan() method
    def epsilon0_arctan(self,r,l,k,A,e0):
        """Method to calcule distance-dependent dielectric function using arctan function"""

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        #e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        #e0_r = A + B/(1+k*np.exp(-l*B*r))
        #e0_r = A + B*(1/2+(k/2)*np.tanh(l*B*r/2))
        #e0_r = A + B*(1/2+(1/2)*np.tanh(l*B*r/2)) OK!
        #e0_r = A + B*(1/2+(1/2)*np.tanh(l*B*r/2))
        #e0_r = A + B*(np.exp(l*B*r)-k*np.exp(-l*B*r))/(np.exp(l*B*r)+k*np.exp(-l*B*r))
        #e0_r = A + B*(1/np.sqrt(2))*np.arctan(l*B*r) # OK!
        #e0_r = A + B*np.arctan(k*l*r)
        e0_r = A + B*(np.exp(1)/np.sqrt(2*k))*np.arctan(l*B*r) # OK!

        # Return result
        return e0_r