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

    #root = tk which is tkinter this will allow me to use root.geometry 
    #to chosse the screen size and root.config to pick a background colour
    
    root = tk.Tk()  

    root.geometry('1366x768')
    root.config(bg='OliveDrab2')
                  
    boardimg = PhotoImage(file='Mū tōrere.png')
    Label(root,image=boardimg).pack()

    root.mainloop() 


#If the name of the program is called main it will run everything below.
if __name__ == '__main__':
    init()
