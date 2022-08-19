#!/bin/bash -l

#submit single-point calculations with MLFF and DFT
for T in #new_temperatures_directories
do 
	echo $T
	mkdir $T 
	cp INCAR_MLFF KPOINTS POTCAR ML_FF mlff_sp.job $T #update with MLFF single-point job name
        cp INCAR_DFT dft_sp.job $T #update with DFT single-point job name
        cp structures/${T}POSCAR* $T
	cd $T
        for NUM in {0..XXX} #XXX is the number of structures per temperature (n_seed*sample) minus 1
	do
		echo $NUM
		mkdir $NUM
		cp INCAR_MLFF KPOINTS POTCAR ML_FF mlff_sp.job $NUM #update with MLFF single-point job name
		mv ${T}POSCAR$NUM $NUM/POSCAR
		mv INCAR_MLFF INCAR
		mkdir ${NUM}/DFT
	        cp dft_sp.job ${NUM}/DFT #update with DFT single-point job name
                cp INCAR_DFT ${NUM}/DFT/INCAR
  		cd $NUM
		qsub mlff_sp.job #update with MLFF single-point job name
		cp POSCAR KPOINTS POTCAR DFT
		cd DFT
		qsub dft_sp.job #update with DFT single-point job name
		cd ../..
	done
	cd ..
done
