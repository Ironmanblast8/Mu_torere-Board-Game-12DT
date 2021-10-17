"""
    Mū Tōrere a 2 player Maori board game. The game is played on 8 pointed star 
    like board with spaces on each corner point and one point at the center. 
    Program Developed by Cameron    
"""

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time
import math
import json
from PIL import Image, ImageTk

bgcolour = ('DarkRed') #instead of writing the background colour each time we will set the variable here.

#Intizaling the program as a function.
def init():

    global root
    #root = tk which is tkinter this will allow me to use root.geometry 
    #to chosse the screen size and root.config to pick a background colour aswell as title.
    
    root = tk.Tk() 
   
    root.title('Mū Tōrere')
    root.geometry('1366x768')
    root.config(bg=bgcolour)
        
    boardimg = Image.open("Mū tōrere.png") #This is importing the image
    boardimg = ImageTk.PhotoImage(boardimg)

    tk.Label(root,image=boardimg, bg=bgcolour).pack(anchor = N) #creating the image as a label
    
    
    
    help()
    checkers() #Will need to call functions here because of the mainloop
    root.mainloop() 


def checkers():
    global root #grabbing the global variable root
    canvas = tk.Canvas(root, bg=bgcolour, relief="flat", highlightthickness=0)  #Creating a canvas for tkinter modules
    frame = tk.Frame(canvas, bg=bgcolour, relief="flat")
    bluecheck= Image.open("bluecircle50.png")   #Opens the image
    bluecheck = ImageTk.PhotoImage(bluecheck)   
    redcheck= Image.open("redcircle50.png")
    redcheck = ImageTk.PhotoImage(redcheck)
    # The board representation is
    #       0  1
    #    7       2
    #        8
    #    6       3
    #      5   4
    # where each number reates to the coordinates from 1 - 4 clockwise and 0 - 5 anticlockwise
    # 8 Is not in the starting coords
    coorddinates = [(751,6), (881,136), (881,136), (751,450), (568,6), (435,136), (435,136), (568,450)] 

    for x,y in coorddinates[4:]:
        print(f"x={x}, y={y}")

    for num in range(4,8): # will only grab the last 4 from the coordinates not doing 5:8 from the list cause it starts at 0 not 1
        #creates the button 4 times looping through a while loop
        bluechecker_button = tk.Button(image=bluecheck, compound="center", borderwidth=0,  bg=bgcolour, command=click)
        #bluechecker_button.place(x=coorddinates_x[num])
        #bluechecker_button.place(y=coorddinates_y[num])
    for num in range(4):
        redchecker_button = tk.Button(image=redcheck, compound="center", borderwidth=0, bg=bgcolour, command=click, highlightthickness=0)
        #redchecker_button.place(x=coorddinates_x[num])
        #redchecker_button.place(y=coorddinates_y[num])
    canvas.create_window(0, 0, anchor=N, window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.pack(fill='both', expand=True, side='bottom')
    root.mainloop()

def help():
    help_file = open('helptext.json', 'r')
    help = json.load(help_file, strict=False)
    for i in help['english']['text']:
        print(i)

def click():
    print("clicked")

#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    init()