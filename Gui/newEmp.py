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
        IDLabel = Label(frame3, text="NEW EMPLOYEE").grid(row=0, column=0, rowspan=2) 
        firstNameLabel = Label(frame3, text="First Name").grid(row=0, column=1)
        lastNameLabel = Label(frame3, text="Last Name").grid(row=0, column=2)
        addressLabel = Label(frame3, text="Adress").grid(row=0, column=3) 
        cityLabel = Label(frame3, text="City").grid(row=0, column=4)
        stateLabel = Label(frame3, text="State").grid(row=2, column=0)
        zipLabel = Label(frame3, text="Zip").grid(row=2, column=1) 
        phoneLabel = Label(frame3, text="Phone Number").grid(row=2, column=2)
        payTypeLabel = Label(frame3, text="Pay Type").grid(row=2, column=3)
        payMethodLabel = Label(frame3, text="Pay Method").grid(row=2, column=4)
        salaryLabel = Label(frame3, text="Salary").grid(row=4, column=0)
        hourlyLabel = Label(frame3, text="Hourly").grid(row=4, column=1)
        commissionLabel = Label(frame3, text="Commission").grid(row=4, column=2) 
        currentPTOLabel = Label(frame3, text="Current PTO").grid(row=4, column=3)
        usedPTOLabel = Label(frame3, text="PTO Used").grid(row=4, column=4)
        limitPTOLabel = Label(frame3, text="PTO Limit").grid(row=6, column=0)
        ssnLabel = Label(frame3, text="SSN").grid(row=6, column=1)
        editorLabel = Label(frame3, text="Editing Permission").grid(row=6, column=2)
        reportLabel = Label(frame3, text="Reporting Permission").grid(row=6, column=3)
        accountingLabel = Label(frame3, text="Accounting Permission").grid(row=6, column=4)
        managerLabel = Label(frame3, text="Manager Permission").grid(row=8, column=0)

        #Add employee text boxes/checkmarks/dropdownmenus and put into frame
        #IDLabelText = Entry(frame3).grid(row=1, column=0)
        firstNameLabelText = Entry(frame3).grid(row=1, column=1)
        lastNameLabelText = Entry(frame3).grid(row=1, column=2)
        addressLabelText = Entry(frame3).grid(row=1, column=3)
        cityLabelText = Entry(frame3).grid(row=1, column=4) 
        stateLabelText = Entry(frame3).grid(row=3, column=0)
        zipLabelText = Entry(frame3).grid(row=3, column=1)
        phoneLabelText = Entry(frame3).grid(row=3, column=2) 

        #dropdown part for payment option
        paymentOptions = ["Salaried", "Commissioned", "Hourly"]

        paymentOption = StringVar(frame3)
        paymentOption.set(paymentOptions[1])

        paymentOptionMenu = OptionMenu(frame3, paymentOption, *paymentOptions).grid(row=3, column=3)

        #Rest of text boxes/checkmarks
        payMethodLabelText = Entry(frame3).grid(row=3, column=4)
        salaryLabelText = Entry(frame3).grid(row=5, column=0) 
        hourlyLabelText = Entry(frame3).grid(row=5, column=1) 
        commissionLabelText = Entry(frame3).grid(row=5, column=2)
        currentPTOLabelText = Entry(frame3).grid(row=5, column=3)
        usedPTOLabelText = Entry(frame3).grid(row=5, column=4)
        limitPTOLabelText = Entry(frame3).grid(row=7, column=0)
        ssnLabelText= Entry(frame3).grid(row=7, column=1)

        editor = IntVar()
        reporter = IntVar()
        accounting = IntVar()
        manager = IntVar()

        editorCheck = Checkbutton(frame3, text="", variable=editor).grid(row=7, column=2)
        reporterCheck = Checkbutton(frame3, text="", variable=reporter).grid(row=7, column=3)
        accountingCheck = Checkbutton(frame3, text="", variable=accounting).grid(row=7, column=4)
        managerCheck = Checkbutton(frame3, text="", variable=manager).grid(row=9, column=0)

        #Add save and cancel buttons
        saveButton = Button(frame3, text='Save').grid(row=10,column=1, padx=15)
        cancelButton = Button(frame3, text='Cancel').grid(row=10,column=3, padx=15)