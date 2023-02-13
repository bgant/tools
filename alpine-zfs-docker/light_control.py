
from datetime import datetime
from dusk import dusk
from FrontOutsideLights import FrontOutsideLights

dusk = dusk()
if dusk < datetime.now() < datetime.now().replace(hour = 21):
   print("Turning front outside lights ON")
   FrontOutsideLights('ON')   # Turn lights ON after Dusk and before 9PM
else:
   print("Turning front outside lights OFF")
   FrontOutsideLights('OFF')

