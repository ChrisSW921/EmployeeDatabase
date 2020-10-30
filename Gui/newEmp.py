from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.insert(0,os.getcwd())

class addEmpWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add New Employee")
        
        #Add employee information area
        self.frame3 = LabelFrame(self.window, text="")
        self.frame3.pack()

        #Add employee information labels and put on grid
        self.IDLabel = Label(self.frame3, text="NEW EMPLOYEE")
        self.firstNameLabel = Label(self.frame3, text="First Name")
        self.lastNameLabel = Label(self.frame3, text="Last Name")
        self.addressLabel = Label(self.frame3, text="Adress")
        self.cityLabel = Label(self.frame3, text="City")
        self.stateLabel = Label(self.frame3, text="State")
        self.zipLabel = Label(self.frame3, text="Zip")
        self.phoneLabel = Label(self.frame3, text="Phone Number")
        self.payTypeLabel = Label(self.frame3, text="Pay Type")
        self.payMethodLabel = Label(self.frame3, text="Pay Method")
        self.salaryLabel = Label(self.frame3, text="Salary")
        self.hourlyLabel = Label(self.frame3, text="Hourly")
        self.commissionLabel = Label(self.frame3, text="Commission") 
        self.currentPTOLabel = Label(self.frame3, text="Current PTO")
        self.usedPTOLabel = Label(self.frame3, text="PTO Used")
        self.limitPTOLabel = Label(self.frame3, text="PTO Limit")
        self.ssnLabel = Label(self.frame3, text="SSN")
        self.editorLabel = Label(self.frame3, text="Editing Permission")
        self.reportLabel = Label(self.frame3, text="Reporting Permission")
        self.accountingLabel = Label(self.frame3, text="Accounting Permission")
        self.managerLabel = Label(self.frame3, text="Manager Permission")

        self.IDLabel.grid(row=0, column=0, rowspan=2) 
        self.firstNameLabel.grid(row=0, column=1)
        self.lastNameLabel.grid(row=0, column=2)
        self.addressLabel.grid(row=0, column=3) 
        self.cityLabel.grid(row=0, column=4)
        self.stateLabel.grid(row=2, column=0)
        self.zipLabel.grid(row=2, column=1) 
        self.phoneLabel.grid(row=2, column=2)
        self.payTypeLabel.grid(row=2, column=3)
        self.payMethodLabel.grid(row=2, column=4)
        self.salaryLabel.grid(row=4, column=0)
        self.hourlyLabel.grid(row=4, column=1)
        self.commissionLabel.grid(row=4, column=2)
        self.currentPTOLabel.grid(row=4, column=3)
        self.usedPTOLabel.grid(row=4, column=4)
        self.limitPTOLabel.grid(row=6, column=0)
        self.ssnLabel.grid(row=6, column=1)
        self.editorLabel.grid(row=6, column=2)
        self.reportLabel.grid(row=6, column=3)
        self.accountingLabel.grid(row=6, column=4)
        self.managerLabel.grid(row=8, column=0)

        #Add employee text boxes/checkmarks/dropdownmenus and put into frame
        #IDLabelText = Entry(frame3).grid(row=1, column=0)
        self.firstNameLabelText = Entry(self.frame3)
        self.lastNameLabelText = Entry(self.frame3)
        self.addressLabelText = Entry(self.frame3)
        self.cityLabelText = Entry(self.frame3)
        self.stateLabelText = Entry(self.frame3)
        self.zipLabelText = Entry(self.frame3)
        self.phoneLabelText = Entry(self.frame3)

        self.firstNameLabelText.grid(row=1, column=1)
        self.lastNameLabelText.grid(row=1, column=2)
        self.addressLabelText.grid(row=1, column=3)
        self.cityLabelText.grid(row=1, column=4) 
        self.stateLabelText.grid(row=3, column=0)
        self.zipLabelText.grid(row=3, column=1)
        self.phoneLabelText.grid(row=3, column=2) 

        #dropdown part for payment option
        self.paymentOptions = ["Salaried", "Commissioned", "Hourly"]

        self.paymentOption = StringVar(self.frame3)
        self.paymentOption.set(self.paymentOptions[1])

        self.paymentOptionMenu = OptionMenu(self.frame3, self.paymentOption, *self.paymentOptions)
        self.paymentOptionMenu.grid(row=3, column=3)


        self.paymentTypes = ["Direct Deposit", "Mailed"]

        self.paymentType = StringVar(self.frame3)
        self.paymentType.set(self.paymentTypes[1])

        #Rest of text boxes/checkmarks
        self.payMethodLabelText = OptionMenu(self.frame3, self.paymentType, *self.paymentTypes)
        self.salaryLabelText = Entry(self.frame3) 
        self.hourlyLabelText = Entry(self.frame3) 
        self.commissionLabelText = Entry(self.frame3)
        self.currentPTOLabelText = Entry(self.frame3)
        self.usedPTOLabelText = Entry(self.frame3)
        self.limitPTOLabelText = Entry(self.frame3)
        self.ssnLabelText= Entry(self.frame3)

        self.payMethodLabelText.grid(row=3, column=4)
        self.salaryLabelText.grid(row=5, column=0)
        self.hourlyLabelText.grid(row=5, column=1)
        self.commissionLabelText.grid(row=5, column=2)
        self.currentPTOLabelText.grid(row=5, column=3)
        self.usedPTOLabelText.grid(row=5, column=4)
        self.limitPTOLabelText.grid(row=7, column=0)
        self.ssnLabelText.grid(row=7, column=1)

        self.editor = IntVar()
        self.reporter = IntVar()
        self.accounting = IntVar()
        self.manager = IntVar()

        self.editorCheck = Checkbutton(self.frame3, text="", variable=self.editor)
        self.reporterCheck = Checkbutton(self.frame3, text="", variable=self.reporter)
        self.accountingCheck = Checkbutton(self.frame3, text="", variable=self.accounting)
        self.managerCheck = Checkbutton(self.frame3, text="", variable=self.manager)

        self.editorCheck.grid(row=7, column=2)
        self.reporterCheck.grid(row=7, column=3)
        self.accountingCheck.grid(row=7, column=4)
        self.managerCheck.grid(row=9, column=0)

        #Add save and cancel buttons
        self.saveButton = Button(self.frame3, text='Save')
        self.cancelButton = Button(self.frame3, text='Cancel', command=self.cancelButtonPressed)

        self.saveButton.grid(row=10,column=1, padx=15)
        self.cancelButton.grid(row=10,column=3, padx=15)

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        print("canceled")