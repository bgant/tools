
from datetime import datetime
from dusk import dusk
from FrontOutsideLights import FrontOutsideLights
from time import sleep

if datetime.now() > datetime.now().replace(hour = 21): 
    print("Turning front outside lights OFF")
    FrontOutsideLights('OFF')     # Turn lights OFF after 9PM
else:
    dusk = dusk()
    while datetime.now() < dusk:
        sleep(600)  # Wait 10 Minutes 
    else:
        print("Turning front outside lights ON")
        FrontOutsideLights('ON')  # Turn lights ON after Dusk

