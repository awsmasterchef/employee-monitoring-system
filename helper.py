import json
import os
from datetime import datetime, timedelta


def dt2str(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def date_from_webkit(webkit_timestamp, tz):
    """Convert webkit(utc) to local datetime"""
    epoch_start = datetime(1601, 1, 1)
    delta = timedelta(hours=tz, microseconds=int(webkit_timestamp))
    return epoch_start + delta


def read_config_file(key: str):
    with open(f"config.json", "r") as file:
        data = json.load(file)
    return data.get(key, None)

