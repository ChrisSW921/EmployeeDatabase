from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.insert(0,os.getcwd())

class paymentWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Payment Method")

        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Make and place main buttons
        self.makeSalariedButton = Button(self.frame1, text='Make Salaried', command=self.makeSalariedButtonPressed)
        self.makeHourlyButton = Button(self.frame1, text='Make Hourly', command=self.makeHourlyButtonPressed)
        self.makeCommissionedButton = Button(self.frame1, text='Make Commissioned', command=self.makeCommissionedButtonPressed)

        self.makeSalariedButton.grid(row=0,column=0, padx=15, pady=40)
        self.makeHourlyButton.grid(row=0,column=1, padx=15, pady=40)
        self.makeCommissionedButton.grid(row=0,column=2, padx=15, pady=40)

        #make and place labels
        self.salaryLabel = Label(self.frame1, text="Salary")
        self.hourlyLabel = Label(self.frame1, text="Hourly pay")
        self.commissionLabel = Label(self.frame1, text="Commission rate") 

        self.salaryLabel.grid(row=1, column=0)
        self.hourlyLabel.grid(row=1, column=1)
        self.commissionLabel.grid(row=1, column=2)

        #Make and place text areas
        self.salaryLabelText = Entry(self.frame1) 
        self.hourlyLabelText = Entry(self.frame1) 
        self.commissionLabelText = Entry(self.frame1)

        self.salaryLabelText.grid(row=2, column=0)
        self.hourlyLabelText.grid(row=2, column=1)
        self.commissionLabelText.grid(row=2, column=2)

        #Make and place save and cancel buttons
        self.saveButton = Button(self.frame1, text='Save')
        self.cancelButton = Button(self.frame1, text='Cancel', command=self.cancelButtonPressed)

        self.saveButton.grid(row=3,column=0, padx=15, pady=40)
        self.cancelButton.grid(row=3,column=2, padx=15, pady=40)

    def makeSalariedButtonPressed(self):
        self.salaryLabelText['state'] = 'normal'
        self.hourlyLabelText['state'] = 'disabled'
        self.commissionLabelText['state'] = 'disabled'
    

    def makeCommissionedButtonPressed(self):
        self.salaryLabelText['state'] = 'disabled'
        self.hourlyLabelText['state'] = 'normal'
        self.commissionLabelText['state'] = 'normal'
        
    
    def makeHourlyButtonPressed(self):
        self.hourlyLabelText['state'] = 'normal'
        self.commissionLabelText['state'] = 'disabled'
        self.salaryLabelText['state'] = 'disabled'
        

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        print("canceled")
            