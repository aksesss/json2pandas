from tqdm import tqdm
from pathlib import Path
import json
from multiprocessing import Pool, RLock
import pandas as pd
import pickle
import argparse
import time


def one_process_execution(pid, f_paths):

    res_arr = []
    indexes = []

    tqdm_text = '#' + f'{pid}'.zfill(3)
    with tqdm(total=len(f_paths), position=pid+1, desc=tqdm_text) as pbar:
        for path in f_paths:
            with open(str(path), 'r') as f:
                d = json.load(f)

                indexes.append(path.stem)
                res_arr.append(d)

                pbar.update(1)
    df = pd.json_normalize(res_arr).assign(index=indexes).set_index('index')
    print(f'Subproc {pid} done')
    return df


def get_arg_pareser():

    parser = argparse.ArgumentParser(description='From json files creates pd.DataFrame')
    parser.add_argument('-i', '--input-folder', type=str,
                        help='input data folder', required=True)
    parser.add_argument('-o', '--output-file', type=str, default=r'output.pickle', 
                        help='output.pickle')
    parser.add_argument('-e', '--n-executors', type=int, default=8, 
                        help='number of subprocesses (default: 8)')
    return parser


def main(jsons_folder_path, N_GROUPS=8):

    # get file paths
    f_paths = list(Path(jsons_folder_path).glob('*.json'))
    in_group = len(f_paths) // N_GROUPS + 1

    # split data
    inp_args = [f_paths[i:i + in_group] for i in range(0, len(f_paths), in_group)]
    inp_args = list(enumerate(inp_args))

    # init pool
    pool = Pool(processes=N_GROUPS, initializer=tqdm.set_lock, initargs=(RLock(),))
    jobs = [pool.apply_async(one_process_execution, args=x) for x in inp_args]

    # run pool
    df_lists = list(map(lambda x: x.get(), jobs))

    # union
    res_df = pd.concat(df_lists)

    return (res_df)


if __name__ == '__main__':
    start_time = time.time()

    args = get_arg_pareser().parse_args()

    # input params
    N_GROUPS = args.n_executors
    jsons_folder_path = args.input_folder
    output_file = args.output_file

    res_df = main(jsons_folder_path, N_GROUPS)

    # save
    with open(output_file, 'wb') as f:
        pickle.dump(res_df, f)

    print(f'Executed in {(time.time() - start_time)/60} min')
