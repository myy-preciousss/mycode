#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
from prettyprinter import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def name_finder(got_list):
        names = []
        for name in got_list:
                got_name_resp = requests.get(name)
                got_name_dj   = got_name_resp.json()
                names.append(got_name_dj['name'])
        return names

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        # pprint.pprint(got_dj)

        ## Challenge 01: Return the house(s) affiliated with the character 
        ## looked up, along with a list of books they appear in
        character_name = got_dj["name"]
        alias = got_dj["aliases"]
        print(f"\nYou looked up {character_name}, also known as {alias[0]}.")
        
        print(f"\n{character_name} belongs to the following houses: ")
        for allegiance in name_finder(got_dj.get("allegiances")):
                print(allegiance)

        print(f"\n{character_name} also appears in the following books:")

        for book in name_finder(got_dj.get("books")):
                print(book)
        

if __name__ == "__main__":
        main()

