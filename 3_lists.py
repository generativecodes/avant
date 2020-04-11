#!/usr/bin/env python3
from avant import *

t = timer(warp=2.5)

vectors = [Vector(pos_x,0) for pos_x in range(-5,6)]

def setup():
    fill(0,0,0)

def loop():
    global t
    t.tick()
    x = t.get()

    for v in vectors:
        circle( v.x * SIZE * 0.25,
                v.y + SIZE * 0.25 * sin(x+v.x),
                radius=(SIZE * 0.02))
