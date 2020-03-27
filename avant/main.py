import cairo
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from avant.code_executer import code_executer
from avant.animator import Animator

import sys
from os import path
import __main__

def main():
    # create gtk window
    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)

    # the "real main file" is where avant was imported
    # this finds its path:
    FILEPATH = path.abspath(sys.modules['__main__'].__file__)
    # give the path to Animator for execution
    anim = Animator(FILEPATH)
    # add Animator to Gtk window
    win.add(anim)
    # run gtk
    win.show_all()
    Gtk.main()
