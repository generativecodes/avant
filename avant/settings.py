fill_val = (1,1,1,1)
stroke_val = (0,0,0,1)

ctx = None

def settings_init_context(context):
    global ctx
    ctx = context

def stroke(r,g,b,a=1):
    global stroke_val
    stroke_val = (r,g,b,a)

def no_stroke():
    global stroke_val
    stroke_val = None

def fill(r,g,b,a=1):
    global fill_val
    fill_val = (r,g,b,a)

def no_fill():
    global fill_val
    fill_val = None

def apply_stroke_and_fill(ctx):
    if(stroke_val):
        ctx.set_source_rgba(stroke_val[0],
                            stroke_val[1],
                            stroke_val[2],
                            stroke_val[3])
        if(fill_val):
            ctx.stroke_preserve()
        else:
            ctx.stroke()

    if(fill_val):
        ctx.set_source_rgba(fill_val[0],
                            fill_val[1],
                            fill_val[2],
                            fill_val[3])
        ctx.fill()

