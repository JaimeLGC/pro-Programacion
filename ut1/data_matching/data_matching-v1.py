import pandas as pd

input_path = './data_shortening/eval_data_short.csv'
output_path = './data_matching/eval_data_match.csv'


def match_rows(path: str):
    file = pd.read_csv(path, nrows=21)
    file['id-2, ACTIVIDAD-TAREA-2, CNO-2'] = ''
    for i, row in file.iterrows():
        file.at[i, 'id-2'] = row.iloc[0]
        file.at[i, 'ACTIVIDAD-TAREA-2'] = row.iloc[1]
        file.at[i, 'CNO-2'] = row.iloc[2]

    return file.to_csv(output_path)


eval_short = match_rows(input_path)
