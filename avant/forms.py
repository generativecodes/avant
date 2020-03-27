from avant.vector import Vector
from avant.settings import *
from math import pi as PI
TWOPI = 2 * PI

ctx = None


def forms_init_context(context):
    global ctx
    ctx = context

def line(x1, y1, x2, y2):
    ctx.move_to(x1, y1)
    ctx.line_to(x2, y2)
    apply_stroke_and_fill(ctx)

def arc(x, y, radius, start, end):
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

