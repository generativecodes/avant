#!/usr/bin/env python3

from avant import *


# https://blog.fossasia.org/creating-animations-in-gtk-with-pycairo-in-susi-linux-app/
class Animator(Gtk.DrawingArea):
    def __init__(self, win, path, **properties):
        super().__init__(*properties)
        self.win = win
        self.connect("draw", self.do_drawing)
        GLib.timeout_add(TWOPI, self.tick)
        ##GLib.timeout_add(16.68/2, self.tick)
        self.path = path
        self.setup_executed = False
        global setup
        global loop
        code = ["global setup\n",
                "global loop \n"]
        with open(self.path) as f:
            code += [line for line in f]
            loopindex = code.index("def loop(ctx):\n") +1
            code.insert(loopindex, "    ctx.translate(width/2, height/2)\n")
            code.insert(loopindex, "    height = surface.get_height()\n")
            code.insert(loopindex, "    width = surface.get_width()\n")
            code.insert(loopindex, "    surface = ctx.get_target()\n")
            code = "".join(code)
        exec(code, globals(), locals())
        self.setup = setup
        self.loop = loop

    def tick(self):
        self.queue_draw()
        return True

    def do_drawing(self, widget, ctx):
        self.draw(ctx, self.get_allocated_width(),
                       self.get_allocated_height())

    def draw(self, ctx, width, height):
        forms_init_context(ctx)
        settings_init_context(ctx)
        if not self.setup_executed:
            ctx.set_antialias(cairo.Antialias.BEST)
            self.setup(ctx)
            self.setup_executed = True
        self.loop(ctx)

    def on_button_press(self, w, event):
        if event.type == Gdk.EventType.BUTTON_PRESS:
            self.queue_draw();
