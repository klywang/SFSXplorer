#!/usr/bin/python
# Program to calculate intermolecular potential based on atomic coordinates in the PDBQT format
# It uses pair-wise energetic terms of the AutoDock4 progam (Morris et al., 1998).
# 
# Walter F. de Azevedo Jr.
# February 8, 2019
# https://azevedolab.net
#
# Reference:
# Morris G, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A. Automated docking using a
# Lamarckian genetic algorithm and an empirical binding free energy function. J Comput Chem. 1998; # 19:1639-1662. 
#
# Define InterMol() class
class InterMol(object):
    """Class to calculate intermolecular potential based on AutoDock4 pair-wise energetic terms"""
    
    # Define constructor method
    def __init__(self,ad4_par_file):
        """Constructor method"""
        
        # Set up attributes
        self.ad4_par_file = ad4_par_file    # AutoDock4 parameter file
        self.n_tors = 0                     # Set up zero to n_tors (number of torsions)
                                            # to be read from TORSDOF in lig.pdbqt        
    # Define read_AD4_bound() method
    def read_AD4_bound(self):
        """Method to read AD4.1_bound.data file and return a list"""
        
        # Set up empty list
        self.ad4_list = []
        
        # Try to open self.ad4_par_file
        try:
            fo1 = open(self.ad4_par_file,"r")
        except IOError:
            print("\n I can't find ",self.ad4_par_file," file.")
            return
            
        # Looping through fo1
        for line in fo1:
            if line[0:8] == "atom_par":
                # print(line)
                self.ad4_list.append(line)
        
        # Close file
        fo1.close()
        
        # Return list
        return self.ad4_list
        
    # Define get_atom_par_LJ()
    def get_atom_par_LJ(self,par,atom_i,atom_j):
        """Method to retrieve LJ parameters for each atom pair"""
        
        # Looping through par
        for line in par:
            if line[9:11] == atom_i:
                reqm_i = float(line[16:20])     # Equilibrium internuclear distance in Angstrom
                epsilon_i = float(line[21:27])  # Well depth at reqm in Kcal/mol
            elif line[9:11] == atom_j:
                reqm_j = float(line[16:20])     # Equilibrium internuclear distance in Angstrom
                epsilon_j = float(line[21:27])  # Well depth at reqm in Kcal/mol
        
        # Return results
        return reqm_i,epsilon_i,reqm_j,epsilon_j 
        
    # Define get_atom_par_HB()
    def get_atom_par_HB(self,par,atom_i,atom_j):
        """Method to retrieve HB parameters for each atom pair"""
        
        # Looping through par
        for line in par:
            if line[9:11] == atom_i:
                reqm_i = float(line[46:51])     # Equilibrium internuclear distance in Angstrom
                epsilon_i = float(line[51:56])  # Well depth at reqm in Kcal/mol
            elif line[9:11] == atom_j:
                reqm_j = float(line[46:51])     # Equilibrium internuclear distance in Angstrom
                epsilon_j = float(line[51:56])  # Well depth at reqm in Kcal/mol
        
        # Return results
        try:
            return reqm_i,epsilon_i,reqm_j,epsilon_j  
        except:
            if atom_j == "HD":
                reqm_j,epsilon_j = 0.0,0.0
            elif atom_j == "C ":
                reqm_j,epsilon_j = 0.0,0.0
            elif atom_j == "A ":
                reqm_j,epsilon_j = 0.0,0.0
            elif atom_j == "N ":
                reqm_j,epsilon_j = 0.0,0.0
            elif atom_j == "NA":
                reqm_j,epsilon_j = 1.9,5.0
            elif atom_j == "OA":
                reqm_j,epsilon_j = 1.9,5.0
            elif atom_j == "SA":
                reqm_j,epsilon_j = 2.5,1.0
            else:
                print("\nProblems with atoms ",atom_i,atom_j)
            return reqm_i,epsilon_i,reqm_j,epsilon_j
            
    
    # Define get_atom_par_Sol()
    def get_atom_par_Sol(self,par,atom_i,atom_j):
        """Method to retrieve solvent parameters for each atom pair"""
        
        # Looping through par
        for line in par:
            if line[9:11] == atom_i:
                vol_i = float(line[27:36])      # Atomic solvation volume (in Angstrom^3)
                sol_i = float(line[36:46])      # Atomic solvation parameter
            elif line[9:11] == atom_j:
                vol_j = float(line[27:36])      # Atomic solvation volume (in Angstrom^3)
                sol_j = float(line[36:46])      # Atomic solvation parameter
        
        # Return results
        try:
            return vol_i,sol_i,vol_j,sol_j 
        except:
            if atom_j == "HD":
                vol_j,sol_j = 0.0000,0.00051
            elif atom_j == "C ":
                  vol_j,sol_j = 33.5103,-0.00143
            elif atom_j == "A ":
                  vol_j,sol_j = 33.5103,-0.00052
            elif atom_j == "N ":
                vol_j,sol_j = 22.4493,-0.00162
            elif atom_j == "NA":
                  vol_j,sol_j = 22.4493,-0.00162
            elif atom_j == "OA":
                  vol_j,sol_j = 17.1573,-0.00251
            elif atom_j == "SA":
                  vol_j,sol_j = 33.5103,-0.00214
            else:
                print("\nProblems with atom ",atom_j)
                
            return vol_i,sol_i,vol_j,sol_j
        
    # Define dist() method
    def dist(self,x1,y1,z1,x2,y2,z2):
        """Method to calculate Euclidian distance"""
        
        # Import library
        import numpy as np
        
        # Calculate Euclidian distance
        d = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

        # Return distance
        return d
        
    # Define intermol_pot_LJ() method
    def intermol_pot_LJ(self,par_in,ligand,receptor,n,m):
        """Method to calculate intermolecular LJ potential"""
        
        # Import library
        from SFSXplorer import vdw_9 as vd
                
        # Assign zero to v_r
        v_r = 0
        
        # Looping through ligand atoms
        for line_i in ligand:
            
            # Looping through receptor atoms
            for line_j in receptor:
                
                # Get atom type
                atom_i = line_i[77:79]
                atom_j = line_j[77:79]
                
                # Get atomic coordinate for i atom
                x_i = float(line_i[30:38])
                y_i = float(line_i[38:46])
                z_i = float(line_i[46:54])
                
                # Get atomic coordinate for j atom
                x_j = float(line_j[30:38])
                y_j = float(line_j[38:46])
                z_j = float(line_j[46:54])
                
                # Invoking dist() method
                r = self.dist(x_i,y_i,z_i,x_j,y_j,z_j)
                
                # Instantiating an object of the PairwisePot() class and assign it to LJ
                LJ = vd.PairwisePot()
                
                # reqm_i and reqm_j = equilibrium internuclear distance in Angstrom
                # epsilon_i and epsilon_j = well depth at reqm in Kcal/mol 
                
                # Avoid some problems with pdbqt file
                try:
                    reqm_i,epsilon_i,reqm_j,epsilon_j=self.get_atom_par_LJ(par_in,atom_i,atom_j)

                except:
                    if atom_i == "A " and atom_j == "A ":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 4.0,0.15,4.0,0.15
                    elif atom_i == "NA" and atom_j == "NA":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 3.5,0.16,3.5,0.16
                    elif atom_i == "N " and atom_j == "N ":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 3.5,0.16,3.5,0.16
                    elif atom_i == "HD" and atom_j == "HD":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 2.0,0.02,2.0,0.02
                    elif atom_i == "OA" and atom_j == "OA":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 3.2,0.2,3.2,0.2
                    elif atom_i == "OA" and atom_j == "C ":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 3.2,0.2,4.0,0.15
                    elif atom_i == "C " and atom_j == "C ":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 4.0,0.15,4.0,0.15
                    elif atom_i == "SA" and atom_j == "SA":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 4.0,0.2,4.0,0.2
                    elif atom_i == "C " and atom_j == "HD":
                        reqm_i,epsilon_i,reqm_j,epsilon_j = 4.0,0.15,2.0,0.02
                    else:
                        print(atom_i,atom_j)
                    
                # Invoking potential() method using above data as arguments
                cn,cm,v = LJ.potential(reqm_i,epsilon_i,reqm_j,epsilon_j,r,m,n)
                
                # Calculate potential for all atoms
                v_r += v
                
        # Return result
        return v_r
                 
    # Define intermol_pot_HB() method
    def intermol_pot_HB(self,par_in,ligand,receptor,n,m):
        """Method to calcular intermolecular potential"""
        
        # Import library
        from SFSXplorer import hb_9 as hb
        
        # Assign zero to v_r
        v_r = 0
        
        # Looping through ligand atoms
        for line_i in ligand:
            
            # Looping through receptor atoms
            for line_j in receptor:
                
                # Get atom type
                atom_i = line_i[77:79]
                atom_j = line_j[77:79]
                
                # Get atomic coordinate for i atom
                x_i = float(line_i[30:38])
                y_i = float(line_i[38:46])
                z_i = float(line_i[46:54])
                
                # Get atomic coordinate for j atom
                x_j = float(line_j[30:38])
                y_j = float(line_j[38:46])
                z_j = float(line_j[46:54])
                
                # Invoking dist() method
                r = self.dist(x_i,y_i,z_i,x_j,y_j,z_j)
                
                # Instantiating an object of the PairwisePotHB() class and assign it to HB1
                HB1 = hb.PairwisePotHB()
                
                # reqm_i and reqm_j = equilibrium internuclear distance in Angstrom
                # epsilon_i and epsilon_j = well depth at reqm in Kcal/mol 
                # Invoking get_atom_par_HB() method             
                reqm_i,epsilon_i,reqm_j,epsilon_j = self.get_atom_par_HB(par_in,atom_i,atom_j)

                # Invoking potential() method using above data as arguments
                cn,cm,v = HB1.potential(reqm_i,epsilon_i,reqm_j,epsilon_j,r,m,n)
                
                # Calculate potential for all atoms
                v_r += v
                        
        # Return result
        return v_r
    
    # Define intermol_pot_Sol() method
    def intermol_pot_Sol(self,par_in,ligand,receptor,n,m,sigma):
        """Method to calcular intermolecular potential"""
        
        # Import library
        from SFSXplorer import solv_9 as s1
                        
        # Assign zero to v_r
        v_r = 0
        
        # Looping through ligand atoms
        for line_i in ligand:
            
            # Looping through receptor atoms
            for line_j in receptor:
                
                # Get atom type
                atom_i = line_i[77:79]
                atom_j = line_j[77:79]
                
                # Get atomic coordinate for i atom
                x_i = float(line_i[30:38])
                y_i = float(line_i[38:46])
                z_i = float(line_i[46:54])
                
                # Get atomic coordinate for j atom
                x_j = float(line_j[30:38])
                y_j = float(line_j[38:46])
                z_j = float(line_j[46:54])
                
                # Invoking dist() method
                r = self.dist(x_i,y_i,z_i,x_j,y_j,z_j)
                
                # Instantiating an object of the PairwisePotHB() class and assign it to LJ
                Sol1 = s1.PairwisePotSol()
                                
                # reqm_i and reqm_j = equilibrium internuclear distance in Angstrom
                # epsilon_i and epsilon_j = well depth at reqm in Kcal/mol 
                
                # Get parameters
                vol_i,sol_i,vol_j,sol_j = self.get_atom_par_Sol(par_in,atom_i,atom_j)
                    
                # Invoking potential() method using above data as arguments WFA 2020 02 07
                v = Sol1.potential(vol_i,sol_i,vol_j,sol_j,r,m,n,sigma)
                
                # Calculate potential for all atoms
                v_r += v
                
        # Return result
        return v_r
    
    # Define read_PDBQT() method
    def read_PDBQT(self,file_in):
        """Method to read PDBQT file"""
        
        # Set up empty for atom lines
        atom_list = []
        
        # Try to open PDBQT file
        try:
            fo1 = open(file_in,"r")
        except IOError:
            print("\nI can't find ",file_in," file.")
            return atom_list
            
        # Looping through fo1
        for line in fo1:
            if line[0:6] == "HETATM" or line[0:6] == "ATOM  ":
                atom_list.append(line)
            elif line[0:7] == "TORSDOF":
                self.n_tors = int(line[7:])
                    
        # Close file
        fo1.close()
        
        # Return results
        return atom_list
    
    # Define intermol_electro() method
    def intermol_electro(self,ligand,receptor,l,k,a,e0,log_w,tanh_w):
        """Method to calculate intermolecular electrostatic potential"""
        
        # Import library
        from SFSXplorer import elec_9 as e1
        
        # Instantiating an object of the PairwiseElecPot() class and assign it to EL1
        EL1 = e1.PairwiseElecPot()
        
        # Invoking potential() method using above data as arguments WFA 2020 02 07
        v_r = EL1.potential(ligand,receptor,l,k,a,e0,log_w,tanh_w)
                
        # Return result
        return v_r
    
    # Define read_torsion() method
    def read_torsion(self,name_dir):
        """Method to return number of torsion angles (TORSDOF)"""
        
        # Return result
        return self.n_tors