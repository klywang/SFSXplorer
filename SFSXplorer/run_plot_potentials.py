# To run plot_potentials
#
# Define main()
def main():

    # Define file_in and file_out for different type of plots

    #file_in = "Inputs/plot_parameters_LJ.in"
    #file_out = "Plots/lj.png"

    #file_in = "Inputs/plot_parameters_HB.in"
    #file_out = "Plots/hb.png"

    #file_in = "Inputs/plot_parameters_ELE1.in"
    #file_out = "Plots/ele1.png"

    #file_in = "Inputs/plot_parameters_ELE2.in"
    #file_out = "Plots/ele2.png"

    #file_in = "Inputs/plot_parameters_ELE3.in"
    #file_out = "Plots/ele3.png"

    file_in = "Inputs/plot_parameters_DESOL.in"
    file_out = "Plots/desol.png"

    #file_in = "Inputs/plot_parameters_ALL1.in"
    #file_out = "Plots/all1.png"

    #file_in = "Inputs/plot_parameters_ALL2.in"
    #file_out = "Plots/all2.png"

    #file_in = "Inputs/plot_parameters_ALL3.in"
    #file_out = "Plots/all3.png"

    #file_in = "Inputs/plot_parameters_EPSILON.in"
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