#!/usr/bin/python3

import urllib.request
import json
import turtle
import os

# Paths of gifs
cwd = os.getcwd()
map = cwd + "/iss_map.gif"
sprite = cwd + "/spriteiss.gif"


# Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

# Call the webserver
trackiss = urllib.request.urlopen(eoss)

# Put into file object
ztrack = trackiss.read()

# Convert from JSON to python data structure
result = json.loads(ztrack.decode('utf-8'))

# Display pythonic data
print("\n\nConverted Python Data")
print(result)
print("\nISS data retrieve & converted.")

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print(f'\nLatitude: {lat}') # E-W
print(f'Longitude: {lon}')  # N-S

screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set resolution
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic(map)

# My location
yellowlat = 35.5
yellowlon = -97.5
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(10)
mylocation.hideturtle()

# ISS Sprite
screen.register_shape(sprite)
iss = turtle.Turtle()
iss.shape(sprite)
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon,lat)
turtle.mainloop() # <- this line should always be at the bottom of the 
                  #    script to prevent the graphic from closing