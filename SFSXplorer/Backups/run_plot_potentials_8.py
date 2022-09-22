# To plot potentials
def main():

    ##########################################################################
    # For plotting (for comparisons sake)
    # You may comment(#) all lines below
    # Define arguments for plot_pot() method
    print("\nPlotting...")
    x_label = "r($\AA$)"        # x-axis label
    y_label = "V(r)(Kcal/mol)"  # y-axis label
    # For LJ
    #type_pot = "LJ"             # Type of potential
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

    # Import package
    from SFSXplorer import plot_potentials as pp

    # Instantiate an object of the PlotV class
    potentials = pp.PlotV(type_pot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,epsilon_j,m,n)

    # Call gen_plot()
    potentials.gen_plot()

main()