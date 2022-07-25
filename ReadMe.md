# Json to pandas

## Run as script

Help:

> python jsons_to_df_pickle_multy_v3.py --help

usage: `jsons_to_df_pickle_multy_v3.py [-h] -i INPUT_FOLDER [-o OUTPUT_FILE] [-e N_EXECUTORS]`
                        
__Example:__

Parse json files from folder `/data/input/`, save to file `output`, run `4` subprocesses

> python jsons_to_df_pickle_multy.py -i /data/input/ -o output -e 4

## Run as function:

> from jsons_to_df_pickle_multy import main
> 
> df = main('/data/input/', 4)
