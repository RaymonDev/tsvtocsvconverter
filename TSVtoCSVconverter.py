#program that converts TSV to CSV
#https://github.com/RaymonDev

#importing the libraries
import tkinter as tk
import pandas as pnd
from tkinter import filedialog
import os
from pynotifier import Notification

#variables for the defs:

pathtotsv = ""
nameofile = ""

#creates tkinter functions to select and open the file

def tsvpath():

    global pathtotsv
    global nameofile

    pathtotsv =  filedialog.askopenfilename(initialdir ="/", title ="Select file", filetypes = (("TSV Files", "*.tsv"), ("CSV Files", "*.csv"), ("All files", "*.*")))
    prev= os.path.basename(pathtotsv) # filters the name of the file
    nameofile = os.path.splitext(prev)[0] #splits the name into the name and the extension and grabs the name only

    annotation = tk.Label(window, text="Please have pacience while the Convert button is different. That means your file is being converted").pack()

def conversion():

    convertbutton['state'] = tk.DISABLED #disables the button

    #detects if there's an error in the path
    if pathtotsv == "":
        Notification(
            title='Error',
            description="Path not defined",
            icon_path='',  # On Windows .ico is required, on Linux - .png
            duration=5,  # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
        ).send()

        convertbutton['state'] = tk.NORMAL #enables the button

    tsvfile = pathtotsv #gets the path of the file
    csvfile = pnd.read_table(tsvfile, sep='\t')
    csvfile.to_csv(nameofile + ".csv", index=False)#converts the file into a csv

    convertbutton['state'] = tk.NORMAL #enables the button


#creating the simple GUI

window = tk.Tk(className=" TSV to CSV converter")
window.resizable(0,0)
window.geometry("600x400")

#creating and configuring the buttons and textbox

tsvbutton = tk.Button(window, text="Select", command = tsvpath)
tsvbutton.place(relx = "0.43", rely = "0.05")

convertbutton = tk.Button(window, text="Convert", command = conversion)
convertbutton.place(relx = "0.42", rely = "0.2")

note = tk.Label(text="Note: The new CSV file will apear in the same path as this python file")
note.place(relx = "0.2", rely = "0.35")

#pack and show the window
window.mainloop()
