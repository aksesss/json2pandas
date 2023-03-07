import pickle
import time
from src.arg_parser import get_arg_pareser
from src.main import jsons2pandas


if __name__ == '__main__':
    start_time = time.time()

    args = get_arg_pareser().parse_args()

    # input params
    N_GROUPS = args.n_executors
    jsons_folder_path = args.input_folder
    output_file = args.output_file

    res_df = jsons2pandas(jsons_folder_path, N_GROUPS)

    # save
    with open(output_file, 'wb') as f:
        pickle.dump(res_df, f)

    print(f'Executed in {(time.time() - start_time)/60} min')
