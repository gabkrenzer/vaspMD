#prepare INCARs with different RANDOM_SEEDs at diffrent temperatures

import os
from shutil import copy
from pymatgen.io.vasp.inputs import Incar

TMIN = #min temperature
TMAX = #max temperature
TSTEP = #step
wd = '/path/to/working/directory/'

for T in range(TMIN, TMAX+1, TSTEP):
    INCAR = Incar.from_file('INCAR').as_dict()
    INCAR['TEBEG'] = str(T)
    INCAR['TEEND'] = str(T)
    INCAR = Incar.from_dict(INCAR)
    dir = wd + str(T)
    os.mkdir(dir)
    INCAR.write_file(dir+ '/INCAR')
    copy('POTCAR', dir)
    copy('ML_FF', dir)
    copy('KPOINTS', dir)
    copy('POSCAR', dir)
    copy('md.job', dir)
