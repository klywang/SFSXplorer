# Run split_binding
def main():

    # Import package
    from SFSXplorer import split_binding as lig

    # Instantiate an object of the Binding_Affinity class and
    # Set up working directory (ie. "F:/Development/Split_binding_data/)
    d1 = lig.Binding_Affinity("F:/Projects/Split_binding_data/")

    # Invoke read_chklig() method
    d1.read_chklig()

    # Invoke read_BindingDB() method
    d1.read_BindingDB()

    # Invoke write_BindingDB() method
    d1.write_BindingDB()

    # Invoke read_chklig() method
    d1.read_chklig()

    # Invoke read_BMOAD() method
    d1.read_BMOAD()

    # Invoke write_BMOAD() method
    d1.write_BMOAD()

    # Invoke read_chklig() method
    d1.read_chklig()

    # Invoke read_PDBbind() method
    d1.read_PDBbind()

    # Invoke write_PDBbind() method
    d1.write_PDBbind()

main()