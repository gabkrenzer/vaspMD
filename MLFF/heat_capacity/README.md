# Heat Capacity Calculations From Molecular Dynamics
The heat capacity can be extracted from Molecular Dynamics (MD) simulations run at different temperatures using two different methods:
1. Computing the numerical derivative of energy, $E$, with respect to temperature, $T$: $C=\frac{dE}{dT}$.
2. Using the analytical solution from statistcal mechanics: $C_{v}=\frac{\langle E^2 \rangle-\langle E \rangle^2}{k_{B}T^2}$.

Both methods should give similar results.
  
# Workflow
A case study including example files is provided with the jupyter notebook, please check it out for more details on how to post-process the data.
  
1. Run `incars.py` in your working directory to prepare directories for MD runs. Note that to reduce noise and improve accuracy, a sensible `TSTEP` is required. Large cells and long simulation times may be required too. Such long simulations times may only be accessible using machine-learning-force-fields.
2. Submit jobs.
3. Once the calculations are finished, run `tdev.txt` to obtain the standard deviation from mean temperatures of the MD runs. Then, visualise thermal fluctuations in the jupyter notebook. You may need to increase the temperature resolution (`TSTEP`) and go back to 1. If the temperature resolution (`TSTEP`) you chose in 1. is equal or superior to the suggested temperature resolution, then you can proceed to 4.
4. Obtain the heat capacity data runnning `c_numder.py` and/or `c_analytical.py` using the `TSTEP` suggested from thermal fluctuations.
5. Visualise, compare, and smooth the heat capacity data using the jupyter notebook.
  
# Acknowledgments
This workflow was developed with the help of Kasper Tolborg and Johan Klarbring. 
