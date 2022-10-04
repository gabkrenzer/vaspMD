from pymatgen.io.vasp.outputs import Oszicar
import numpy as np

TMIN = #min temperature
TMAX = #max temperature
TSTEP = #step
start_step = #number of equilibration steps
nb_of_formula = #supercell size, e.g. 2*2*2
conv = 1.602e-19 #eV to Joules
na = 6.02e23 #Avogadro constant
kb = 8.617e-5 #Boltzmann constant in eV/K
wd = '/path/to/working/directory/'

T_master = []
E_ms_master = []
E_sm_master = []

def T_parse():
    T_list = [step['T'] for step in steps]
    T = sum(T_list)/len(T_list)
    T_master.append(T) 
    
def E_parse():
    F_array = np.array([step ['F'] for step in steps]) #in eV
    KE_array = np.array([step['EK'] for step in steps]) #in eV
    E_array = F_array + KE_array
    return E_array

for T in range(TMIN, TMAX+1, TSTEP):
    steps = Oszicar(wd + str(T) + '/OSZICAR').ionic_steps[start_step:]
    T_parse()
    E_sm = np.mean(E_parse())**2
    E_sm_master.append(E_sm)
    E_s_array = np.array([E**2 for E in E_parse()])
    E_ms = np.mean(E_s_array)
    E_ms_master.append(E_ms)

C_array = (np.array(E_ms_master)-np.array(E_sm_master))/(kb*np.array(T_master)**2) #in eV/K
C_array = C_array*conv*na/nb_of_formula #in J/(K.mol.formula_unit)
    
np.savetxt('c_mssm.txt', np.array([T_master, C_array]))
