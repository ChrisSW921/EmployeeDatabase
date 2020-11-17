from tkinter import *
from tkinter import ttk
from errorMessage import errorWindow
from Backend.employee_timecard import EmployeeTimecard
import sys
import os
sys.path.insert(0,os.getcwd())

class addTimeCardWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add Time Card")

        #Create frame
        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Create labels/text areas and buttons and put on screen
        self.titleLabel = Label(self.frame1, text="Add Time Card")
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
        card = self.inputTextBox.get()
        try:
             card = float(card)
             cardToAdd = EmployeeTimecard(card)
             self.user.add_timecard(cardToAdd)
             self.window.destroy()
             errorWindow("Time Card Added! Select record again to refresh")
        except:
            errorWindow("Only numbers or decimals allowed")
        

    def cancelButtonPressed(self):
        """Cancels process"""
        self.window.destroy()