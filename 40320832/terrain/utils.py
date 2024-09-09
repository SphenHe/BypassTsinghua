#!/usr/bin/env python3

from PIL import Image
import numpy as np
import json
import gzip
import sys
from os.path import join, isfile

PREFIX = './data/weather/'

def read_data():

    for f in ['terrain.tif', 'terrain.metadata.json', 'wind.json.gz', 'precipitation.json.gz']:
        path = join(PREFIX, f)
        if not isfile(path):
            print(f'Data {path} not found, please run ./data/fetch.sh', file=sys.stderr)
            exit(1)

    print("Reading terrain...")
    with Image.open(join(PREFIX, 'terrain.tif')) as terrain_raw:
        terrain_data = np.array(terrain_raw)

    print("Reading terrain metadata...")
    with open(join(PREFIX, 'terrain.metadata.json')) as f:
        terrain_metadata = json.load(f)

    print("Reading wind...")
    with gzip.open(join(PREFIX, 'wind.json.gz')) as f:
        wind = json.load(f)

    print("Reading precipitation...")
    with gzip.open(join(PREFIX, 'precipitation.json.gz')) as f:
        precipitation = json.load(f)

    return {
        "terrain": {
            "metadata": terrain_metadata,
            "data": terrain_data,
        },
        "wind": wind,
        "precipitation": precipitation,
    }


if __name__ == "__main__":
    data = read_data()
    print(list(data.keys()))

