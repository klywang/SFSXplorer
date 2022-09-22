# To run plot_potentials
#
# Define main()
def main():

    # Define file_in and file_out for different type of plots

    #file_in = "Inputs/plot_pars_LJ.csv"
    #file_out = "Plots/lj.png"

    #file_in = "Inputs/plot_pars_HB.csv"
    #file_out = "Plots/hb.png"

    #file_in = "Inputs/plot_pars_ELE1.csv"
    #file_out = "Plots/ele1.png"

    #file_in = "Inputs/plot_pars_ELE2.csv"
    #file_out = "Plots/ele2.png"

    #file_in = "Inputs/plot_pars_ELE3.csv"
    #file_out = "Plots/ele3.png"

    #file_in = "Inputs/plot_pars_DESOL.csv"
    #file_out = "Plots/desol.png"

    #file_in = "Inputs/plot_pars_ALL1.csv"
    #file_out = "Plots/all1.png"

    #file_in = "Inputs/plot_pars_ALL2.csv"
    #file_out = "Plots/all2.png"

    #file_in = "Inputs/plot_pars_ALL3.csv"
    #file_out = "Plots/all3.png"

    #file_in = "Inputs/plot_pars_EPSILON.csv"
    #file_out = "Plots/epsilon.png"

    # Import plot_potentials from SFSXplorer package
    from SFSXplorer import plot_potentials as pp

    # Instantiate an object of the PlotV class
    potentials = pp.PlotV(file_in,file_out)

    # Call read_plot_parameters()
    potentials.read_plot_parameters()

    # Call gen_plot()
    potentials.gen_plot()

main()