from avant.vector import Vector
from avant.settings import *
from math import pi as PI
TWOPI = 2 * PI
PHI = (-1 + sqrt(5))/2


ctx = None

def forms_init_context(context):
    global ctx
    ctx = context

def line(x1, y1, x2, y2):
    y1 = -y1
    y2 = -y2
    ctx.move_to(x1, y1)
    ctx.line_to(x2, y2)
    apply_stroke_and_fill(ctx)

def arc(x, y, radius, start, end):
    y = -y
    ctx.arc(x, y, radius, start, end)
    apply_stroke_and_fill(ctx)

def polygon(x, y, radius, edges, rotation):
    #edges = abs(round(edges))
    if edges is 0:
        arc(x, y, radius, 0, TWOPI)
    elif edges is 1:
        arc(x, y, 1, 0, TWOPI)
    elif edges is 2:
        v1 = Vector(x-radius,y)
        v1.rotate(rotation)
        v2 = Vector(x+radius,y)
        v2.rotate(rotation)
        print(v1,v2,v1.x)
        line(v1.x, v1.y, v2.x, v2.y)
    else:
        y=-y
        ctx.save()
        ctx.translate(x, y)
        ctx.new_path()
        angle = TWOPI / edges
        v = Vector.from_angle(rotation - PI/2)
        v = v*radius
        ctx.move_to(v.x, v.y)
        for i in range(edges):
            v.rotate(angle)
            ctx.line_to(v.x,v.y)
        ctx.close_path()
        apply_stroke_and_fill(ctx)
        ctx.restore

def circle(x=0, y=0, radius=None):
    if radius is None:
        radius = size()
    arc(x,y,radius,0,TWOPI)

def point(x=0,y=0):
    circle(x,y, radius=0.1)

def hexagon(x=0, y=0, radius=None, rotation=None):
    if radius is None:
        radius = size()
    if rotation is None:
        rotation = 0
    polygon(x,y,radius,6,rotation)

def pentagon(x=0, y=0, radius=None, rotation=None):
    if radius is None:
        radius = size() * PHI * PHI
    if rotation is None:
        rotation = 0
    polygon(x,y,radius,5,rotation)

def square(x=0, y=0, radius=None, rotation=None):
    if radius is None:
        radius = size() / sqrt(2)
    if rotation is None:
        rotation = 0
    polygon(x,y,radius,4,rotation)

def triangle(x=0, y=0, radius=None, rotation=None):
    if radius is None:
        radius = size() / sqrt(3)
    if rotation is None:
        rotation = 0
    polygon(x,y,radius,3,rotation)

