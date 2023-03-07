from multiprocessing import Pool, RLock
from pathlib import Path
from tqdm import tqdm
from src.jsons_to_pandas import one_process_execution
import pandas as pd


def jsons2pandas(jsons_folder_path, N_GROUPS=8):
    """
    Преобразует множество json файлов из  папки jsons_folder_path в единый pd.DataFrame используя N_GROUPS подпроцессов

    :param jsons_folder_path: Folder with jsons files
    :param N_GROUPS: N executors for multyprocessing
    :return: union pd.DataFrame
    """

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

    return res_df
