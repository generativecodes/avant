# dependencies
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
# our stuff gets drawn with :
import cairo

from avant.code_executer import code_executer

# https://blog.fossasia.org/creating-animations-in-gtk-with-pycairo-in-susi-linux-app/
class Animator(Gtk.DrawingArea):
    def __init__(self, path, **properties):
        super().__init__(*properties)
        self.connect("draw", self.do_drawing)
        GLib.timeout_add(16.68, self.tick)

        self.executer = code_executer(path)

        self.path = path
        self.setup_executed = False
        self.executer.run()

    def tick(self):
        self.queue_draw()
        return True

    def do_drawing(self, widget, ctx):
        self.draw(ctx, self.get_allocated_width(),
                       self.get_allocated_height())

    def draw(self, ctx, width, height):
        if not self.setup_executed:
            ctx.set_antialias(cairo.Antialias.BEST)
            self.executer.setup(ctx)
            self.setup_executed = True
        self.executer.loop(ctx)
