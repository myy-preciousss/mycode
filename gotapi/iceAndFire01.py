#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
from prettyprinter import pprint

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    pprint(got_dj)
    
    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
    print("\n", got_dj.keys())
    

if __name__ == "__main__":
    main()

