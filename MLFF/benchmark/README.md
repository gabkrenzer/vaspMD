# The importance of benchmarking
The only way to have confidence in the results produced by a newly trained Machine Learning Force Field (MLFF) is by benchmarking it. There are two ways to benchmark an MLFF:
1. Against data that was _seen_ during training.
2. Against data that was _not seen_ during training.

Good practice involves first benchmarking against seen data. Once satisfied, the only way to build true confidence in an MLFF is by testing it against unseen data. To do so, one has to build a new data set from _ab initio_ Molecular Dynamics (AIMD), or MLFF-MD, using different random seeds. As a final check, one should also look at the Bayesian errors of the production runs.

# Workflow

## Seen Data
Run in you working directory:
1. `parse_regfile.sh`, which greps useful data and prints the number of DFT calculations performed 
(also a good indicator on whether the MLFF has been trained enough or not).
2. `mae_rmse.py`, which prints Mean solute Errors (MAE), Root Mean Squared Errors (RMSE), and Maximum Absolute Errors (MaxAE) on energies, forces, and stresses.

## Unseen Data
There are two ways to generate the unseen data with random seeds: from AIMD, or from MLFF-MD. Intuition suggests that AIMD will generate structures that are more different from the training configurations than MLFF-MD. Nevertheless, MLFF-MD is significantly cheaper and should be used where AIMD is too expensive, or does not allow to generate long-enough simulation times. Random seeds are used to explore more of the potential surface and obtain a wider variety of structures.
1. Run `incars.py` to prepare AIMD/MLFF-MD simulations with different random seeds at different temperatures. Assumes all standard input files are in your working directory.
2. Run `mega_sub.sh`, which is an example submission script.
3. Once the AIMD/MLFF-MD simulations are finished, run `rng_structures.py` to randomly select structures from the AIMD/MLFF-MD simulations at each temperature.
4. Store all the structure files in directory `structures` in the working directory.
5. Prepare new input files to run single-point calculations. Example INCARs are attached as `INCAR_DFT` and `INCAR_MLFF`. Note that DFT parameters must be same as the ones used during the training. 
6. Run `sp.sh`, which is an example submission script to submit single-point calculations using the MLFF and DFT.
7. Once the single-point calculations are finished, run `grep_fe.sh` to grep forces and energies.
8. Run `parse_fe.py` to write energies and forces into files.
9. Run `mae_rmse.py` to calculate MAE, RMSE, and MaxAE on energies and forces.

## Further Benchmarking
Further benchmarking is encouraged.  For instance, one can benchmark an MLFF against the harmonic phonon dispersion, mean square displacements, or radial distribution functions.

## Production Runs
It is recommended to check the Bayesian errors of the production runs. Run `BEEFgrep.sh` in your working directory and plot the Bayesian errors in the notebook exemple. 

# Acknowledgments 
`parse_regfile.sh` and `mae_rmse.py` are adapted from codes that were initially written by Johan Klarbring.
