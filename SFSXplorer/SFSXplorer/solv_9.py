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
# Define class
class PairwisePotSol(object):
    """Class to calculate pairwise potential energy for solvatation based on the autodock equation"""

    # Define potential() method
    def potential(self,vol_i,sol_i,vol_j,sol_j,r,m,n,sigma):
        """Method to calculate pairwise potential energy based on the AutoDock equation"""

        # Import library
        import numpy as np

        # Calculate v(r)
        v = ((vol_i*sol_i) + (vol_j*sol_j))*np.exp(-r**n/(2*sigma**m))

        # Return result
        return v
