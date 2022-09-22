#!/usr/bin/python
#
# Scoring Function Space eXplorer
#
# SFSXplore: A Python package for exploration of the Scoring Function Space.
#
# This code was developed by Dr. Walter F. de Azevedo, Jr. and is used in the
# program SAnDReS (Xavier et al., 2016).
# These programs are useful for the exploration of the scoring function space
# (Heck et al., 2017; Bitencourt-Ferreira & Azevedo, 2019b) to develop
# computational models targeted to specific protein systems.
#
# References:
#
# Bitencourt-Ferreira G, de Azevedo WF Jr. Machine Learning to Predict Binding
# Affinity. Methods Mol Biol. 2019a; 2053: 251–273.
# DOI: 10.1007/978-1-4939-9752-7_16
#
# Bitencourt-Ferreira G, de Azevedo WF Jr. Exploring the Scoring Function Space.
# Methods Mol Biol. 2019a; 2053: 275–281.
# DOI: 110.1007/978-1-4939-9752-7_17
#
# Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF.
# Supervised Machine Learning Methods Applied to Predict Ligand-Binding
# Affinity. Curr Med Chem. 2017; 24(23): 2459–2470.
# DOI: 10.2174/0929867324666170623092503
#
###############################################################################################################
#
# SAnDReS-Statistical Analysis of Docking Results and Scoring functions
# Written by Dr. Walter F. de Azevedo, Jr.
# with help from
# Mariana M. Xavier, Gabriela Sehnem Heck, Mauricio B. de Avila,
# Nayara M. Bernhardt Levin, Val de Oliveira Pintro, and Nathalia L. Carvalho.
#
# SAnDReS became operational on 12 January 2016 at the Computational Systems
# Biology Laboratory in Porto Alegre, RS Brazil as version number 1.0.1.
#
# Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL,
# Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of
# Docking Results and Development of Scoring Functions.
# Comb Chem High Throughput Screen. 2016; 19(10): 801–812.
# DOI: 10.2174/1386207319666160927111347
#
###############################################################################################################
#
#  GNU General Public License
#  This file is part of SFSXplorer.
#
#    SFSXplorer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    SFSXplorer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with SFSXplorer. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################################################
#
# Contact
# SFSXplorer and SAnDReS are in continuous development, feel free
# to download the latest version and use them in your machine learning
# modelling. If you have any question regarding
# SFSXplorer and SAnDReS, please feel free
# to e-mail me: walter@azevedolab.net
#
# Funding
# Funding Agency: Conselho Nacional de Desenvolvimento Científico e Tecnológico-
# National Counsel of Technological
# and Scientific Development (www.cnpq.br)
# Principal Investigator : Walter F. de Azevedo Jr., Ph.D
# Process Numbers: 472590/2012-0, 308883/2014-4, and 309029/2018-0.
#
###############################################################################################################
#
# Show message about SFSXplorer
print("""
SFSXplorer: A Python package for exploration of the Scoring Function Space.
Developed by the ingenuity of Dr. Walter F. de Azevedo, Jr.
""")