#!/usr/bin/python
#
# Class to calculate intermolecular potential based on atomic coordinates in the PDBQT
# format. It calculates the potential energy based on Assisted Model Building with Energy
# Refinement (AMBER) force field (Cornell et al., 1995) using the energy terms derived
# from the AutoDock4 (Morris et al., 1998). The traditional 12/10 potential energy is 
# modified to adapt to the data set used to train the scoring function. We vary the exponents
# (m and n parameters) in order to scan the scoring function space (Heck et al., 2017) to
# find the hydrogen-bond potential adequate to the system being modeled.
# 
# 
# Walter F. de Azevedo Jr.
# February 12, 2020
# https://azevedolab.net
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
# Define class PairwisePotHB()
class PairwisePotHB(object):
    """Class to calculate pairwise potential energy for hydrogen bonds based on the
        assisted Model Building with Energy Refinement (AMBER) force 
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
            v           : Hydrogen-bond potential energy
            
            """
        
        # Import library
        import numpy as np
        
        # To obtain the Rij value for H-bonding atoms
        if reqm_i > reqm_j:
            reqm = reqm_i
        elif reqm_i < reqm_j:
            reqm = reqm_j
        else:
            reqm = reqm_i
        
        #  To obtain the epsilon value for H-bonding atoms
        if epsilon_i > epsilon_j:
            epsilon = epsilon_i
        elif epsilon_i < epsilon_j:
            epsilon = epsilon_j
        else:
            epsilon = epsilon_i
        
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