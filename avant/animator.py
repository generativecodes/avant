from avant.dependencies import Gtk, GLib, cairo
from avant.code_executer import code_executer

class Animator(Gtk.DrawingArea):
    """Display the Animation with a certain Framerate.

    This is inspired by:
    github:     @fossasia
    repo:       susi-linux
    path:       /susi_linux/ui/animators.py
    license:    Apache-2.0
    """

    def __init__(self, path, **properties):
        """initialize Animator and set framerate

        path -- The Filepath to the users code
        **properties -- parameters for the gtk drawingarea
        """
        super().__init__(*properties)
        self.connect("draw", self.do_drawing)
        self.set_framerate(60)
        # initialise code executer
        self.executer = code_executer(path)
        # "compiles" the user code
        self.executer.run()

    def tick(self):
        self.queue_draw()
        return True

    def do_drawing(self, widget, ctx):
        self.draw(ctx, self.get_allocated_width(),
                       self.get_allocated_height())

    def draw(self, ctx, width, height):
        """executes the user writen setup() or draw()"""
        self.executer.display(ctx,width,height)

    def set_framerate(self,fps):
        GLib.timeout_add(1000 / fps, self.tick)
