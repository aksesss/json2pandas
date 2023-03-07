from tqdm import tqdm
import json
import pandas as pd


def one_process_execution(pid: int, f_paths: list) -> pd.DataFrame:
    """
    Прогонка группы json файлов с преобразованием в pd.DataFrame в едином процессе

    :param pid: Номер подпроцесса
    :param f_paths: Список путей до файла
    :return: pd.DataFrame
    """

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
