#!/usr/bin/env python
#python script to calculate errors on forces and energies
#from VASP-MLFF with respect to DFT

import numpy as np


def rmse(dft, ml):
    rmse = np.sqrt(((dft - ml) ** 2).mean())
    return rmse

def mae(dft, ml):
    mae = np.sum(np.abs(dft -  ml))/len(dft)
    return mae

def norm(force_components):
    force_norm = np.sum(np.abs(force_components.reshape((-1,3)))**2,axis=-1)**(1/2)
    return force_norm


n_atoms = 256
temp_list = [300, 400, 500, 600, 678, 800]

for temp in temp_list:
    E_dft = np.loadtxt(str(temp) + 'DFTenergies.txt')/n_atoms #eV/at.
    E_ml = np.loadtxt(str(temp) + 'MLFFenergies.txt')/n_atoms #eV/at.
    F_dft = np.loadtxt(str(temp) + 'DFTforces.txt')
    F_ml = np.loadtxt(str(temp) + 'MLFFforces.txt')
    print('TEMPERATURE', temp)
    print('     MAE ,        RMSE,          max (absolute) error')
    print('energy (meV/at.):')
    print('{:10.4f}'.format(1000*mae(E_dft, E_ml)),
          '{:10.4f}'.format(1000*rmse(E_dft, E_ml)),
          '{:10.4f}'.format(1000*max(np.abs(E_dft - E_ml))))
    print('force components (eV/A):')
    print('{:10.4f}'.format(mae(F_dft, F_ml)),
          '{:10.4f}'.format(rmse(F_dft, F_ml)),
          '{:10.4f}'.format(max(np.abs(F_dft - F_ml))))
    print('force norm (eV/A):')
    print('{:10.4f}'.format(mae(norm(F_dft), norm(F_ml))),
          '{:10.4f}'.format(rmse(norm(F_dft), norm(F_ml))),
          '{:10.4f}'.format(max(np.abs(norm(F_dft) - norm(F_ml)))))
