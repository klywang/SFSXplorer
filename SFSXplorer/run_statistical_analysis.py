# Run statistical_analysis
def main():

    # Import plot_potentials from SFSXplorer package
    from SFSXplorer import statistical_analysis as sa

    # Define stats_in file
    stats_in = "Inputs/stats_EC_2_7_11_1.in"

    # Instantiate an object of Stats class
    data1 = sa.Stats(stats_in)

    # Invoke read_stats_in() method
    data1.read_stats_in()

    # Invoke read_it() method
    data1.read_it()

    # Invoke process_it() method
    data1.process_it()

main()