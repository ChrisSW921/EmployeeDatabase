from tkinter import *
from tkinter import ttk

class paymentWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Payment Method")


        #Make and place main buttons
        makeSalariedButton = Button(text='Make Salaried').grid(row=0,column=0, padx=15, pady=40)
        makeHourlyButton = Button(text='Make Hourly').grid(row=0,column=1, padx=15, pady=40)
        makeCommissionedButton = Button(text='Make Commissioned').grid(row=0,column=2, padx=15, pady=40)

        #make and place labels
        salaryLabel = Label(text="Salary").grid(row=1, column=0)
        hourlyLabel = Label(text="Hourly pay").grid(row=1, column=1)
        commissionLabel = Label(text="Commission rate").grid(row=1, column=2) 

        #Make and place text areas
        salaryLabelText = Entry().grid(row=2, column=0) 
        hourlyLabelText = Entry().grid(row=2, column=1) 
        commissionLabelText = Entry().grid(row=2, column=2)

        #Make and place save and cancel buttons
        saveButton = Button(text='Save').grid(row=3,column=0, padx=15, pady=40)
        cancelButton = Button(text='Cancel').grid(row=3,column=2, padx=15, pady=40)

        