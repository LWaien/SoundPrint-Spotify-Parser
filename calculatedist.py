from geopy.geocoders import Nominatim

import math

try:
    geolocator = Nominatim(user_agent="calculatedist")
    home = geolocator.geocode("Amherst",timeout=None)
except:
    print("geolocator is not working")
    pass

def getDist(lat,long):
    try:
        distance = calculateDist(lat, long, home.latitude, home.longitude)
        return distance
    except:
        return None

def calculateDist(lat1, lon1, lat2, lon2):
    # Earth's radius in miles
    radius = 3959

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = round(radius * c)

    return distance