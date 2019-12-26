#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 06:43:38 2019

@author: jasonervin
"""
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter.ttk import * 
import re

root = Tk()
root.title('ContactSeeker')

#*** Body ***
bod = Frame(root)
bod.pack()

        
def phoneSeeker():
    """Scrapes url provided by user and creates a txt file"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features="html5lib")
    [s.extract() for s in soup('script')]
    ro = re.compile(r'''(
                    (\d{3} | \(\d{3}\))?
                    (\s|-|\.)?
                    \d{3}
                    (\s|-|\.)
                    \d{4}
                    )''', re.VERBOSE)
                    
    mo = ro.findall(data)
    
    for i in range(len(mo)):
        content = str(mo[:][i][0]) + ','
        i = i + 1
        file = open('Phonefile.txt', 'a')
        file.write(str(content))
        file.close()
    
    
    
def emailSeeker():
    """Scrapes url provided by user and creates a txt file"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features="html5lib")
    [s.extract() for s in soup('script')]
    ro = re.compile(r'mailto:\S+@\w+\.\w+', re.IGNORECASE)
    mo = ro.findall(data)
    
    for i in range(len(mo)):
        content = str(mo[i]) + ','
        i = i + 1
        file = open('Emailfile.txt', 'a')
        file.write(str(content))
        file.close()

#*** Label ***
UrlLabel = Label(bod, text='Please enter URL here:')

#*** Blank ***
UrlEntry = Entry(bod)
UrlEntry.insert(INSERT, 'Enter URL Here')
UrlEntry.pack()
UrlEntry.grid(row=1, column=1)

#*** Buttons ***
UrlSubmit = Button(bod, text='Phone Number', command=phoneSeeker)
UrlSubmit2 = Button(bod, text='Email', command=emailSeeker)
UrlCancel = Button(bod, text='Close', command=root.destroy)
UrlSubmit.grid(row=1, column=3)
UrlSubmit2.grid(row=1, column=4)
UrlCancel.grid(row=1, column=5)

root.mainloop()