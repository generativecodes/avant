#!/usr/bin/env python3
import avant
from math import sin, cos

t = timer(warp=5)

def setup():
    fill(0,0,0)

def loop():
    global t
    t.tick()
    x = t.get()
    pos_x = SIZE * sin(x)
    pos_y = SIZE * cos(x)
    circle(pos_x, pos_y*sin(x), radius = SIZE/3)
