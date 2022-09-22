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

    file_in = "Inputs/plot_pars_EPSILON.csv"
    file_out = "Plots/epsilon.png"

    # Import from SFSXplorer package
    from SFSXplorer import read_parameters as par

    # Instantiate ao object of PlotParameters() class
    p1 = par.PlotParameters(file_in)

    # Call read_all() method
    title_in,type_plot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,\
    epsilon_j,log_w,tanh_w,m_array,n_array,l_array,k_array,a_array,s_array,\
    e0_array = p1.read_all()

    # Import from SFSXplorer package
    from SFSXplorer import plot_potentials as pp

    # Instantiate an object of the PlotV class
    potentials = pp.PlotV(title_in,type_plot,x_label,y_label,r_min,r_max,reqm_i,
    epsilon_i,reqm_j,epsilon_j,log_w,tanh_w,m_array,n_array,l_array,k_array,
    a_array,s_array,e0_array,file_out)

    # Call gen_plot()
    potentials.gen_plot()

main()