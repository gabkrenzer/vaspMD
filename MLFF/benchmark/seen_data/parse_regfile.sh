#!/bin/bash
#Number of ref. structs (DFT calcs):
N_conf=$(grep -A2 'The number of configurations' ML_ABN |tail -n1 |awk '{print $1}')
echo "Number of DFT calcs:"
echo $N_conf
N_at=$(grep -A2 'The maximum number of atoms per system' ML_ABN |tail -n1| awk '{print $1}')
echo "Number of atoms:"
echo $N_at


#Energies, converted to eV/at., fix awk precision
grep -A $((N_conf+1)) 'Total energies (eV)' ML_REG |tail -n $N_conf |awk -v x=$N_at '{print $1/x" "$2/x}' > E_reg.dat
#Forces
grep -A $((3*N_at*N_conf+1)) 'Forces (eV ang.^-1)' ML_REG |tail -n $((3*N_at*N_conf)) >F_reg.dat
#Stresses (in some weird order: XX XY ZX YY YZ ZZ)
grep -A $((6*N_conf+1)) 'Stress (kbar)' ML_REG |tail -n $((6*N_conf)) > Stress_reg.dat
