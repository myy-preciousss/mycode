#!/usr/bin/python3
"""opening a static file containing JSON data | Alta3 Research"""

# JSON is part of the Python Standard Library
import json
from prettyprinter import pprint

def main():
    """runtime code"""
    ## open the file
    with open("jsondata\datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    ## display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))           
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")            

    ## Create the JSON string
    datacenterdecoded = json.loads(datacenterstring)

    ## This is now a dictionary
    print(type(datacenterdecoded))

    ## display the servers in the datacenter
    pprint(datacenterdecoded)

    ## display the servers in row3
    print("\nServers in row 3")
    pprint(datacenterdecoded["row3"])

    ## display the 2nd server in row2
    print("\n2nd server from row 2")
    pprint(datacenterdecoded["row2"][1])

    ## write code to
    ## display the last server in row3
    print("\nLast server in row 3")
    pprint(datacenterdecoded["row3"][3])

if __name__ == "__main__":
    main()

