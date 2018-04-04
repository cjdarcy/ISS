#!/usr/bin/env python3

# A Python 3 script that utilizes urllib3 and pygeocoder to pull
# the most recent ISS location data from the Open-Notify.org API.

import time
import urllib3
import json
from pygeocoder import Geocoder
from pygeocoder import GeocoderError

# Starting a PoolManager instance to make simple requests
http = urllib3.PoolManager()

# Making a request to the Open-Notify API
r = http.request('GET', 'http://api.open-notify.org/iss-now.json')

# Decoding and deserializing JSON data
obj = json.loads(r.data.decode('utf-8'))

# Assigning latitude and longitude variables to make things easier
latitude = obj['iss_position']['latitude']
longitude = obj['iss_position']['longitude']

# Printing the timestamp & ISS location data
print('Timestamp: ' + time.ctime(int(obj['timestamp'])))
print('Latitude: ' + str(latitude))
print('Longitude: ' + str(longitude))

# Reverse geocoding voodoo magic, now with 100% more error handling
try:
    location = Geocoder.reverse_geocode(latitude, longitude)
    print('Location: ' + str(location))
except GeocoderError:
    print('The coordinates could not be reverse geocoded.')    
