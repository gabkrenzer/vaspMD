#!/bin/bash -l 

L = #number_of_atoms + 1

for T in #new_temeprature_directories
do
	cd $T
	for NUM in {0..199}
	do 
		cd $NUM
		grep TOTAL-FORCE -A ${L} OUTCAR > positions-forces.dat
		grep -oP "(?<=E0= ).{0,16}" OSZICAR > energy.dat
		cd DFT
		grep TOTAL-FORCE -A ${L} OUTCAR > positions-forces.dat
                grep -oP "(?<=E0= ).{0,16}" OSZICAR > energy.dat
		cd ../..
	done
	cd ..
done
