from tkinter import *
from tkinter import ttk

class paymentWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Payment Method")

        frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        frame1.pack()

        #Make and place main buttons
        makeSalariedButton = Button(frame1, text='Make Salaried')
        makeHourlyButton = Button(frame1, text='Make Hourly')
        makeCommissionedButton = Button(frame1, text='Make Commissioned')

        makeSalariedButton.grid(row=0,column=0, padx=15, pady=40)
        makeHourlyButton.grid(row=0,column=1, padx=15, pady=40)
        makeCommissionedButton.grid(row=0,column=2, padx=15, pady=40)

        #make and place labels
        salaryLabel = Label(frame1, text="Salary")
        hourlyLabel = Label(frame1, text="Hourly pay")
        commissionLabel = Label(frame1, text="Commission rate") 

        salaryLabel.grid(row=1, column=0)
        hourlyLabel.grid(row=1, column=1)
        commissionLabel.grid(row=1, column=2)

        #Make and place text areas
        salaryLabelText = Entry(frame1) 
        hourlyLabelText = Entry(frame1) 
        commissionLabelText = Entry(frame1)

        salaryLabelText.grid(row=2, column=0)
        hourlyLabelText.grid(row=2, column=1)
        commissionLabelText.grid(row=2, column=2)

        #Make and place save and cancel buttons
        saveButton = Button(frame1, text='Save')
        cancelButton = Button(frame1, text='Cancel', command=self.cancelButtonPressed)

        saveButton.grid(row=3,column=0, padx=15, pady=40)
        cancelButton.grid(row=3,column=2, padx=15, pady=40)

    def makeSalariedButtonPressed(self):
        print("Made salaried")

    def makeCommissionedButtonPressed(self):
        print("Made commissioned")
    
    def makeHourlyButtonPressed(self):
        print("Made Hourly")

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        print("canceled")
            