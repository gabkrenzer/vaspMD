# The importance of benchmarking
The only way you can have confidence in the results produced by a newly training MLFF is by benchmarking it.
There are two ways to benchmarking an MLFF:
1. Against data that was seen during training.
2. Against data that was not seen during training.
Good practice involves first benchmarking against seen data. Once satisfied, one should then proceed to test against 
unseen data. Note that this is the only way to build true confidence in the MLFF. 

## Workflow

### Seen Data
1. Run `parse_regfile.sh`, which greps useful data and prints the number of DFT calculations performed 
(also a good indicator).
2. .Run `mae_rmse.py`, which prints the errors.

### Unseen Data
