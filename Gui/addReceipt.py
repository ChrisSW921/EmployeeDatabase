from tkinter import *
from tkinter import ttk
from errorMessage import errorWindow
from Backend.employee_receipt import EmployeeReceipt
import sys
import os
sys.path.insert(0,os.getcwd())

class addReceiptWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add Receipt")

        #Create frame
        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Create labels/text areas and buttons and put on screen
        self.titleLabel = Label(self.frame1, text="Add Receipt")
        self.hoursLabel = Label(self.frame1, text="Amount:")
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
        receipt = self.inputTextBox.get()
        try:
             receipt = float(receipt)
             receiptToAdd = EmployeeReceipt(receipt)
             self.user.add_receipt(receiptToAdd)
             self.window.destroy()
             errorWindow("Receipt Added! Select record again to refresh")
        except:
            errorWindow("Only numbers or decimals allowed")


        

    def cancelButtonPressed(self):
        """Cancels process"""
        self.window.destroy()