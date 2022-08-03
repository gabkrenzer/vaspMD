#code to be used on michael
from pymatgen.io.vasp.outputs import Oszicar
import numpy as np

TMIN = #min temperature
TMAX = #max temperature
TSTEP = #step
start_step = #number of equilibration steps
wd = '/path/to/working/directory/'

T_master = []
dev_master = []

for T in range(TMIN, TMAX+1, TSTEP):
    steps = Oszicar(wd + str(T) + '/OSZICAR').ionic_steps[start_step:]
    T_arr = np.array([step['T'] for step in steps])
    T = np.mean(T_arr)
    T_master.append(T)
    std = np.std(T_arr)
    dev_master.append(std)
    
np.savetxt('tdev.txt', np.array([T_master, dev_master]))
