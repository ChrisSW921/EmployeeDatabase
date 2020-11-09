from tkinter import *
from tkinter import ttk
from errorMessage import errorWindow
import sys
import os
sys.path.insert(0,os.getcwd())

class paymentWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Payment Method")

        self.chosen = ''

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
        self.saveButton = Button(self.frame1, text='Save', command=self.saveButtonPressed)
        self.cancelButton = Button(self.frame1, text='Cancel', command=self.cancelButtonPressed)

        self.saveButton.grid(row=3,column=0, padx=15, pady=40)
        self.cancelButton.grid(row=3,column=2, padx=15, pady=40)

    def makeSalariedButtonPressed(self):
        """Changes the employees paytype to Salaried/disables other boxes"""
        self.salaryLabelText['state'] = 'normal'
        self.hourlyLabelText['state'] = 'disabled'
        self.commissionLabelText['state'] = 'disabled'
        self.chosen = 'Salaried'
    

    def makeCommissionedButtonPressed(self):
        """Changes the employees paytype to Commissioned/disables other boxes"""
        self.salaryLabelText['state'] = 'normal'
        self.hourlyLabelText['state'] = 'disabled'
        self.commissionLabelText['state'] = 'normal'
        self.chosen = 'Commissioned'
        
    
    def makeHourlyButtonPressed(self):
        """Changes the employees paytype to Hourly/disables other boxes"""
        self.hourlyLabelText['state'] = 'normal'
        self.commissionLabelText['state'] = 'disabled'
        self.salaryLabelText['state'] = 'disabled'
        self.chosen = 'Hourly'
        

    def saveButtonPressed(self):
        """This function saves the information to the database"""
        if self.chosen == 'Salaried':
            try:
                self.user.Salary = float(self.salaryLabelText.get())
                self.user.Pay_Type = 1
                self.user.save()
                self.window.destroy()
                errorWindow('Employee Salary Updated! Select employee again to see changes')
            except:
                errorWindow('Only enter numbers, no special characters or spaces for salary')
        elif self.chosen == 'Commissioned':
            try:
                self.user.Salary = float(self.salaryLabelText.get())
                self.user.Commission = float(self.commissionLabelText.get())
                self.user.Pay_Type = 2
                self.user.save()
                self.window.destroy()
                errorWindow('Employee Salary and Commission Updated! Select employee again to see changes')
            except:
                errorWindow('Only enter numbers, no special characters or spaces for salary or commission')    
        elif self.chosen == 'Hourly':
            try:
                self.user.Hourly = float(self.hourlyLabelText.get())
                self.user.Pay_Type = 3
                self.user.save()
                self.window.destroy()
                errorWindow('Employee Hourly Updated! Select employee again to see changes')
            except:
                errorWindow('Only enter numbers, no special characters or spaces for Hourly')
        else:
            errorWindow('Please choose which pay type and input values before saving.')

    def cancelButtonPressed(self):
        """Cancels this process"""
        self.window.destroy()
        
            