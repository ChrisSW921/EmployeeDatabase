#Set up home page, showing certain buttons to create user to only select access levels. Home page
#will include access to all major and minor features of software. . 

from tkinter import *
from tkinter import ttk
from changePayment import paymentWindow
from lessPTO import usePTOWindow
from morePTO import addPTOWindow
from newEmp import addEmpWindow
from newPassword import changePasswordWindow
from scrollable import ScrollableFrame


class MainMenu:

    def __init__(self, user):
        """Main menu screen. Instantiates with a user from login"""
        self.loggedInUser = user
        self.selectedUser = "Generic user we will create"
        self.window = Tk()
        self.window.title("Main Menu")
        self.window.config(bg="sky blue")

        self.frame0 = ScrollableFrame(self.window)
        

        #Create tree view frame
        self.frame1 = LabelFrame(self.frame0.scrollable_frame, text="")
        self.frame1.pack()

        #Create tree view
        self.searchResults = ttk.Treeview(self.frame1)
        self.searchResults['columns'] = ("First Name", "Last Name", "ID", "Phone Number")

        # Format tree view
        self.searchResults.column("#0", width=0, minwidth=0)
        self.searchResults.column("First Name", anchor=CENTER)
        self.searchResults.column("Last Name", anchor=CENTER)    
        self.searchResults.column("ID", anchor=CENTER)
        self.searchResults.column("Phone Number", anchor=CENTER)

        #Create Tree View Headings
        self.searchResults.heading("#0", text="", anchor=W)
        self.searchResults.heading("First Name", text="First Name", anchor=W)
        self.searchResults.heading("Last Name", text="Last Name", anchor=W)
        self.searchResults.heading("ID", text="ID", anchor=W)
        self.searchResults.heading("Phone Number", text="Phone Number", anchor=W)

        #Add sample data into tree view
        self.searchResults.insert(parent='', index='end', iid=0, text="", values=("John", "Smith", 123, 8017452099))
        self.searchResults.insert(parent='', index='end', iid=1, text="", values=("Mary", "Oaks", 225, 8017052087))
        
        #Place tree view into frame
        self.searchResults.grid(row=0, column=0)

        #Add search bar frame
        self.frame2 = LabelFrame(self.frame0.scrollable_frame, text="")
        self.frame2.pack()

        #Add search bar, search bar label and select button
        self.searchLabel = Label(self.frame2, text="Search:")
        self.searchBar = Entry(self.frame2)
        self.searchBarButton = Button(self.frame2, text="Go->")
        self.selectButton = Button(self.frame2, text="Select Record")

        self.searchLabel.grid(row=0, column=0)
        self.searchBar.grid(row=0, column=1)
        self.searchBarButton.grid(row=0, column=2)
        self.selectButton.grid(row=1, column=1)

        #Add employee information area
        self.frame3 = LabelFrame(self.frame0.scrollable_frame, text="Employee Information")
        self.frame3.pack(pady=20)

        #Add employee information labels and put on grid
        self.IDLabel = Label(self.frame3, text="ID")
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

        self.IDLabel.grid(row=0, column=0) 
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

        #Add employee text boxes/checkmarks and put into frame
        self.IDLabelText = Entry(self.frame3, state='disabled')
        self.firstNameLabelText = Entry(self.frame3, state='disabled')
        self.lastNameLabelText = Entry(self.frame3, state='disabled')
        self.addressLabelText = Entry(self.frame3, state='disabled')
        self.cityLabelText = Entry(self.frame3, state='disabled')
        self.stateLabelText = Entry(self.frame3, state='disabled')
        self.zipLabelText = Entry(self.frame3, state='disabled')
        self.phoneLabelText = Entry(self.frame3, state='disabled')
        self.payTypeLabelText = Entry(self.frame3, state='disabled')

        self.IDLabelText.grid(row=1, column=0)
        self.firstNameLabelText.grid(row=1, column=1)
        self.lastNameLabelText.grid(row=1, column=2)
        self.addressLabelText.grid(row=1, column=3)
        self.cityLabelText.grid(row=1, column=4) 
        self.stateLabelText.grid(row=3, column=0)
        self.zipLabelText.grid(row=3, column=1)
        self.phoneLabelText.grid(row=3, column=2) 
        self.payTypeLabelText.grid(row=3, column=3)

        self.paymentOptions = ["Direct Deposit", "Mailed"]

        self.paymentOption = StringVar(self.frame3)
        self.paymentOption.set(self.paymentOptions[0])

        self.paymentOptionMenu = OptionMenu(self.frame3, self.paymentOption, *self.paymentOptions)
        self.paymentOptionMenu.configure(state='disabled')
        self.paymentOptionMenu.grid(row=3, column=4)

        
        self.salaryLabelText = Entry(self.frame3, state='disabled')
        self.hourlyLabelText = Entry(self.frame3, state='disabled')
        self.commissionLabelText = Entry(self.frame3, state='disabled')
        self.currentPTOLabelText = Entry(self.frame3, state='disabled')
        self.usedPTOLabelText = Entry(self.frame3, state='disabled')
        self.limitPTOLabelText = Entry(self.frame3, state='disabled')
        self.ssnLabelText= Entry(self.frame3, state='disabled')

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

        self.editorCheck = Checkbutton(self.frame3, text="", variable=self.editor, state='disabled')
        self.reporterCheck = Checkbutton(self.frame3, text="", variable=self.reporter, state='disabled')
        self.accountingCheck = Checkbutton(self.frame3, text="", variable=self.accounting, state='disabled')
        self.managerCheck = Checkbutton(self.frame3, text="", variable=self.manager, state='disabled')

        self.editorCheck.grid(row=7, column=2)
        self.reporterCheck.grid(row=7, column=3)
        self.accountingCheck.grid(row=7, column=4)
        self.managerCheck.grid(row=9, column=0)

        #Create Employee Action Button Frame
        self.frame4 = LabelFrame(self.frame0.scrollable_frame, text="Employee Actions", padx=20, pady=20)
        self.frame4.pack(pady=20)

        #Create Buttons and place in grid
        self.editButton = Button(self.frame4, text="Edit Employee Info")
        self.archiveEmployeeButton = Button(self.frame4, text="Archive Employee")
        self.unarchiveEmployeeButton = Button(self.frame4, text="Unarchive Employee")
        self.saveChangesButton = Button(self.frame4, text="Save Changes")
        self.addPTOButton = Button(self.frame4, text="Add PTO")
        self.changePaymentTypeButton = Button(self.frame4, text="Change Payment Type")

        self.editButton.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.archiveEmployeeButton.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.unarchiveEmployeeButton.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.saveChangesButton.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.addPTOButton.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        self.changePaymentTypeButton.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        #Create Company Buttons Frame
        self.frame5 = LabelFrame(self.frame0.scrollable_frame, text="Company Actions", padx=20, pady=20)
        self.frame5.pack(pady=20)

        #Create Company Buttons and place in grid
        self.addEmployeeButton = Button(self.frame5, text="Add Employee")
        self.paymentReportButton = Button(self.frame5, text="Generate Payment Report")
        self.employeeReportButton = Button(self.frame5, text="Generate Employee Data Report")

        self.addEmployeeButton.grid(row=0, column=0, padx=5, pady=5)
        self.paymentReportButton.grid(row=0, column=1, padx=5, pady=5)
        self.employeeReportButton.grid(row=0, column=2, padx=5, pady=5)

        #Create your actions button frame
        self.frame6 = LabelFrame(self.frame0.scrollable_frame, text="Your Actions", padx=20, pady=20)
        self.frame6.pack(pady=20)

        #Create your Buttons and place in grid
        self.usePTOButton = Button(self.frame6, text="Use PTO")
        self.changePasswordButton = Button(self.frame6, text="Change Password")
        self.logOutButton = Button(self.frame6, text="Log Out", command=self.logoutButtonPressed)

        self.usePTOButton.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.changePasswordButton.grid(row=0, column=1, padx=5, pady=5)
        self.logOutButton.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.frame0.pack(expand=1,  fill=Y)

        self.setInitialState()


   
        

    #Functions

    def setInitialState(self):
        #This function sets up initial state of buttons before selecting an employee
        self.paymentReportButton['state'] = 'disabled'
        self.employeeReportButton['state'] = 'disabled'
        self.editButton['state'] = 'disabled'
        self.addPTOButton['state'] = 'disabled'
        self.changePaymentTypeButton['state'] = 'disabled'
        self.archiveEmployeeButton['state'] = 'disabled'
        self.unarchiveEmployeeButton['state'] = 'disabled'
        self.addEmployeeButton['state'] = 'disabled'
        self.saveChangesButton['state'] = 'disabled'


    def goButtonPressed(self):
        print("Go")
        #searchBarButton['state'] = 'disabled'
        

    def selectRecordButtonPressed(self):
        print("Select record")
        #selectedRecord would equal the one we find in database
        selectedRecord = "The one we clicked on"
        self.setState(selectedRecord)

    def editButtonPressed(self):
        print("Edit")
    
    def archiveEmpButtonPressed(self):
        print("Archived Emp")

    def unArchiveEmpButtonPressed(self):
        print("Unarchived Emp")

    def addPTOButtonPressed(self):
        print("added PTO")

    def changePaymentTypePressed(self):
        print("Changed payment type")

    def saveButtonPressed(self):
        print("Saved changes")

    def addEmpButtonPressed(self):
        print("Added Emp")

    def paymentReportButtonPressed(self):
        print("Payment report generated")

    def empReportButtonPressed(self):
        print("Emp report generated")

    def usePTOButtonPressed(self):
        print("PTO used")

    def changePasswordButtonPressed(self):
        print("Password changed")

    def logoutButtonPressed(self):
        from login import LoginScreen
        self.window.destroy()
        login = LoginScreen()


    def setState(self, loggedInUser):
        #Set up button states for loggedInUser

        if not self.loggedInUser.permissions.Reporting_Permission:
            self.paymentReportButton['state'] = 'disabled'
            self.employeeReportButton['state'] = 'disabled'
            

        if not self.loggedInUser.permissions.Editing_Permission:
            self.editButton['state'] = 'disabled'
            self.addPTOButton['state'] = 'disabled'
            self.changePaymentTypeButton['state'] = 'disabled'
            

        if not self.loggedInUser.permissions.Manager_Permission:
            self.archiveEmployeeButton['state'] = 'disabled'
            self.unarchiveEmployeeButton['state'] = 'disabled'
            self.addEmployeeButton['state'] = 'disabled'
            

    def showData(self, selectedUser):
        #This determines what things the user can see (I haven't written it yet)
        if self.loggedInUser.permissions.Accounting_Permission:
            #give accounting permision
            print("no")
        else:
            #Don't let them see stuff
            print("Ok")

    
        
        