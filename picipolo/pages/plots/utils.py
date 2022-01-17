from pathlib import Path
import pandas as pd


def load_data() -> pd.DataFrame:
    file_path = Path(__file__).resolve()
    data_path = file_path.parents[3].joinpath(
        'data', 'user_data', 'parsed', 'messengerData.csv')
    df = pd.read_csv(data_path, delimiter=';')
    df['time'] = pd.to_datetime(df['time'])
    return df


def load_path_fonts():
    file_path = Path(__file__).resolve()
    data_path = file_path.parents[3].joinpath('data', 'fonts', 'Symbola.ttf')
    return data_path.as_posix()
