from avant.dependencies import Gtk
from avant.animator import Animator

import sys
from os import path
import __main__

def main():
    """Run the necessary UI tools for ɅVɅNT."""

    # create gtk window
    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)

    # the "initial main file" is where avant was imported
    # this finds its path:
    path_ = path.abspath(sys.modules['__main__'].__file__)
    # give the path to Animator for execution
    anim = Animator(path_)
    # add Animator to Gtk window
    win.add(anim)
    # run gtk
    win.show_all()
    Gtk.main()
