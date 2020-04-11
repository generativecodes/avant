import matplotlib.font_manager
import cairo

WIDTH = 0
HEIGHT = 0
SIZE = 0
ctx = None


def print_available_fonts():
    flist = matplotlib.font_manager.get_fontconfig_fonts()
    names = [matplotlib.font_manager
                .FontProperties(fname=fname)
                .get_name() for fname in flist]
    for n in names:
        print(n)

def init_text(w, h, s, c):
    global WIDTH, HEIGHT, SIZE, ctx
    WIDTH = w
    HEIGHT = h
    SIZE = s
    ctx = c


def test():
    ctx.select_font_face("Lato", cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)

    ctx.set_font_size(30)

    glyphs = []
    index = 0

    for y in range(20):
        for x in range(35):
            glyphs.append((index,
                -WIDTH/2 + x*20 + 27, 
                -WIDTH/2 + y*23 + 27))
            index += 1

    ctx.show_glyphs(glyphs)

