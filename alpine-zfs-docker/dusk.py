# Source: https://sunrisesunset.io/api/

### Setup
# python3 -m venv .venv
# source .venv/bin/activate
# pip list
# pip install --upgrade pip
# pip install requests

### Usage
# from datetime import datetime
# from dusk import dusk
# dusk = dusk()
# datetime.now() > dusk
#   False


import requests
from datetime import datetime

def dusk():
    # Sidney, IL
    lat =  40.0224345 # Required field
    lng = -88.0787767 # Required field
    timezone = 'CST'  # (Optional) defaults to lat and lng timezone / can also use America/Chicago
    date = 'today'    # (Optional) defaults to today / tomorrow or YYYY-MM-DD are other options
    
    url = f'https://api.sunrisesunset.io/json?lat={lat}&lng={lng}'
    data = requests.get(url).json()
    
    dusk_tuple = data['results']['dusk'].split(' ')[0].split(':')
    dusk_datetime = datetime.now().replace(hour = int(dusk_tuple[0])+12, minute = int(dusk_tuple[1]), second = 0)
    return dusk_datetime 

if __name__ == '__main__':
    print(dusk().strftime('%a %Y-%m-%d %H:%M:%S'))
