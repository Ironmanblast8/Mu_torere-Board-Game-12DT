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

scoreboard = 0

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
    # 8 Is not in the starting coords, The bottem line isn't 0-7 so I've put number to represent
    #                   1        2          3          4          0        7          6          5
    coorddinates = [(751,6), (881,136), (881,316), (751,450), (568,6), (435,136), (435,316), (568,450)] 

    for x,y in coorddinates[:4]:  #creates the button 4 times looping through a while loop / The :4 also means it only grabs the first 4
        redx = (f"{x}")
        redy = (f"{y}")
        redchecker_button = tk.Button(image=redcheck, compound="center", borderwidth=0, bg=bgcolour, command=click, highlightthickness=0)     
        redchecker_button.place(x=redx)  #This is where it places on either x or y axis depending on the coordinates from the top list
        redchecker_button.place(y=redy)
        print (redx)
        print (redy)

    for x,y in coorddinates[4:]: #this also creates the button 4 times with the 4: it grapbs the last 4 numberes in the list
        bluex = (f"{x}") #this convents in the list to a tuple by defining the first one x and the other y.
        bluey = (f"{y}") 
        bluechecker_button = tk.Button(image=bluecheck, compound="center", borderwidth=0,  bg=bgcolour, command=click, highlightthickness=0)
        bluechecker_button.place(x=bluex)
        bluechecker_button.place(y=bluey)

    canvas.create_window(0, 0, anchor=N, window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.pack(fill='both', expand=True, side='bottom')
    root.mainloop()

def help():
    help_file = open('helptext.json', 'r')
    help = json.load(help_file, strict=False)
    for Eng in help['english']['text']:
        print(Eng)
    for Mao in help['maori']['text']:
        print(Mao)


def click(): #this function will be run when a checker/stone is clicked
    global scoreboard #this is grabbing the scoreboard function which is scoreboard = 0 since it's out of this fucntion it won't be affected everytime it's re run.
    global bluechecker_button
    print("clicked")

    tk.Button.place (x=659, y=226)
    
    scoreboard += 1  #changing the scoreboard value by 1 everytime it is run.
    print (scoreboard)
    moves_label = tk.Label(root, text= "Moves:" + str(scoreboard), bg=bgcolour, font=('verdana', 35), fg='pink')  #a tk.label is creating a text under the game showing how many moves "Moves: ___ "
    moves_label.place(x=590, y=500)

#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    init()