#!usr/bin/env python
#prepare INCARs with different RANDOM_SEEDs at diffrent temperatures from an VASP MD INCAR

import os
from shutil import copy
from pymatgen.io.vasp.inputs import Incar

RANDOM_SEED_LIST = [] #input different random seeds as strings, e.g. '248489752 0 0'
T_LIST = [] #input different temperatures

n = 1
for RANDOM_SEED in RANDOM_SEED_LIST:
    t_index = 1
    for T in T_LIST:
        INCAR = Incar.from_file('INCAR').as_dict()
        INCAR['TEBEG'] = str(T)
        INCAR['TEEND'] = str(T)
        INCAR['RANDOM_SEED'] = RANDOM_SEED
        INCAR = Incar.from_dict(INCAR)
        #input path to working directory
        parent_dir = '/path/to/working/directory' + str(t_index) + '-' + str(T)
        if os.path.exists(parent_dir):
            directory = '0' + str(n) + '-trajectory'
            path = os.path.join(parent_dir, directory)
            print(path)
            os.mkdir(path)
            INCAR.write_file(path + '/INCAR')
            copy('POTCAR', path)
            copy('KPOINTS', path)
            copy('POSCAR', path)
            copy('md.job', path)
        else:
            os.mkdir(parent_dir)
            directory = '0' + str(n) + '-trajectory'
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            INCAR.write_file(path + '/INCAR')
            copy('POTCAR', path)
            copy('KPOINTS', path)
            copy('POSCAR', path)
            copy('md.job', path)
        j = j + 1
    i = i + 1
