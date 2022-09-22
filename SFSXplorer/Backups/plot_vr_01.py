
# Define plot_pot()
def plot_pot(type_pot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,epsilon_j,m,n):
    """MGenerate plot for intermolecular potential functions"""

    # Import libraries
    import numpy as np
    import matplotlib.pyplot as plt

    r = np.arange(r_min,r_max, 0.01)

    # Check type of potential to plot
    if type_pot == "LJ":
        # Import specific library
        from SFSXplorer import vdw_8 as vd

        # Instantiating an object of the PairwisePot() class and assign it to LJ
        LJ = vd.PairwisePot()

        # Invoking potential() method using above data as arguments
        _,_,v = LJ.potential(reqm_i,epsilon_i,reqm_j,epsilon_j,r,m,n)

        # Plot stuff
        plt.plot(r,v)
        plt.ylim(-1.0,0.6)
        plt.grid()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        plt.savefig("lj.png")

    elif type_pot == "HB":
        # Import specific library
        from SFSXplorer import hb_8 as hb

        # Instantiating an object of the PairwisePot() class and assign it to LJ
        HB1 = hb.PairwisePotHB()

        # Invoking potential() method using above data as arguments
        _,_,v = HB1.potential(reqm_i,epsilon_i,reqm_j,epsilon_j,r,m,n)

        # Plot stuff
        plt.plot(r,v)
        plt.ylim(-1.0,0.6)
        plt.grid()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        plt.savefig("hb.png")

    elif type_pot == "ALL":

        # Import specific library
        from SFSXplorer import vdw_8 as vd

        # Instantiating an object of the PairwisePot() class and assign it to LJ
        LJ = vd.PairwisePot()

        # Invoking potential() method using above data as arguments
        _,_,v1 = LJ.potential(4.00,0.150,4.00,0.15,r,6,12)

        # Import specific library
        from SFSXplorer import hb_8 as hb

        # Instantiating an object of the PairwisePot() class and assign it to LJ
        HB1 = hb.PairwisePotHB()

        # Invoking potential() method using above data as arguments
        _,_,v2 = HB1.potential(1.9,5.0,1.9,5.0,r,10,12)

        # Electrostatic potential
        q_i = -4 # Dummy positive charge
        q_j = 4  # Dummy negative charge
        #v3 = q_i*q_j/(r*epsilon0(r))   # Coulomb potential

        # Import library
        from SFSXplorer import solv_8 as s1

        # Instantiating an object of the PairwisePotHB() class and assign it to LJ
        Sol1 = s1.PairwisePotSol()

        # Get parameters
        vol_i,sol_i,vol_j,sol_j = 22.4493, -0.00162,17.1573,-0.00251

        v4 = Sol1.potential(vol_i,sol_i,vol_j,sol_j,r,0,0)

        # Plot stuff
        plt.plot(r,v1,label="Dispersion/Repulsion")
        plt.plot(r,v2,label="Hydrogen Bonds")
        #plt.plot(r,v3,label="Electrostatics")
        plt.plot(r,v4,label="Desolvatation")

        # Positioning the legends
        plt.legend(loc='upper right')

        plt.ylim(-1.0,0.6)
        plt.grid()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title("AutoDock 4.1 Force Field")
        plt.show()
        plt.savefig("all.png")
def main():

    ##########################################################################
    # For plotting (for comparisons sake)
    # You may comment(#) all lines below
    # Define arguments for plot_pot() method
    print("\nPlotting...")
    x_label = "r($\AA$)"        # x-axis label
    y_label = "V(r)(Kcal/mol)"  # y-axis label
    # For LJ
    type_pot = "LJ"             # Type of potential
    r_min = 2.8                 # Minimum value for r (interatomic distance) in Angstrom
    r_max = 10                  # Maximum value for r (interatomic distance) in Angstrom
    reqm_i  = 3.5               # sum of vdW radii of two like atoms (in Angstrom) (NA atom)
    epsilon_i = 0.16            # Well depth (in Kcal/mol) (NA atom)
    reqm_j  = 3.2               # sum of vdW radii of two like atoms (in Angstrom) (OA atom)
    epsilon_j = 0.20            # Well depth (in Kcal/mol) (OA atom)
    m = 6                       # Attraction expoent
    n = 12                      # Repulsion expoent
    # For HB/ALL
    type_pot = "ALL"            # Type of potential
    r_min = 0.2                 # Minimum value for r (interatomic distance) in Angstrom
    r_max = 10                  # Maximum value for r (interatomic distance) in Angstrom
    reqm_i  = 1.9               # H-bond radius (in Angstrom) (NA atom)
    epsilon_i = 5.0             # Well depth of H-bond (in Kcal/mol) (NA atom)
    reqm_j  = 1.9               # H-bond radius (in Angstrom) (NA atom) (OA atom)
    epsilon_j = 5.0             # Well depth of H-bond (in Kcal/mol) (OA atom)
    m = 10                      # Attraction expoent
    n = 12                      # Repulsion expoent
    # Call plot_plot()
    plot_pot(type_pot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,epsilon_j,m,n)
main()