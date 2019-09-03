#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Apr 06, 2019 03:14:10 PM IST  platform: Windows NT


import nltk
from tabulate import tabulate
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize 
import numpy as np
import pandas as pd
from gensim.models import word2vec
from gensim import corpora
from gensim import models
from gensim import similarities
import csv

import json
import collections
import operator
import re

import sys
global z
global output
global output1

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

import unknown5_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    sys.stdout.flush()
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown5_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown5_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 14 -weight bold"

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=-0.022, height=831, width=1380)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#0d0819")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"similardisplay.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=self._img0)
        #self.Label1.configure(text='''Label''')
        
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.059, rely=0.044, height=51, width=304)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(font=font9)
        self.Label2.configure(width=304)
        self.Label2.configure(text=z)

        ##THis is trial


        trainrecipts = json.load(open('train.json','r'))

        sentences = list()
        # one hot ingredients


        for recipt in trainrecipts:
            clean_recipt = list()
            # I want ingredient remove 
            for ingredient in recipt['ingredients']:
                # remove this description from the ingredients
                # minimal preprocessing
                ingredient =  re.sub(r'\(.*oz.\)|crushed|crumbles|ground|minced|powder|chopped|sliced',
                                     '', 
                                     ingredient)
                clean_recipt.append(ingredient.strip())
            sentences.append(clean_recipt)
                
        len(sentences)

        # Set values for NN parameters
        num_features = 300    # Word vector dimensionality                      
        min_word_count = 3    # 50% of the corpus                    
        num_workers = 4       # Number of CPUs
        context = 10          # Context window size; 
                              # let's use avg recipte size                                                                                  
        downsampling = 1e-3   # threshold for configuring which 
                            # higher-frequency words are randomly downsampled

        # Initialize and train the model 
        model = word2vec.Word2Vec(sentences, workers=num_workers, \
                    size=num_features, min_count = min_word_count, \
                    window = context, sample = downsampling)

        # If you don't plan to train the model any further, calling 
        # init_sims will make the model much more memory-efficient.
        model.init_sims(replace=True)

        #output=model.most_similar('broccoli', 'bacon')
        output1=model.most_similar('broccoli')
        print(output1)

        sample = open("ingrlist.csv", "r") 
        s = sample.read() 
        f = s.replace("'", " ") 
        data = []

        
        for i in sent_tokenize(f): 
            temp = []
        
            for j in word_tokenize(i): 
                temp.append(j) 
            data.append(temp)

##        trainrecipts = json.load(open('train.json','r'))
##        sentences = list()
##        for recipt in trainrecipts:
##            clean_recipt = list()
##            # I want ingredient remove 
##            for ingredient in recipt['ingredients']:
##                # remove this description from the ingredients
##                # minimal preprocessing
##                ingredient =  re.sub(r'\(.*oz.\)|crushed|crumbles|ground|minced|powder|chopped|sliced',
##                             '', 
##                             ingredient)
##                clean_recipt.append(ingredient.strip())
##        sentences.append(clean_recipt)
##        print(sentences)
        num_features = 1000
        context = 1
        downsampling = 1e-3
        model = word2vec.Word2Vec(data , size=num_features, window = context, sample = downsampling)
##        num_features = 300    # Word vector dimensionality                      
##        min_word_count = 3    # 50% of the corpus                    
##        num_workers = 4       # Number of CPUs
##        context = 10          # Context window size; 
##                              # let's use avg recipte size                                                                                  
##        downsampling = 1e-3

##        model = word2vec.Word2Vec(sentences, workers=num_workers, \
##            size=num_features, min_count = min_word_count, \
##            window = context, sample = downsampling)
        global output
##        output=model.most_similar('u feta cheese')
        output=model.most_similar(z)

        with open('filename.csv', 'w') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(output1)
            
##        a = zip(*csv.reader(open("filename.csv", "r")))
##        csv.writer(open("filename.csv", "w")).writerows(a)

        with open("filename.csv") as f:
            a=f.read()
        print(a)
        t=a.replace(',','\n')
        print(t)
        
        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.051, rely=0.204, relheight=0.732
                   , relwidth=0.376)
        self.Listbox1.configure(background="#e2d7de")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font9)
        self.Listbox1.configure(foreground="black")
        self.Listbox1.configure(width=514)
        self.Listbox1.configure(borderwidth=0)
        i=1
        for line in t.splitlines():
            self.Listbox1.insert(i,line)
            i=i+1
##        with open("filename.csv",errors='ignore', newline = "") as file:
##            reader = csv.reader(file)
##
##            # r and c tell us where to grid the labels
##            r = 0
##            for row in reader:
##               c = 0
##               for col in row:
##                  # i've added some styling
##                  self.label = tk.Label(top, wraplength = 500, height = 3, \
##                                        text = col,bg="#d9d9d9")
##                  self.label.grid(row = c, column = r)
##                  c += 1
##               r += 1

            
    
##        self.Label2 = tk.Label(top)
##        self.Label2.place(relx=0.1, rely=0.74, height=61, width=294)
##        self.Label2.configure(background="#d9d9d9")
##        self.Label2.configure(disabledforeground="#a3a3a3")
##        self.Label2.configure(foreground="#000000")
##        self.Label2.configure(width=194)
##        self.Label2.configure(text=output)

    
    
if __name__ == '__main__':
    vp_start_gui()





