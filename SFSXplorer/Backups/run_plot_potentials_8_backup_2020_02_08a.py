# To run plot_potentials
#
# Define read_plot_pars()
def read_plot_pars(file_in):
    """Read plot parameters"""

    # Import libraries
    import csv
    import sys
    import numpy as np

    # Try to open csv file
    try:
        fo1 = open(file_in,"r")
        my_csv1 = csv.reader(fo1)
    except IOError:
        sys.exit("IOError! I can't find ",file_in," file!")

    # Looping through my_csv1
    for line in my_csv1:
        if line[0] == "#":
            continue
        elif line[0] == "type_plot":
            type_plot = line[1]
        elif "title_in" in line:
            title_in = line[1]
        elif line[0] == "x_label":
            x_label = line[1]
        elif line[0] == "y_label":
            y_label = line[1]
        elif line[0] == "r_min":
            r_min = float(line[1])
        elif line[0] == "r_max":
            r_max = float(line[1])
        elif line[0] == "reqm_i":
            reqm_i = float(line[1])
        elif line[0] == "reqm_j":
            reqm_j = float(line[1])
        elif line[0] == "epsilon_i":
            epsilon_i = float(line[1])
        elif line[0] == "epsilon_j":
            epsilon_j = float(line[1])
        elif line[0] == "log_w":
            log_w = float(line[1])
        elif line[0] == "tanh_w":
            tanh_w = float(line[1])
        elif line[0] == "a_array":
            _1 = float(line[1])
            _2 = float(line[2])
            _3 = int(line[3])
            a_array = np.linspace(_1,_2,_3)
        elif line[0] == "e0_array":
            _1 = float(line[1])
            _2 = float(line[2])
            _3 = int(line[3])
            e0_array = np.linspace(_1,_2,_3)
        elif line[0] == "k_array":
            _1 = float(line[1])
            _2 = float(line[2])
            _3 = int(line[3])
            k_array = np.linspace(_1,_2,_3)
        elif line[0] == "l_array":
            _1 = float(line[1])
            _2 = float(line[2])
            _3 = int(line[3])
            l_array = np.linspace(_1,_2,_3)
        elif line[0] == "m_array":
            _1 = int(line[1])
            _2 = int(line[2])
            _3 = int(line[3])
            m_array = np.linspace(_1,_2,_3)
        elif line[0] == "n_array":
            _1 = int(line[1])
            _2 = int(line[2])
            _3 = int(line[3])
            n_array = np.linspace(_1,_2,_3)
        elif line[0] == "s_array":
            _1 = float(line[1])
            _2 = float(line[2])
            _3 = int(line[3])
            s_array = np.linspace(_1,_2,_3)
        else:
            continue

    # Close file
    fo1.close()

    # Return parameters
    return title_in,type_plot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,\
    reqm_j,epsilon_j,log_w,tanh_w,m_array,n_array,l_array,k_array,a_array,\
    s_array,e0_array

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

    # Call read_plot_pars()
    title_in,type_plot,x_label,y_label,r_min,r_max,reqm_i,epsilon_i,reqm_j,\
    epsilon_j,log_w,tanh_w,m_array,n_array,l_array,k_array,a_array,s_array,\
    e0_array = read_plot_pars(file_in)

    # Import package
    from SFSXplorer import plot_potentials as pp

    # Instantiate an object of the PlotV class
    potentials = pp.PlotV(title_in,type_plot,x_label,y_label,r_min,r_max,reqm_i,
    epsilon_i,reqm_j,epsilon_j,log_w,tanh_w,m_array,n_array,l_array,k_array,
    a_array,s_array,e0_array,file_out)

    # Call gen_plot()
    potentials.gen_plot()

main()