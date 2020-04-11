# inspired by fossasia(github) /susi_linux/ui/animators.py
from avant.dependencies import Gtk, GLib, cairo
from avant.code_executer import code_executer

class Animator(Gtk.DrawingArea):
    """Display the Animation with a certain Framerate.

    """

    def __init__(self, path, **properties):
        """initialize Animator and set framerate

        path -- The Filepath to the users code
        **properties -- parameters for the gtk drawingarea
        """
        super().__init__(**properties)
        self.connect("draw", self.draw)
        framerate = 60
        self.set_framerate(framerate)
        # initialise code executer
        self.executer = code_executer(path)
        # runs the user code to assign setup and draw
        self.executer.run()

    def tick(self):
        self.queue_draw()
        return True

    def draw(self, widget, ctx):
        """runs the user-setup() or -draw()"""
        self.executer.display(ctx,
                self.get_allocated_width(),
                self.get_allocated_height())

    def set_framerate(self,fps):
        GLib.timeout_add(1000 / fps, self.tick)
