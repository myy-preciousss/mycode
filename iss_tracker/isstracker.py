# API challenge ISS
import json
from prettyprinter import pprint
import requests
import reverse_geocoder as rg
from time import strftime, localtime

URL = "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(URL).json()

    # Get Timestamp
    epoch = resp["timestamp"]
    local = strftime('%Y-%m-%d %H:%M:%S', localtime(epoch))

    # Get coordinates
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    coords_tuple = (lat, lon)
    location = rg.search(coords_tuple, verbose=False) #Returns as a list/ordered dict
    country = location[0]["cc"]
    city = location[0]["name"]

    # pprint(location)

    print("CURRENT LOCATION OF ISS:")
    print(f'> Timestamp: {local}')
    print(f"> Lon: {lon}")
    print(f"> Lat: {lat}")
    print(f"> City/Country: {city}, {country}")

if __name__ == "__main__":
    main()

