#!/bin/bash -l

steps =  #nb of steps or NSW

for T in #temperature directories
do
        grep BEEF ${T}/ML_LOGFILE | tail -n ${steps} | awk '{print $4}' > BEEF${T}.dat
        #grep BEEF ${T}/sequential_run2/ML_LOGFILE | tail -n ${steps} | awk '{print $4}' >> BEEF${T}.dat - use as many as there are sequential runs
done
