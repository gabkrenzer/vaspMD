#!/bin/bash -l
#submit all AIMD jobs

for T in temperature_directory_names
do 
	echo $T
	cd $T
	for NUM in trajectory_number 
	do
		echo $NUM	
		cd $NUM-trajectory
		qsub md.job
		cd ../
	done
	cd ../	
done
