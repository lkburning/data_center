import csv

import requests


def read_from_request(url: str, **kwargs):
    result = requests.get(url)
    if result.status_code == 200:
        return None
    return result.text


def read_csv(path):
    pass
