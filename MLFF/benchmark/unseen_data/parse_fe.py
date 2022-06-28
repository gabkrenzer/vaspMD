#!/usr/bin/env python
#parser for energies and forces

import numpy as np
import pandas as pd
from pymatgen.io.vasp.outputs import Oszicar

sample = #number of structures per trajectory
temp_list = [] #input temperatures
n_seed = #number of trajectories per temperature
n_sp = sample*n_seed
n_atoms = #number of atoms
path ='/path/to/working/directory'

def parser(method, n_sp, temp_path, n_atoms, temp):
    energies = []
    forces = []
    for n in range(0, n_sp):
        if method == 'MLFF':
            path = temp_path + '/' + str(n)
        elif method == 'DFT'
            path = temp_path + '/' + str(n) + '/DFT'
        #energies
        energy_data = path + '/energy.dat'
        E0_file = open(energy_data, 'r')
        for line in E0_file:
            E0 = float(line)
        energies.append(E0)
        #forces
        pf = pd.read_csv(path + '/positions-forces.dat', sep="\s+", skiprows = 2, names = ['x', 'y', 'z', 'fx', 'fy', 'fz'])
        for a in range(0, n_atoms):
            forces.append(pf.loc[a, 'fx'])
            forces.append(pf.loc[a, 'fy'])
            forces.append(pf.loc[a, 'fz'])
    np.savetxt(str(temp) + method + 'energies.txt', np.array([energies])) 
    np.savetxt(str(temp) + method + 'forces.txt', np.array([forces]))

#parser
#XDATCAR, OSZICAR, and OUTCAR are in path/${temp}/${n}
for temp in temp_list:
    print('TEMPERATURE:', temp)
    temp_path = path + '/'+ str(temp)
    parser('MLFF', n_sp, temp_path, n_atoms, temp)
    parser('DFT', n_sp, temp_path, n_atoms, temp)
    print('Energies and forces from MLFF and DFT written to files')
