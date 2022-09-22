# To run SFSXplorer

# Define main()
def main():
    
    # Import package
    from SFSXplorer import sfs
    
    # Instantiate an object of the Explorer class
    space = sfs.Explorer()
    
    # Invoke read_input() method
    space.read_input()

    # Invoke read_data() method
    space.read_data()
    
    # Invoke write_energy() method
    space.write_energy()

main()