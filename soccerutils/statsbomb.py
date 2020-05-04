import requests
import pandas as pd
import numpy as np

base_url = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/"


def get_matches(competition_id: int, season_id: int, url=base_url):
    """
    Returns a list of all StatsBomb games in specified competition/season.
    """
    comp_url = base_url + "matches/{}/{}.json"
    return requests.get(url=comp_url.format(competition_id,
                                            season_id)).json()


def get_events(competition_id: int = None,
               season_id: int = None,
               match_id: int = None,
               url=base_url):
    """
    Returns a list of all StatsBomb events in specified competition/season
    or match_id.
    """

    assert competition_id != match_id,\
        "Set either (competition_id, season_id) or match_id"

    match_url = base_url + "events/{}.json"

    if match_id is None:
        matches = get_matches(competition_id, season_id, base_url)
        match_ids = [m['match_id'] for m in matches]
    else:
        match_ids = [match_id]

    events = []
    for match_id in match_ids:
        for e in requests.get(url=match_url.format(match_id)).json():
            events.append(e)

    return events


def events_to_pandas(events: list):
    """
    Returns a Pandas DataFrame of a list of raw StatsBomb Events

    TODO: Incorporate tactics_lineup, related_events, and shot_freee_frames.
    TODO: Configure auth for StatsBomb API requests
    """

    df = pd.json_normalize(events, sep='_')

    location_columns = [x for x in df.columns.values if 'location' in x]
    for col in location_columns:
        for i, dimension in enumerate(["x", "y"]):
            new_col = col.replace("location", dimension)
            df[new_col] = df.apply(
                lambda x: x[col][i] if type(x[col]) == list else None, axis=1)

    df = df[[c for c in df.columns if c not in location_columns]]

    columns_to_remove = ['tactics_lineup',
                         'related_events',
                         'shot_freeze_frame']

    return df[[c for c in df.columns if c not in columns_to_remove]]
