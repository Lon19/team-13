import requests
from shapely.geometry import Point
from shapely.geometry import Polygon
from geopy.geocoders import Nominatim


def fetch_all():
    url = 'http://www.nomisweb.co.uk/api/v01/dataset/NM_162_1.jsonstat.json?date=latest&Gender=0,1,2&Age=11,12'
    return requests.get(url).json()


def gel_location(address):
    geolocator = Nominatim('Looking for address...')
    location = geolocator.geocode(address)
    lat, lon = location.latitude, location.longitude
    return Point(lat, lon)


def is_in_polygon(point, points):
    return Polygon(points).contains(point)


