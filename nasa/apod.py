#!/usr/bin/python3
import requests
import json
import os

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/planetary/apod?"

cwd = os.getcwd()
creds = cwd + "/creds/nasa.creds"

def main():
    ## Define creds
    with open(creds) as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    # nasacreds = "api_key=DEMO_KEY"
    ## Call the webservice with our key
    apodresponse = requests.get(NASAAPI + nasacreds)

    ## decode JSON to Python data structure
    apod = apodresponse.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()

