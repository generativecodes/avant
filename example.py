#!/usr/bin/env python3
from avant import *


def test_function():
    print("hello test")

def setup(ctx):
    global t
    t = 0

def loop(ctx):
    global t
    t = (t + (TWOPI/360)) % TWOPI
    fill(0,0,0)
    from math import sin, cos
    angle = TWOPI/6
    size = min(width,height)/16
    for i in range(6):
        x = size * sin(t + angle * i)
        y = size * cos(t + angle * i)
        arc(3*x, 3*y, size, 0, TWOPI)
        arc(6*y, 6*x, size,0,TWOPI)

