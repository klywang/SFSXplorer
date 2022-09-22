# Run copy_folder
# Main function
def main():

    # Set up file and directories
    chklig_in = "chklig_moad.in"
    root_src = "F:/Backup_Datasets/CDK_IC50/"
    dest = "F:/Backup_Datasets/CDK_IC50_MOAD/NewDataset2020"

    # Import package
    from SFSXplorer import copy_folders as folder

    # Instantiate an object of the Binding_Affinity class and
    # Instantiate an object of CopyDataset()
    d0 = folder.CopyDataset(chklig_in,root_src,dest)

    # Method copy_dir()
    d0.copy_dir()

main()