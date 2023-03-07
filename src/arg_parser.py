import argparse


def get_arg_pareser():
    """
    Обработчик параметров командной строки
    :return:
    """
    parser = argparse.ArgumentParser(description='From json files creates pd.DataFrame')
    parser.add_argument('-i', '--input-folder', type=str,
                        help='input data folder', required=True)
    parser.add_argument('-o', '--output-file', type=str, default=r'output.pickle',
                        help='output.pickle')
    parser.add_argument('-e', '--n-executors', type=int, default=8,
                        help='number of subprocesses (default: 8)')
    return parser
