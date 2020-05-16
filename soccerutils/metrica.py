import pandas as pd
import requests
import csv
from io import StringIO


def metrica_to_pandas(fh, teamname):
    data = fh.content.decode('utf8')

    reader = csv.reader(data.split('\n'), delimiter=',')
    teamnamefull = next(reader)[3].lower()
    jerseys = [x for x in next(reader) if x != '']
    columns = next(reader)
    for i, j in enumerate(jerseys):
        columns[i*2+3] = "{}_{}_x".format(teamname, j)
        columns[i*2+4] = "{}_{}_y".format(teamname, j)
    columns[-2] = "ball_x"
    columns[-1] = "ball_y"

    return pd.read_csv(
        StringIO(data), names=columns, index_col='Frame', skiprows=3)


def merge_tracking_data(home, away):
    return home.drop(
        columns=['ball_x', 'ball_y']).merge(
            away, left_index=True, right_index=True)


def build_tracking(home_url, away_url, as_list=True):
    home_data = requests.get(url=home_url)
    away_data = requests.get(url=away_url)

    home_frames = metrica_to_pandas(home_data, 'home')
    away_frames = metrica_to_pandas(away_data, 'away')

    merged = merge_tracking_data(home_frames, away_frames)

    if as_list:
        return merged.to_dict(orient='records')
    else:
        return merged
