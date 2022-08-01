#!/bin/bash -l

#submit single-point calculations with MLFF and DFT
for T in #new_temperatures_directories
do 
	echo $T
	mkdir $T 
	cp INCAR_MLFF KPOINTS POTCAR ML_FF mlff_sp.job $T
        cp INCAR_DFT dft_sp.job $T
        cp structures/${T}POSCAR* $T
	cd $T
        for NUM in {0..199}
	do
		echo $NUM
		mkdir $NUM
		cp INCAR_MLFF KPOINTS POTCAR ML_FF mlff_sp.job $NUM
		mv ${T}POSCAR$NUM $NUM/POSCAR
		mv INCAR_MLFF INCAR
		mkdir ${NUM}/DFT
	        cp dft_sp.job ${NUM}/DFT
                cp INCAR_DFT ${NUM}/DFT/INCAR
  		cd $NUM
		qsub mlff_sp.job
		cp POSCAR KPOINTS POTCAR DFT
		cd DFT
		qsub dft_sp.job
		cd ../..
	done
	cd ..
done
