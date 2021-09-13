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
from PIL import Image, ImageTk

bgcolour = ('SkyBlue') #instead of writing the background colour each time we will set the variable here.

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
    
    
    

    checkers() #Will need to call functions here because of the mainloop
    root.mainloop() 


def checkers():
    global root #grabbing the global variable root
    blue = 0
    red = 0
    canvas = tk.Canvas(root, bg=bgcolour, relief="flat", highlightthickness=0)
    frame = tk.Frame(canvas, bg=bgcolour, relief="flat")
    bluecheck= Image.open("bluecircle50.png")   #Opens the image
    bluecheck = ImageTk.PhotoImage(bluecheck)   
    redcheck= Image.open("redcircle50.png")
    redcheck = ImageTk.PhotoImage(redcheck)
    while blue < 4:
        #creates the button 4 times looping through a while loop
        bluechecker_button = tk.Button(image=bluecheck, compound="center", borderwidth=0,  bg=bgcolour, command=click)
        bluechecker_button.pack()
        blue += 1 #This changes the blue variable so the while loop will eventaully stop
    while red < 4:
        redchecker_button = tk.Button(image=redcheck, compound="center", borderwidth=0, bg=bgcolour, command=click, highlightthickness=0)
        redchecker_button.place(x=760, y=0)
        red += 1
    canvas.create_window(0, 0, anchor=N, window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.pack(fill='both', expand=True, side='bottom')
    root.mainloop()


def click():
    print("clicked")

#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    init()
    