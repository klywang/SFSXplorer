# Define PlotV() class
class PlotV(object):
    """Class to generate plot of potential energy terms"""

    # Define constructor method
    def __init__(self,type_pot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,epsilon_j,m,n):
        """Constructor method"""

        # Define attributes
        self.type_pot = type_pot
        self.x_label = x_label
        self.y_label = y_label
        self.r_min = r_min
        self.r_max = r_max
        self.reqm_i = reqm_i
        self.epsilon_i = epsilon_i
        self.reqm_j = reqm_j
        self.epsilon_j = epsilon_j
        self.m = m
        self.n = n

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
            LJ = vd.PairwisePot()

            # Invoking potential() method using above data as arguments
            _,_,self.v = LJ.potential(self.reqm_i,self.epsilon_i,self.reqm_j,self.epsilon_j,self.r,self.m,self.n)

            # Plot stuff
            plt.plot(self.r,self.v)
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.show()
            plt.savefig("lj.png")

        elif self.type_pot == "HB":

            # Import library
            from SFSXplorer import hb_8 as hb

            # Instantiating an object of the PairwisePot() class and assign it to LJ
            HB1 = hb.PairwisePotHB()

            # Invoking potential() method using above data as arguments
            _,_,self.v = HB1.potential(self.reqm_i,self.epsilon_i,self.reqm_j,self.epsilon_j,self.r,self.m,self.n)

            # Plot stuff
            plt.plot(self.r,self.v)
            plt.ylim(-1.0,0.6)
            plt.grid()
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.show()
            plt.savefig("hb.png")

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
            self.v3 = q_i*q_j/(self.r*self.epsilon0(self.r))   # Coulomb potential

            # Desolvatation Potential

            # Import library
            from SFSXplorer import solv_8 as s1

            # Instantiating an object of the PairwisePotSol() class and assign it to Sol1
            Sol1 = s1.PairwisePotSol()

            # Get parameters
            vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

            # Invoking potential() method using specific data as arguments
            self.v4 = Sol1.potential(vol_i,sol_i,vol_j,sol_j,self.r,0,0)

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
            plt.title("AutoDock 4.1 Force Field")
            plt.show()
            plt.savefig("all.png")

    # Define epsilon0() method
    def epsilon0(self,r):
        """Method to calcule sigmoidal distance-dependent dielectric function """

        # Import library
        import numpy as np

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        A = -8.5525
        l = 0.003627
        k = 7.7839
        e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model solvent
        # screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        e0_r = A + B/(1+k*np.exp(-l*B*r))

        # Return result
        return e0_r