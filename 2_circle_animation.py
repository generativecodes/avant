#!/usr/bin/env python3
import avant
from math import sin, cos

x = 0

def setup():
    pass

def loop():
    global x
    x += 0.02
    position_x = SIZE * sin(x)
    position_y = SIZE * cos(x)
    circle(position_x, position_y, radius=SIZE/2)

