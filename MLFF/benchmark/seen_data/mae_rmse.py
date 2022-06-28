#!/bin/python
import numpy as np

def rmse(dft, ml):
    return np.sqrt(((dft - ml) ** 2).mean())

def mae(dft, ml):
    return np.sum(np.abs(dft -  ml))/len(dft)

E = np.loadtxt('E_reg.dat')
F = np.loadtxt('F_reg.dat')
S = np.loadtxt('Stress_reg.dat')

#norms of forces
F_dft = np.sum(np.abs(F[:,0].reshape((-1,3)))**2,axis=-1)**(1./2)
F_ml = np.sum(np.abs(F[:,1].reshape((-1,3)))**2,axis=-1)**(1./2)


print("     MAE ,        RMSE,          max (absolute) error")
print("energy (meV/at.):")
print( "{:10.4f}".format(1000*mae(E[:,0], E[:,1]) ),
       "{:10.4f}".format(1000*rmse(E[:,0], E[:,1])),
       "{:10.4f}".format(1000*max(np.abs(E[:,0] - E[:,1]))) )
print("stress (kbar):")
print( "{:10.4f}".format(mae(S[:,0], S[:,1])),
       "{:10.4f}".format(rmse(S[:,0], S[:,1])),
       "{:10.4f}".format(max(np.abs(S[:,0] - S[:,1]))) )
print("force components (eV/A):")
print( "{:10.4f}".format(mae(F[:,0], F[:,1])),
       "{:10.4f}".format(rmse(F[:,0], F[:,1])),
       "{:10.4f}".format(max(np.abs(F[:,0] - F[:,1]))) )
print("force norm (eV/A):")
print( "{:10.4f}".format( mae(F_dft, F_ml) ),
       "{:10.4f}".format(rmse(F_dft, F_ml)),
       "{:10.4f}".format(max(np.abs(F_dft - F_ml))))
