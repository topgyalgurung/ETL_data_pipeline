'''
from json file to dict to pandas df
'''

import pandas as pd
import json
from pandas.io.json import json_normalize


def convert_json_to_dict(filename):
    """ Convert json file to python dictionary
    """
    with open(filename, 'r') as JSON:
        json_dict = json.load(JSON)
    return json_dict


def convert_dict_to_df(filename):
    """ Convert python dictionary to pandas dataframe
    """
    return pd.json_normalize(convert_json_to_dict(filename))