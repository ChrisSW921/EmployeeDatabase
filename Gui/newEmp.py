from tkinter import *
from tkinter import ttk

class addEmpWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add New Employee")
        
        #Add employee information area
        frame3 = LabelFrame(self.window, text="")
        frame3.pack()

        #Add employee information labels and put on grid
        IDLabel = Label(frame3, text="NEW EMPLOYEE")
        firstNameLabel = Label(frame3, text="First Name")
        lastNameLabel = Label(frame3, text="Last Name")
        addressLabel = Label(frame3, text="Adress")
        cityLabel = Label(frame3, text="City")
        stateLabel = Label(frame3, text="State")
        zipLabel = Label(frame3, text="Zip")
        phoneLabel = Label(frame3, text="Phone Number")
        payTypeLabel = Label(frame3, text="Pay Type")
        payMethodLabel = Label(frame3, text="Pay Method")
        salaryLabel = Label(frame3, text="Salary")
        hourlyLabel = Label(frame3, text="Hourly")
        commissionLabel = Label(frame3, text="Commission") 
        currentPTOLabel = Label(frame3, text="Current PTO")
        usedPTOLabel = Label(frame3, text="PTO Used")
        limitPTOLabel = Label(frame3, text="PTO Limit")
        ssnLabel = Label(frame3, text="SSN")
        editorLabel = Label(frame3, text="Editing Permission")
        reportLabel = Label(frame3, text="Reporting Permission")
        accountingLabel = Label(frame3, text="Accounting Permission")
        managerLabel = Label(frame3, text="Manager Permission")

        IDLabel.grid(row=0, column=0, rowspan=2) 
        firstNameLabel.grid(row=0, column=1)
        lastNameLabel.grid(row=0, column=2)
        addressLabel.grid(row=0, column=3) 
        cityLabel.grid(row=0, column=4)
        stateLabel.grid(row=2, column=0)
        zipLabel.grid(row=2, column=1) 
        phoneLabel.grid(row=2, column=2)
        payTypeLabel.grid(row=2, column=3)
        payMethodLabel.grid(row=2, column=4)
        salaryLabel.grid(row=4, column=0)
        hourlyLabel.grid(row=4, column=1)
        commissionLabel.grid(row=4, column=2)
        currentPTOLabel.grid(row=4, column=3)
        usedPTOLabel.grid(row=4, column=4)
        limitPTOLabel.grid(row=6, column=0)
        ssnLabel.grid(row=6, column=1)
        editorLabel.grid(row=6, column=2)
        reportLabel.grid(row=6, column=3)
        accountingLabel.grid(row=6, column=4)
        managerLabel.grid(row=8, column=0)

        #Add employee text boxes/checkmarks/dropdownmenus and put into frame
        #IDLabelText = Entry(frame3).grid(row=1, column=0)
        firstNameLabelText = Entry(frame3)
        lastNameLabelText = Entry(frame3)
        addressLabelText = Entry(frame3)
        cityLabelText = Entry(frame3)
        stateLabelText = Entry(frame3)
        zipLabelText = Entry(frame3)
        phoneLabelText = Entry(frame3)

        firstNameLabelText.grid(row=1, column=1)
        lastNameLabelText.grid(row=1, column=2)
        addressLabelText.grid(row=1, column=3)
        cityLabelText.grid(row=1, column=4) 
        stateLabelText.grid(row=3, column=0)
        zipLabelText.grid(row=3, column=1)
        phoneLabelText.grid(row=3, column=2) 

        #dropdown part for payment option
        paymentOptions = ["Salaried", "Commissioned", "Hourly"]

        paymentOption = StringVar(frame3)
        paymentOption.set(paymentOptions[1])

        paymentOptionMenu = OptionMenu(frame3, paymentOption, *paymentOptions)
        paymentOptionMenu.grid(row=3, column=3)


        paymentTypes = ["Direct Deposit", "Mailed"]

        paymentType = StringVar(frame3)
        paymentType.set(paymentTypes[1])

        #Rest of text boxes/checkmarks
        payMethodLabelText = OptionMenu(frame3, paymentType, *paymentTypes)
        salaryLabelText = Entry(frame3) 
        hourlyLabelText = Entry(frame3) 
        commissionLabelText = Entry(frame3)
        currentPTOLabelText = Entry(frame3)
        usedPTOLabelText = Entry(frame3)
        limitPTOLabelText = Entry(frame3)
        ssnLabelText= Entry(frame3)

        payMethodLabelText.grid(row=3, column=4)
        salaryLabelText.grid(row=5, column=0)
        hourlyLabelText.grid(row=5, column=1)
        commissionLabelText.grid(row=5, column=2)
        currentPTOLabelText.grid(row=5, column=3)
        usedPTOLabelText.grid(row=5, column=4)
        limitPTOLabelText.grid(row=7, column=0)
        ssnLabelText.grid(row=7, column=1)

        editor = IntVar()
        reporter = IntVar()
        accounting = IntVar()
        manager = IntVar()

        editorCheck = Checkbutton(frame3, text="", variable=editor)
        reporterCheck = Checkbutton(frame3, text="", variable=reporter)
        accountingCheck = Checkbutton(frame3, text="", variable=accounting)
        managerCheck = Checkbutton(frame3, text="", variable=manager)

        editorCheck.grid(row=7, column=2)
        reporterCheck.grid(row=7, column=3)
        accountingCheck.grid(row=7, column=4)
        managerCheck.grid(row=9, column=0)

        #Add save and cancel buttons
        saveButton = Button(frame3, text='Save')
        cancelButton = Button(frame3, text='Cancel', command=self.cancelButtonPressed)

        saveButton.grid(row=10,column=1, padx=15)
        cancelButton.grid(row=10,column=3, padx=15)

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        print("canceled")