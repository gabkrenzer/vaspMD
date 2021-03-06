# The importance of benchmarking
The only way you can have confidence in the results produced by a newly trained Machine Learning Force Field (MLFF) is by benchmarking it. There are two ways to benchmark an MLFF:
1. Against data that was _seen_ during training.
2. Against data that was _not seen_ during training.

Good practice involves first benchmarking against seen data. Once satisfied, the only way to build true confidence in an MLFF is by testing it against unseen data. To do so, one has to build a new data set from _ab initio_ Molecular Dynamics (AIMD) using different random seeds.

# Workflow

## Seen Data
1. Run `parse_regfile.sh`, which greps useful data and prints the number of DFT calculations performed 
(also a good indicator on whether the MLFF has been trained enough or not).
2. Run `mae_rmse.py`, which prints Mean solute Errors (MAE), Root Mean Squared Errors (RMSE), and Maximum Absolute Errors (MaxAE) on energies, forces, and stresses.

## Unseen Data
1. Run `incars.py` to prepare AIMD simulations with different random seeds at different temperatures. 
2. Run `mega_sub.sh`, which is an example submission script.
3. Once the AIMD simulations are finished, run `rng_structures.py` to randomly select structures from the AIMD simulations at each temperature.
4. Store the structure files in directory `structures` in the working directory.
5. Prepare new input files to run single-point calculations.
6. Run `sp.sh`, which is an example submission script to submit single-point calculations using the MLFF and DFT.
7. Once the single-point calculations are finished, run `grep_fe.sh` to grep forces and energies.
8. Run `parse_fe.py` to write energies and forces into files.
9. Run `mae_rmse.py` to calculate MAE, RMSE, and MaxAE on energies and forces.

## Further Benchmarking
Further benchmarking is encouraged.  For instance, one can benchmark an MLFF against the harmonic phonon dispersion, mean square displacements, or radial distribution functions.

# Acknowledgments 
`parse_regfile.sh` and `mae_rmse.py` are adapted from codes that were initially written by Johan Klarbring.
