#!/usr/bin/python3
"""The json.dumps() function creates a JSON string | Alta3 Research"""

# JSON is part of the Python Standard Library
import json
from prettyprinter import pprint

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print("Type: ", type(hitchhikers))
    pprint(hitchhikers)

    ## Create the JSON string
    jsonstring = json.dumps(hitchhikers)

    ## Display a single string of JSON
    print("Type: ", type(jsonstring))
    pprint(jsonstring)

if __name__ == "__main__":
    main()

