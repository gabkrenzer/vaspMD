#!/usr/bin/env python
#parser that randomly selects structures in an XDATCAR file and write the corresponding energies and forces to a file
#this code is written to go over different independent trajectories carried out at different temperatures

import random
import numpy as np
from pymatgen.io.vasp.outputs import Xdatcar, Oszicar
from ase.io.vasp import read_vasp_out

nsw = #number of steps in XDATCAR
sample = #number of structures needed per trajectory
temp_list = [] #input temperatures
n_seed = #number of trajectories per temperature
path ='/path/to/working/directory/with/trajectories'

#random number generator
def rng(nsw, sample):
    random_list = []
    i = 0
    while i < sample:
        n = random.randrange(0, nsw)
        if n not in random_list:
            random_list.append(n)
            i = i + 1
    return random_list

#parser
#XDATCAR is in path/0${t_index}-${temp}K/0${seed}-trajectory
t_index = 1
for temp in temp_list:
    print('TEMPERATURE:', temp)
    temp_dir = '/0' + str(t_index) + '-' + str(temp) + 'K'
    k = 0
    for seed in range(1, n_seed + 1):
        print('TRAJECTORY:', seed)
        traj_dir = '/0' + str(seed) + '-trajectory'
        full_path = path + temp_dir + traj_dir
        xdat = '/XDATCAR'
        struct_list = Xdatcar(full_path + xdat).structures
        for n in rng(nsw, sample):
            struct_list[n].to('poscar', str(temp) + 'POSCAR' + str(k))
            print(str(k)+ ': structure number ' + str(n) + ' written to file' )
            k = k + 1
    t_index = t_index + 1
