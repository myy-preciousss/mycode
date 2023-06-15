#!/usr/bin/env python3

import requests

url =  "https://cat-fact.herokuapp.com/facts"

resp = requests.get(url).json()

for fact in resp:
    print(fact["text"])
