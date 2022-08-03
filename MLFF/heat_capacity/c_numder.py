from pymatgen.io.vasp.outputs import Oszicar
import numpy as np

TMIN = #min temperature
TMAX = #max temperature
TSTEP = #step
start_step = #number of equilibration steps
nb_of_formula = #supercell size, e.g. 2*2*2
wd = '/path/to/working/directory/'
conv = 1.602e-19 #eV to Joules
na = 6.02e23 #avogadro constant

T_master = []
E_master = []

def T_parse():
    T_list = [step['T'] for step in steps]
    T = sum(T_list)/len(T_list)
    T_master.append(T)

def E_parse():
    F_array = np.array([step ['F'] for step in steps]) #in eV
    KE_array = np.array([step['EK'] for step in steps]) #in eV
    F = np.mean(F_array)
    KE = np.mean(KE_array)
    E = F + KE
    E = E/nb_of_formula #in eV/formula_unit
    E_master.append(E)

def numerical_der(xlist, ylist):
    yprime = np.diff(ylist)/np.diff(xlist)
    xprime = []
    for i in range(len(yprime)):
        xtemp = (xlist[i+1]+xlist[i])/2
        xprime = np.append(xprime, xtemp)
    return xprime, yprime

for T in range(TMIN, TMAX+1, TSTEP):
    steps = Oszicar(wd + str(T) + '/OSZICAR').ionic_steps[start_step:]
    T_parse()
    E_parse()

tprime, C = numerical_der(T_master, E_master)
C = C*conv*na #in J/(K.mol.formula_unit)
    
np.savetxt('c_numder.txt', np.array([tprime, C]))
