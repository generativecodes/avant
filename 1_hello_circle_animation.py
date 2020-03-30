#!/usr/bin/env python3
import avant
from math import sin

x = 0

def setup():
    no_fill()

def loop():
    global x
    x += TWOPI/180
    for i in range(round(10*((sin(x)+1)/2))):
        circle(radius=(i*SIZE*phi*phi*phi))
