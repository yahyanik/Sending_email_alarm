from __future__ import division

from datetime import datetime
import requests
import datetime

def request():
    url = 'http://0.0.0.0:81'
    local_filename = url.split('/')[-1]+str(datetime.datetime.now())
    r = requests.get(url)


