from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.insert(0,os.getcwd())

class changePasswordWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Change Password")

        #Create frame
        frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        frame1.pack()

        #Create labels/text areas and buttons and put on screen
        userIdLabel = Label(frame1, text="Employee Id")
        oldPasswordLabel = Label(frame1, text="New Password")
        newPasswordLabel = Label(frame1, text="Confirm Password")
        userIdTextBox = Entry(frame1)
        oldPasswordTextBox = Entry(frame1)
        newPasswordTextBox = Entry(frame1)
        saveButton = Button(frame1, text="Save")
        cancelButton = Button(frame1, text="Cancel", command=self.cancelButtonPressed)

        userIdLabel.grid(row=0, column=0)
        userIdTextBox.grid(row=0, column=1)
        oldPasswordLabel.grid(row=1, column=0)
        newPasswordLabel.grid(row=2, column=0)
        oldPasswordTextBox.grid(row=1, column=1)
        newPasswordTextBox.grid(row=2, column=1)
        saveButton.grid(row=3, column=0)
        cancelButton.grid(row=3, column=1)

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        print("canceled")