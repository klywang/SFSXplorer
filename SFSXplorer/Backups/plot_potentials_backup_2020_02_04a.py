# Define PlotV() class
class PlotV(object):
    """Class to generate plot of potential energy terms"""

    # Define constructor method
    def __init__(self,title_in,type_pot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,epsilon_j,
    m_array,n_array,l_array,k_array,a_array,s_array):
        """Constructor method"""

        # Define attributes
        self.title_in = title_in
        self.type_pot = type_pot
        self.x_label = x_label
        self.y_label = y_label
        self.r_min = r_min
        self.r_max = r_max
        self.reqm_i = reqm_i
        self.epsilon_i = epsilon_i
        self.reqm_j = reqm_j
        self.epsilon_j = epsilon_j
        self.m_array = m_array
        self.n_array = n_array
        self.l_array = l_array
        self.k_array = k_array
        self.a_array = a_array
        self.s_array = s_array

    # Define gen_plot() method
    def gen_plot(self):
        """Method to generate plot"""

        # Import libraries
        import numpy as np
        import matplotlib.pyplot as plt

        # Set up array
        self.r = np.arange(self.r_min,self.r_max, 0.01)

        # Check type of potential to plot
        if self.type_pot == "LJ":

            # Import library
            from SFSXplorer import vdw_8 as vd

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            LJ1 = vd.PairwisePot()

            # Looping through self.m_array (attraction expoent m = 6)
            for m in self.m_array:

                # Looping through self.n_array (repulsion expoent n = 12)
                for n in self.n_array:

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
            plt.savefig("lj.pdf")

        elif self.type_pot == "HB":

            # Import library
            from SFSXplorer import hb_8 as hb

            # Instantiating an object of the PairwisePotHB() class and assign it to LJ
            HB1 = hb.PairwisePotHB()

            # Looping through self.m_array (attraction expoent m = 6)
            for m in self.m_array:

                # Looping through self.n_array (repulsion expoent n = 12)
                for n in self.n_array:

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
            plt.savefig("hb.pdf")

        elif self.type_pot == "ELE1":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array, k_array, and a_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:

                        # Calculate electrostatic potential
                        self.v = q_i*q_j/(self.r*self.epsilon0(self.r,l,k,a))   # Coulomb potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0_tanh(self.r,l,k,a))   # Coulomb potential

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
            plt.savefig("elec1.png")

        elif self.type_pot == "ELE2":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array and a_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:
                        # Calculate electrostatic potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0(self.r,l,k,a))   # Coulomb potential
                        self.v = q_i*q_j/(self.r*self.epsilon0_tanh(self.r,l,k,a))   # Coulomb potential

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
            plt.savefig("elec2.png")

        elif self.type_pot == "ELE3":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array and a_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:
                        # Calculate electrostatic potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0(self.r,l,k,a))   # Coulomb potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0_tanh(self.r,l,k,a))   # Coulomb potential
                        self.v = q_i*q_j/(self.r*self.epsilon0_Gompertz(self.r,l,k,a))   # Coulomb potential

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
            plt.savefig("elec3.png")

        elif self.type_pot == "ELE4":

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Looping through l_array and a_array
            for l in self.l_array:
                for k in self.k_array:
                    for a in self.a_array:
                        # Calculate electrostatic potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0(self.r,l,k,a))   # Coulomb potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0_tanh(self.r,l,k,a))   # Coulomb potential
                        #self.v = q_i*q_j/(self.r*self.epsilon0_Gompertz(self.r,l,k,a))   # Coulomb potential
                        self.v = q_i*q_j/(self.r*self.epsilon0_softplus(self.r,l,k,a))   # Coulomb potential

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
            plt.savefig("elec4.png")

        elif self.type_pot == "SOL1":

            # Import library
            from SFSXplorer import solv_8 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Looping through self.m_array (m = 2)
            for m in self.m_array:

                # Looping through self.n_array (n = 2)
                for n in self.n_array:

                    # Looping throug self.s_array (sigma = 3.5 A)
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
            plt.savefig("sol1.png")

        elif self.type_pot == "ALL":

            # Lennard-Jones Potential

            # Import library
            from SFSXplorer import vdw_8 as vd

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            LJ = vd.PairwisePot()

            # Invoking potential() method using specific data as arguments
            _,_,self.v1 = LJ.potential(4.00,0.150,4.00,0.15,self.r,6,12)

            # Hydrogen-bond Potential

            # Import library
            from SFSXplorer import hb_8 as hb

            # Instantiating an object of the PairwisePotHB() class and assign it to HB
            HB1 = hb.PairwisePotHB()

            # Invoking potential() method using specific data as arguments
            _,_,self.v2 = HB1.potential(1.9,5.0,1.9,5.0,self.r,10,12)

            # Electrostatic potential

            # Set up charges
            q_i = -4 # Dummy positive charge
            q_j = 4  # Dummy negative charge

            # Calculate electrostatic potential
            l = 0.003627
            k = 7.7839
            A = -8.5525
            self.v3 = q_i*q_j/(self.r*self.epsilon0(self.r,l,k,A))   # Coulomb potential

            # Desolvatation Potential

            # Import library
            from SFSXplorer import solv_8 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Invoking potential() method using specific data as arguments
            self.v4 = Sol1.potential(vol_i,sol_i,vol_j,sol_j,self.r,2,2)

            # Plot stuff
            plt.plot(self.r,self.v1,label="Dispersion/Repulsion")
            plt.plot(self.r,self.v2,label="Hydrogen Bonds")
            plt.plot(self.r,self.v3,label="Electrostatics")
            plt.plot(self.r,self.v4,label="Desolvatation")

            # Positioning the legends
            plt.legend(loc='upper right')

            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title_in)
            plt.show()
            plt.savefig("all.png")

    # Define epsilon0() method
    def epsilon0(self,r,l,k,A):
        """Method to calcule sigmoidal distance-dependent dielectric function """

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        e0_r = A + B/(1+k*np.exp(-l*B*r))

        # Return result
        return e0_r

    # Define epsilon0_tanh() method
    def epsilon0_tanh(self,r,l,k,A):
        """Method to calcule distance-dependent dielectric function using tanh"""

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        #e0_r = A + B/(1+k*np.exp(-l*B*r))
        e0_r = A + B*(1/2+(k/2)*np.tanh(l*B*r/2))

        # Return result
        return e0_r

    # Define epsilon0_Gompertz() method
    def epsilon0_Gompertz(self,r,l,k,A):
        """Method to calcule distance-dependent dielectric function using Gompertz function"""

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        #e0_r = A + B/(1+k*np.exp(-l*B*r))
        #e0_r = A + B*(1/2+(k/2)*np.tanh(l*B*r/2))
        e0_r = A + B*(np.exp(-k*(np.exp(-l*B*r)-1)))    # https://en.wikipedia.org/wiki/Gompertz_function

        # Return result
        return e0_r

    # Define epsilon0_softplus() method
    def epsilon0_softplus(self,r,l,k,A):
        """Method to calcule distance-dependent dielectric function using softplus function"""

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        #A = -8.5525
        #l = 0.003627
        #k = 7.7839
        e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        #e0_r = A + B/(1+k*np.exp(-l*B*r))
        #e0_r = A + B*(1/2+(k/2)*np.tanh(l*B*r/2))
        #e0_r = A + B*(np.exp(-k*(np.exp(-l*B*r)-1)))   # https://en.wikipedia.org/wiki/Gompertz_function
        e0_r = A + B*np.log(k/2+(k/2)*np.exp(l*B*r))  # https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Softplus

        # Return result
        return e0_r