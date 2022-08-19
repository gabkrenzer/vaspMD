#!/bin/bash -l
#submit all AIMD/MLFF-MD jobs

for T in #temperature_directory_names
do 
	echo $T
	cd $T
	for NUM in #n_seed
	do
		echo $NUM	
		cd $NUM-trajectory
		qsub md.job #update with job name
		cd ../
	done
	cd ../	
done
