# To run SFSXplorer

# Define main()
def main():

    # Import package
    from SFSXplorer import sfs

    # Set up input file
    sfs_input = "G:/Projects/SFSXplorer2020h/Inputs/sfs.in"

    # Instantiate an object of the Explorer class
    space = sfs.Explorer(sfs_input)

    # Invoke read_input() method
    space.read_input()

    # Invoke read_data() method
    space.read_data()

    # Invoke write_energy() method
    space.write_energy()

main()