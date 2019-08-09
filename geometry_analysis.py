"""
geometry_analysis.py
This module contains the geometry analysis project 
"""

import numpy
import os
import sys


def open_xyz(filename):
    """
    A function that reads in and processes an xyz file    
    Inputs: filename
    Outputs: symbols, coords (as numpy array)
    """
        
    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2,  dtype='unicode')

    symbols = xyz_file[:, 0]
    coordinates = xyz_file[:, 1:]
    coordinates = coordinates.astype(numpy.float)
    
    return symbols, coordinates   


def bond_check(distance, min_length=0.0, max_length=1.5):
    """
    This function checks if a distance is between the specified
    min (default: 0.0 Angstrom) and max (default: 1.5 Angstrom) values
    Inputs: distance [Ansgstrom], min and max limits
    Returns: True or False
    
    """
    res = False
    if distance < max_length and distance > min_length:
        res = True
    return res

def calculate_distance(atom1_coord, atom2_coord):
    """
    This function takes the coordinates of two atoms 
    Inputs: atom1 coord, atom2 coord
    Return: distance
    """
    if(len(atom1_coord)<3):
        raise ValueError("Incorrect input: Length of the atom1 coordinates array is too small")
    if(len(atom2_coord)<3):
        raise ValueError("Incorrect input: Length of the atom1 coordinates array is too small")

    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]    
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance




if __name__ == "__main__":


    print(F"Running {sys.argv[0]}")
    if(len(sys.argv) < 2):
        raise NameError("Incorrect input: Please specify an xyz file to be used")

    file_location = sys.argv[1]

    symbols, coord = open_xyz(file_location)
    #coord = coord[:,:2]

    num_atoms = len(symbols)

    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                    
                bond_length_12 = calculate_distance(coord[num1], coord[num2])
                if bond_check(bond_length_12) is True:                
                    #print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12}')
                    print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')
                    #pass

