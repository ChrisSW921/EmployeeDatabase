from tkinter import *
from tkinter import ttk
from erroMessage import errorWindow
import sys
import os
sys.path.insert(0,os.getcwd())

class addPTOWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add PTO")

        #Create frame
        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Create labels/text areas and buttons and put on screen
        self.titleLabel = Label(self.frame1, text="Add PTO")
        self.hoursLabel = Label(self.frame1, text="Hours:")
        self.inputTextBox = Entry(self.frame1)
        self.saveButton = Button(self.frame1, text="Save")
        self.cancelButton = Button(self.frame1, text="Cancel", command=self.cancelButtonPressed)

        self.titleLabel.grid(row=0, column=1)
        self.hoursLabel.grid(row=1, column=0)
        self.inputTextBox.grid(row=1, column=1)
        self.saveButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)

    def saveButtonPressed(self):
        pto = self.inputTextBox.get()
        if pto.isdigit():
            #update the emp
            print("update")
        else:
            errorWindow("Only whole numbers allowed")
        

    def cancelButtonPressed(self):
        self.window.destroy()
        