from avant.dependencies import Gtk, GLib, cairo
from avant.code_executer import code_executer

# https://blog.fossasia.org/creating-animations-in-gtk-with-pycairo-in-susi-linux-app/
class Animator(Gtk.DrawingArea):
    """A class; run the animation-loop."""

    def __init__(self, path, **properties):
        super().__init__(*properties)
        self.connect("draw", self.do_drawing)
        GLib.timeout_add(16.68, self.tick)
        self.executer = code_executer(path)
        self.executer.run()

    def tick(self):
        self.queue_draw()
        return True

    def do_drawing(self, widget, ctx):
        self.draw(ctx, self.get_allocated_width(),
                       self.get_allocated_height())

    def draw(self, ctx, width, height):
        self.executer.setup_(ctx)
        self.executer.loop_(ctx)
