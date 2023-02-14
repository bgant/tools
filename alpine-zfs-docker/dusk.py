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


'''
>>> data
{'results': 
  {'sunrise':     '6:57:30 AM', 
   'sunset':      '5:17:54 PM', 
   'first_light': '5:25:21 AM', 
   'last_light':  '6:50:03 PM', 
   'dawn':        '6:29:11 AM', 
   'dusk':        '5:46:14 PM', 
   'solar_noon': '12:07:42 PM', 
   'golden_hour': '4:39:06 PM', 
   'day_length': '10:20:24', 
   'timezone': 'CST'}, 
'status': 'OK'}

>>> data['results'].keys()
dict_keys(['sunrise', 'sunset', 'first_light', 'last_light', 'dawn', 'dusk', 'solar_noon', 'golden_hour', 'day_length', 'timezone'])
'''

