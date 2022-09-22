#!/usr/bin/python
#
# Class to calculate intermolecular potential based on atomic coordinates in the PDBQT
# format. It calculates the potential energy based on Assisted Model Building with Energy
# Refinement (AMBER) force field (Cornell et al., 1995) using the energy terms derived
# from the AutoDock4 (Morris et al., 1998). The traditional 12/6 potential energy is 
# modified to adapt to the data set used to train the scoring function. We vary the exponents
# (m and n parameters) in order to scan the scoring function space (Heck et al., 2017) to
# find the Lennard-Jones potential adequate to the system being modeled.
# 
# References:
# Cornell WD, Cieplak P, Bayly CI, Gould IR, Merz KM Jr, Ferguson DM, Spellmeyer DC, Fox T, 
# Caldwell JW, Kollman PA (1995). A Second Generation Force Field for the Simulation of Proteins, 
# Nucleic Acids, and Organic Molecules. J Am Chem Soc. 1995; 117 (19): 5179–5197. 
#
# Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine 
# Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459–2470.
#
# Morris G, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A. Automated docking using a
# Lamarckian genetic algorithm and an empirical binding free energy function. J Comput Chem. 1998; 19: 1639–1662. 
# 
# Walter F. de Azevedo Jr.
# February 8, 2019
# azevedolab.net
#
# Define class
class PairwisePot(object):
    """Class to calculate pairwise potential energy for van der Waals interactions
        based on the assisted Model Building with Energy Refinement (AMBER) force 
        field (Cornell et al., 1995)"""
        
    # Define potential() method
    def potential(self,reqm_i,epsilon_i,reqm_j,epsilon_j,r,m,n):
        """Method to calculate pairwise potential energy based on the
            assisted Model Building with Energy Refinement (AMBER) force 
            field (Cornell et al., 1995).
            
            Inputs
            reqm_i      : Sum of vdW radii of two like atoms (in Angstrom)
            epsilon_i   : Well depth (in Kcal/mol)
            reqm_j      : Sum of vdW radii of two like atoms (in Angstrom)
            epsilon_j   : Well depth (in Kcal/mol)
            r           : Intermolecular distance
            m           : Attraction expoent 
            n           : Repulsion expoent
            
            Outputs
            cn, cm      : cn and cm are constants whose values depend on the 
                          depth of the energy well and the equilibrium 
                          separation of the two atoms’ nuclei.
            v           : Lennard-Jones potential energy
            """
        
        # Import library
        import numpy as np
        
        # To obtain the Rij value for non H-bonding atoms
        reqm = 0.5*(reqm_i+reqm_j)
        
        #  To obtain the epsilon value for non H-bonding atoms
        epsilon = np.sqrt(epsilon_i*epsilon_j)
        
        # Calculate cm and cn parameters if n != m
        if n != m:
            cm = (n/(n-m))*epsilon*reqm**m 
            cn = (m/(n-m))*epsilon*reqm**n
        else:
            return None,None,None
                
        # Calculate v(r)        
        v = cn/r**n - cm/r**m
        
        # Return results
        return cn,cm,v