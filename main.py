"""
    Mū Tōrere a 2 player Maori board game. The game is played on 8 pointed star 
    like board with spaces on each corner point and one point at the center. 
    Program Developed by Cameron    
"""

import tkinter as tk
from tkinter import *
import time
import math
from PIL import Image, ImageTk

#Intizaling the program as a function.
def init():

    global root
    #root = tk which is tkinter this will allow me to use root.geometry 
    #to chosse the screen size and root.config to pick a background colour aswell as title.
    
    root = tk.Tk() 
   

    root.title('Mū Tōrere')
    root.geometry('1366x768')
    root.config(bg='OliveDrab2')
        
    boardimg = PhotoImage(file='Mū tōrere.png') #This is importing the image
    Label(root,image=boardimg).pack() #creating the image as a label

    checkers() #Will need to call functions here because of the mainloop
    root.mainloop() 


def checkers():
    global root
    blue = 0
    blueimg = []
    bluepeice = []
    canvas = tk.Canvas(root, bg='OliveDrab2', relief="flat", borderwidth=0, highlightthickness=0, width=0)
    frame = tk.Frame(canvas, bg='OliveDrab2', relief="flat", borderwidth=0, highlightthickness=0, width=0)
    while blue < 4:
        bluecheck= Image.open("bluecircle50.png")
        bluecheck = ImageTk.PhotoImage(bluecheck)
        bluechecker_button = tk.Button(frame, image=bluecheck, compound="center", borderwidth=0,  bg='OliveDrab2', command=click)
        bluechecker_button.pack()
        blue += 1
        bluepeice.append(blueimg)
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.pack(fill='both', expand=True, side='bottom')
    root.mainloop()

def click():
    print("clicked")

#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    init()
    
