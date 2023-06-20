from geopy.geocoders import Nominatim
import geopy.distance
import math

geolocator = Nominatim(user_agent="calculatedist")
home = geolocator.geocode("232 N East St, Amherst")

def getDist(location):
    try:
        loc = geolocator.geocode(location)
        distance = calculateDist(loc.latitude, loc.longitude, home.latitude, home.longitude)
        return distance
    except:
        return None

def calculateDist(lat2,lon2,lat1,lon1):
    c1 = (lat1,lon1)
    c2 = (lat2,lon2)
    return geopy.distance.geodesic(c1, c2).miles