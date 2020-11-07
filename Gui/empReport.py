from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.insert(0,os.getcwd())

from Database import database
from Gui.errorMessage import errorWindow


class empReporting:

    def __init__(self, user, reportType):
        self.user = user
        self.window = Tk()
        self.window.title("Report")
        self.includeArchived = False
        self.report = reportType

        #Create frame
        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Create labels/text areas and buttons and put on screen
        self.titleLabel = Label(self.frame1, text="")
        self.hoursLabel = Label(self.frame1, text="Include Archived Emps ->", padx=20, pady=20)

        self.archived = IntVar()

        self.archivedBox = Checkbutton(self.frame1, text="", variable=self.archived, state='normal', padx=20, pady=20) 
        self.generateButton = Button(self.frame1, text="Generate", command=self.generateButtonPressed)
        self.cancelButton = Button(self.frame1, text="Cancel", command=self.cancelButtonPressed)

        self.titleLabel.grid(row=0, column=1)
        self.hoursLabel.grid(row=1, column=0)
        self.archivedBox.grid(row=1, column=1)
        self.generateButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)

    def generateButtonPressed(self):
        """Processes the employee report/payment report"""
        if self.archived == 1:
            if self.report == 'employee':
                database.generate_employee_report(True)
                errorWindow("Successfully generated employee report")

            elif self.report == 'payment':
                database.generate_payment_report()
                errorWindow("Successfully generated employee report")

        else:
            if self.report == 'employee':
                database.generate_employee_report(False)
                errorWindow("Successfully generated employee report")


            elif self.report == 'payment':
                database.generate_payment_report()
                errorWindow("Successfully generated employee report")

    def cancelButtonPressed(self):
        """Cancels current process"""
        self.window.destroy()
        