#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 20, 2019 09:36:55 PM IST  platform: Windows NT

import sys
import unknown2

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

def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

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

def display():
     unknown2.create_Toplevel1(root)

##def callbackFunc(self):
##     #print("New Element Selected")
##     print(unknown1.s.get())


if __name__ == '__main__':
    import unknown1
    unknown1.vp_start_gui()





