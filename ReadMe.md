# Json to pandas

## Run as script

Help:

> python jsons_to_df_pickle_multy.py --help

usage: `jsons_to_df_pickle_multy.py [-h] -i INPUT_FOLDER [-o OUTPUT_FILE] [-e N_EXECUTORS]`
                        
__Example:__

Parse json files from folder `/data/input/`, save to file `output.pickle`, run `4` subprocesses

> python jsons_to_df_pickle_multy.py -i /data/input/ -o output.pickle -e 4

## Run as function:

> from jsons_to_df_pickle_multy import main
> 
> df = main('/data/input/', 4)
