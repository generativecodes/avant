# dependencies
import cairo
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

# dependencies from python standart library
from math import *
PI=pi
TWOPI=2*pi

from avant.Vector import Vector
from avant.settings import *
from avant.forms import *
from avant.animator import Animator

import sys
from os import path
import __main__
FILEPATH = path.abspath(sys.modules['__main__'].__file__)
#with open(FILEPATH) as code:
#    code = [line for line in code]
#    code =  "".join(code)
#    exec(code, globals(), locals())
win = Gtk.Window()
win.connect('destroy', Gtk.main_quit)
global setup
global draw
drawingarea = Animator(win, FILEPATH)
#drawingarea.setup = setup
#drawingarea.loop = loop
win.add(drawingarea)
win.show_all()
Gtk.main()
