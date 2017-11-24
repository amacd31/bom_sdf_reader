import io
import pandas as pd
import requests

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

class SDFReader(object):

    def __init__(
            self,
            auth,
            server_url = 'http://reg.bom.gov.au',
            site_base = '/water/reg/stf',
            product_base = '/fwo/reg'
        ):

        self.server_url = server_url
        self.site_base = site_base
        self.product_base = product_base
        self.auth = auth
        config_url = '{0}{1}/content/config/site_config.json'.format(self.server_url, site_base)
        self.metadata = requests.get(config_url, auth = self.auth).json()

        self.station_list = []
        self.station_meta = {}
        for station in self.metadata['stations']['features']:
            station_id = station['properties']['awrc_id']

            self.station_list.append(station_id)

            self.station_meta[station_id] = {
                'product_id': station['properties']['product_id'],
            }

    def get_site_info(self, awrc):
        return self.station_meta[awrc]['properties']

    def get_forecast(self, awrc):
        # http://reg.bom.gov.au/fwo/reg/IDV37010/data/403242A/403242A_latest.csv
        forecast_url = '{site}{product_base}/{product_id}/data/{awrc}/{awrc}_latest.csv'.format(**{
            'site': self.server_url,
            'product_base': self.product_base,
            'product_id': self.station_meta[awrc]['product_id'],
            'awrc': awrc
        })
        forecast_csv = io.BytesIO(requests.get(forecast_url, auth = self.auth).content)

        return pd.read_csv(forecast_csv, skiprows=23, index_col='Time', parse_dates=True, na_values=['--'])

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
