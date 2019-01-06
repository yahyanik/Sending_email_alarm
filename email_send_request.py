from __future__ import division

from datetime import datetime
import requests
import datetime


def main():
    url = 'http://0.0.0.0:80'
    local_filename = url.split('/')[-1]+str(datetime.datetime.now())
    r = requests.get(url)

if __name__ == '__main__':
    main()
