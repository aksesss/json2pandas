# Json to pandas

Преобразует множество json файлов в единый pandas.DataFrame используя мультипроцессинг в разрезе файлов. В качестве
результата работы скрипта выступает pickle-файл с pandas.DataFrame

## Run as script

Help:

> python jsons_to_df_pickle_multy.py --help

usage: `jsons_to_df_pickle_multy.py [-h] -i INPUT_FOLDER [-o OUTPUT_FILE] [-e N_EXECUTORS]`
                        
__Example:__

Parse json files from folder `/data/input/`, save to file `output.pickle`, run `4` subprocesses

> python jsons_to_df_pickle_multy.py -i /data/input/ -o output.pickle -e 4

## Run as function:

> from src.main import jsons2pandas
> 
> df = jsons2pandas('/data/input/', 4)
