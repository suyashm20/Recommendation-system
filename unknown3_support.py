#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Apr 06, 2019 02:35:06 PM IST  platform: Windows NT

import sys
import unknown1
import unknown4

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def pair():
     unknown1.create_Toplevel1(root)

def similar():
     unknown4.create_Toplevel1(root)
    

if __name__ == '__main__':
    import unknown3
    unknown3.vp_start_gui()




