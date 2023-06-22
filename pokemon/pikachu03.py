#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

from prettyprinter import pprint
import os
import json

ITEMURL = "https://pokeapi.co/api/v2/item/"
POKEURL = "https://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return all
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=2050")
    items = items.json()

    # create a list to store items with the word searched on
    matchedwords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the search word
        if args.searchword in item.get("name"):
            # if TRUE, add that item to the end of list matchedwords
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    ## list all words containing matched word
    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    pprint(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    cwd = os.getcwd()
    itemsdf.to_excel(f"{cwd}/pokemonitems.xlsx", index=False)

    ## Code Customization -b
    ## Export a list of all pokemon as plaintext, JSON, & Excel
    pokemon = requests.get(f"{POKEURL}?limit=1281")
    # print(f"Pokemon HTTP: {type(pokemon)}")
    pokemon = pokemon.json()
    poke_names = []

    for poke in pokemon["results"]:
        poke_names.append(poke["name"])
    
    poke_df = pandas.DataFrame(poke_names)

    # print(f"Pokemon JSON: {type(pokemon)}")
    # print(f"Poke_names: {type(poke_names)}")
    # print(f"Poke DF: {type(poke_df)}")
    
    ## To plaintext
    poke_df.to_csv(f"{cwd}/pokemonlist.csv", index=False)
    
    ## To JSON
    with open(f"{cwd}/pokemonlist.csv", 'w') as jsonfile:
        jsonfile.write(json.dumps(poke_names))
    
    ## To Excel
    poke_df.to_excel(f"{cwd}/pokemonlist.xlsx", index=False)

    ## Code Customization -e
    
    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('--searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()

