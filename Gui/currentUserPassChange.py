import sys
import os
sys.path.insert(0,os.getcwd())

from tkinter import *
from tkinter import ttk

from Gui.errorMessage import errorWindow
from Database import database
from Backend.employee import Employee

class changeUserPassword:
    def __init__(self, user : Employee):
        self.window = Tk()
        self.window.title("Change Your Password")
        self.currentUser = user

        #Create frame
        frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        frame1.pack()

        #Create labels/text areas and buttons and put on screen
        oldPasswordLabel = Label(frame1, text="New Password")
        newPasswordLabel = Label(frame1, text="Confirm Password")
        self.newPassTextBox = Entry(frame1, show="*")
        self.confPassTextBox = Entry(frame1, show="*")
        saveButton = Button(frame1, text="Save", command=self.saveButtonPressed)
        cancelButton = Button(frame1, text="Cancel", command=self.cancelButtonPressed)

        oldPasswordLabel.grid(row=0, column=0)
        newPasswordLabel.grid(row=1, column=0)
        self.newPassTextBox.grid(row=0, column=1)
        self.confPassTextBox.grid(row=1, column=1)
        saveButton.grid(row=2, column=0)
        cancelButton.grid(row=2, column=1)

    def saveButtonPressed(self):
        """Saves info to database"""
        try:
            newPass = self.newPassTextBox.get()
            confPass = self.confPassTextBox.get()

            if (newPass != confPass):
                errorWindow("Passwords do not match")
            else:  
                self.currentUser.set_password(newPass)
                errorWindow("Password saved!")
                # Maybe have a success window appear??
                self.window.destroy()
                print("saved")

        except ValueError:
            errorWindow("Please enter an integer in the id field")

    def cancelButtonPressed(self):
        """Cancels process"""
        self.window.destroy()
        print("canceled")