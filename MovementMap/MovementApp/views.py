from django.http import HttpResponseRedirect
from django.shortcuts import render
# import ukpostcodeutils
# from geopy.geocoders import Nominatim
# import geopy
# import geocoder

# Create your views here.
import json
from name_dict import get_name_dict

dict = {'map': 'total'}


def index(request):
    # dict = {'map': 'total'}
    return render(request, 'MovementApp/index.html', context=dict)


def search(request):
    return render(request, 'MovementApp/search.html')


def submit(request):
    global dict

    ward_name = request.GET.get('ward-name', 'Failed').capitalize()
    # if ukpostcodeutils.validation.is_valid_postcode(ward_name):

    # lat_lng_coords = None
    # while (lat_lng_coords is None):
    #   g = geocoder.google(ward_name)
    #   lat_lng_coords = g.latlng
    # latitude = lat_lng_coords[0]
    # longitude = lat_lng_coords[1]
    # print(latitude, longitude)

    # geolocator = Nominatim(user_agent="MovementApp")
    # location = geolocator.geocode(ward_name)
    # coord = location.latitude, location.longitude
    # print(coord)
    male_bool = request.GET.get('male', 'False')
    female_bool = request.GET.get('female', 'False')
    # print("q" + male_bool + 'q')
    # print(type(male_bool), male_bool, type(female_bool), female_bool)
    if male_bool == 'True' and female_bool == 'True':
        dict = {'map': 'total'}
    elif male_bool == 'True' and female_bool == 'False':
        # print('Male!!!')
        dict = {'map': 'male'}
    elif female_bool == 'True' and male_bool == 'False':
        dict = {'map': 'female'}
    else:
        dict = {'map': 'total'}

    return_dict = get_name_dict()
    # my_dict = {"ward_data": return_dict[ward_name]}
    return render(request, 'MovementApp/index.html', context=dict)


def search_submit(request):
    params = request.GET.get('ward-name', 'Failed')
    print(params)
    with open('result.json') as f:
        txt = f.read()
    text = json.loads(txt)
    wards = text["features"]
    l = []
    for dic in wards:
        new_dict = {"Name": dic["properties"]["wd16nm"], "ID": dic["properties"]["wd16cd"],
                    "Coordinates": dic["geometry"]["coordinates"][0][0]}
        l.append(new_dict)
    # print(l)
    my_dict = {'ward_data': [x for x in l if x['Name'] == params][0]}
    print(my_dict)
    return render(request, 'MovementApp/search.html', context=my_dict)
# submit(0)
