# Mehmet Alp Aysan

import json
import urllib3
import re

api_key = "i8F30cTGqhtmtUAdxa2TBrf9wr9GMuGZ" # "eauUGxjZkDMdh3HSNEur6IHsMBw9uvW4" Alp API

def getWeatherInfo(type):

    # find current location lat and lon
    http = urllib3.PoolManager()
    url = 'http://ipinfo.io/json'
    response = http.request('GET', url)
    res = json.loads(response.data.decode('utf-8'))
    # print(res)
    coord = (res['loc'])
    pattern = r"(.*),(.*)"

    location = re.findall(pattern,coord)
    # print(location)
    if len(location) < 1:
        print("Cannot extract geolocation!")
        return None
    lat = location[0][0]
    lon = location[0][1]

    # print(lat,lon)

    # find the location key for that location (AccuWeather API)

    url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=' + api_key + '&q=' + lat + '%2C' + lon + '&language=en-us&details=false&toplevel=false'
    response = http.request('GET',url)
    res = json.loads(response.data.decode('utf-8'))
    # print(res)

    if 'Key' not in res:
        print("API Cannot get Weather Data for the Location")
        return None

    # print(res['Key'])
    location_key = res['Key']

    # find the temp data from the given location key

    url = "http://dataservice.accuweather.com/currentconditions/v1/" + location_key + '?apikey=' + api_key + '&language=en-us&details=false'
    response = http.request('GET', url)
    res = json.loads(response.data.decode('utf-8'))
    # print(res)
    # print(res[0]['Temperature'])

    if type == 'C':
        result = res[0]['Temperature']['Metric']['Value']
    elif type == 'F':
        result = res[0]['Temperature']['Imperial']['Value']
    else:
        return None

    return round(result, 0)

print(getWeatherInfo('C'))