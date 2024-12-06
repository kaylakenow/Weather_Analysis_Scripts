#!/usr/bin/env python

import numpy as np
from datetime import datetime, timedelta
import requests
from siphon.catalog import TDSCatalog
import sys


def get_rap_dataset(dt: datetime = datetime.utcnow().replace(microsecond=0,second=0,minute=0)):
    try:
        base_url = 'https://www.ncei.noaa.gov/thredds/catalog/model-rap130anl/'
        cat = TDSCatalog(f'{base_url}{dt:%Y%m}/{dt:%Y%m%d}/catalog.xml')
        print(f'{base_url}{dt:%Y%m}/{dt:%Y%m%d}/catalog.xml')
        ds = cat.datasets.filter_time_range(dt,dt+timedelta(hours=0))[-1]
        ncss = ds.subset()
        print(ncss)
        return ncss
    except requests.exceptions.HTTPError as err:
        try:
            base_url = 'https://www.ncei.noaa.gov/thredds/catalog/model-rap130anl-old/'
            cat = TDSCatalog(f'{base_url}{dt:%Y%m}/{dt:%Y%m%d}/catalog.xml')
            ds = cat.datasets.filter_time_range(dt,dt+timedelta(hours=0))[-1]
            ncss = ds.subset()
            print(ncss)
            return ncss
        except requests.exceptions.HTTPError as err:
            print("Data not available")
            sys.exit()
