import sys
import os
sys.path.insert(0,os.getcwd())

from tkinter import *
from tkinter import ttk

from Gui.errorMessage import errorWindow
from Database import database

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
        self.empIdTextBox = Entry(frame1)
        self.newPassTextBox = Entry(frame1, show="*")
        self.confPassTextBox = Entry(frame1, show="*")
        saveButton = Button(frame1, text="Save", command=self.saveButtonPressed)
        cancelButton = Button(frame1, text="Cancel", command=self.cancelButtonPressed)

        userIdLabel.grid(row=0, column=0)
        oldPasswordLabel.grid(row=1, column=0)
        newPasswordLabel.grid(row=2, column=0)
        self.empIdTextBox.grid(row=0, column=1)
        self.newPassTextBox.grid(row=1, column=1)
        self.confPassTextBox.grid(row=2, column=1)
        saveButton.grid(row=3, column=0)
        cancelButton.grid(row=3, column=1)

    def saveButtonPressed(self):
        """Saves info to database"""
        try:
            empId = int(self.empIdTextBox.get())
            newPass = self.newPassTextBox.get()
            confPass = self.confPassTextBox.get()

            if (newPass != confPass):
                errorWindow("Passwords do not match")
            else:
                selectedEmployee = database.get_employee(empId)

                if (selectedEmployee == None):
                    errorWindow("Could not find employee with id" + str(empId))
                else:
                    selectedEmployee.set_password(newPass)
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