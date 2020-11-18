from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.insert(0,os.getcwd())
from Gui.errorMessage import errorWindow

class usePTOWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Use PTO")

        #Create frame
        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Create labels/text areas and buttons and put on screen
        self.titleLabel = Label(self.frame1, text="Use PTO")
        self.hoursLabel = Label(self.frame1, text="Hours:")
        self.inputTextBox = Entry(self.frame1)
        self.saveButton = Button(self.frame1, text="Save", command=self.saveButtonPressed)
        self.cancelButton = Button(self.frame1, text="Cancel", command=self.cancelButtonPressed)

        self.titleLabel.grid(row=0, column=1)
        self.hoursLabel.grid(row=1, column=0)
        self.inputTextBox.grid(row=1, column=1)
        self.saveButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)

    def saveButtonPressed(self):
        """Saves info to database"""
        ptoUsed = self.inputTextBox.get()
        if ptoUsed.isdigit():
            if (self.user.PTO.Used_PTO + int(ptoUsed)) > self.user.PTO.PTO_Limit:
                errorWindow(f"Can't use that much PTO, only {self.user.PTO.PTO_Limit - self.user.PTO.Current_PTO} hours left")
            else:
                self.user.PTO.Current_PTO -= int(ptoUsed)
                self.user.PTO.Used_PTO += int(ptoUsed)
                self.user.save()
                self.window.destroy()
                errorWindow("PTO Used!")
        else:
            errorWindow("Only whole numbers allowed")

    def cancelButtonPressed(self):
        """Cancels process"""
        self.window.destroy()
   