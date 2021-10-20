"""
    Mū Tōrere a 2 player Maori board game. The game is played on 8 pointed star 
    like board with spaces on each corner point and one point at the center. 
    Program Developed by Cameron    
"""

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from functools import partial
import time
import math
import json
from PIL import Image, ImageTk

bgcolour = ('DarkRed') #instead of writing the background colour each time we will set the variable here.



#Intizaling the program as a function.
def init():

    global scoreboard
    global button_identities
    global root
    #root = tk which is tkinter this will allow me to use root.geometry 
    #to chosse the screen size and root.config to pick a background colour aswell as title.
    
    root = Tk() 
   
    root.title('Mū Tōrere')
    root.geometry('1366x768')
    root.config(bg=bgcolour)

    scoreboard = 0

    button_identities = []

    boardimg = Image.open("Mū tōrere.png") #This is importing the image
    boardimg = ImageTk.PhotoImage(boardimg)

    tk.Label(root,image=boardimg, bg=bgcolour).pack(anchor = N) #creating the image as a label
    
    help()
    checkers() #Will need to call functions here because of the mainloop


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
    #                   1        2          3          4          0        7          6          5          8
    coorddinates = [(751,6), (881,136), (881,316), (751,450), (568,6), (435,136), (435,316), (568,450), (659, 226)] 


    for x,y in coorddinates[:4]:  #creates the button 4 times looping through a while loop / The :4 also means it only grabs the first 4
        global bluechecker_button #creates a global variable of bluechecker_button
        redx = (f"{x}")
        redy = (f"{y}")
        redchecker_button = tk.Button(root, image=redcheck, compound="center", borderwidth=0,  bg=bgcolour, highlightthickness=0)
        redchecker_button['command'] = lambda x=redchecker_button: click(x) 
        redchecker_button.place(x=redx)  #This is where it places on either x or y axis depending on the coordinates from the top list
        redchecker_button.place(y=redy)
        #print (redx)   These are here for testing to make sure it is running smotthly
        #print (redy)
        button_identities.append(redchecker_button)

    for x,y in coorddinates[4:8]: #this also creates the button 4 times with the 4:8 it grapbs the last 4 numberes in the list, It is witten so it won't grab the ninth item in the list.
        global bluechecker_button #creates a global variable of bluechecker_button
        bluex = (f"{x}") #this convents in the list to a tuple by defining the first one x and the other y.
        bluey = (f"{y}") 
        bluechecker_button = tk.Button(root, image=bluecheck, compound="center", borderwidth=0,  bg=bgcolour, highlightthickness=0)
        bluechecker_button['command'] = lambda x=bluechecker_button: click(x)
        bluechecker_button.place(x=bluex)
        bluechecker_button.place(y=bluey)
        button_identities.append(bluechecker_button)
        

    canvas.create_window(0, 0, anchor=N, window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.pack(fill='both', expand=True, side='bottom')
    root.mainloop()

def help():
    help_file = open('helptext.json', 'r') #opens helptext.json file with text for the instructions
    help = json.load(help_file, strict=False) #loads in the Json File
    for Eng in help['english']['text']:    #Searches for the english array then the text object
        Eng_label1 = tk.Label(root, text= "INSTRUCTIONS:", bg=bgcolour, font=('verdana', 40), fg='green')   #creates label with text saying INSTRUCTIONS:
        Eng_label1.place(x=920, y=40)  #places label at these pixels
        Eng_label = tk.Label(root, text= Eng, bg=bgcolour, font=('verdana', 12), fg='green', wraplength=250)  #creates a label withe the instructions with a wrap so it doesn't go off the side
        Eng_label.place(x=980, y=100) #places label at these pixels                               #prints the text object which is the instructions
    for Mao in help['maori']['text']:   #does it with the maori text array
        Mao_label1 = tk.Label(root, text= "TOHUTOHU:", bg=bgcolour, font=('verdana', 40), fg='green')   #creates label with text saying tohutohu:
        Mao_label1.place(x=45, y=40)  #places label at these pixels
        Mao_label = tk.Label(root, text= Mao, bg=bgcolour, font=('verdana', 12), fg='green', wraplength=250)  #creates a label withe the instructions with a wrap so it doesn't go off the side
        Mao_label.place(x=59, y=100) #places label at these pixels

def click(clicked_button): #this function will be run when a checker/stone is clicked
    global scoreboard #this is grabbing the scoreboard function which is scoreboard = 0 since it's out of this fucntion it won't be affected everytime it's re run.
    global bluechecker_button
    print(clicked_button)

    clicked_button.place(x=659)
    clicked_button.place(y=226)
    
    #tk.Button.place (x=659, y=226)
    
    scoreboard += 1  #changing the scoreboard value by 1 everytime it is run.
   # print (scoreboard)
    moves_label = tk.Label(root, text= "Moves:" + str(scoreboard), bg=bgcolour, font=('verdana', 35), fg='pink')  #a tk.label is creating a text under the game showing how many moves "Moves: ___ "
    moves_label.place(x=590, y=500)

    root.mainloop()


#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    init()