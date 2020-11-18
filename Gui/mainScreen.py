#Set up home page, showing certain buttons to create user to only select access levels. Home page
#will include access to all major and minor features of software. . 

from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.insert(0,os.getcwd())
from Gui.login import LoginScreen
from Gui.changePayment import paymentWindow
from Gui.lessPTO import usePTOWindow
from Gui.morePTO import addPTOWindow
from Gui.newEmp import addEmpWindow
from Gui.newPassword import changePasswordWindow
from Gui.scrollable import ScrollableFrame
from Backend.employee import Employee
from Database import database
from Gui.errorMessage import errorWindow
from Gui.empReport import empReporting
from Gui.addReceipt import addReceiptWindow
from Gui.addTimeCard import addTimeCardWindow
from Gui.currentUserPassChange import changeUserPassword

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
        self.searchResults['columns'] = ("ID", "First Name", "Last Name", "Phone Number")

        # Format tree view
        self.searchResults.column("#0", width=0, minwidth=0)
        self.searchResults.column("ID", anchor=CENTER)
        self.searchResults.column("First Name", anchor=CENTER)
        self.searchResults.column("Last Name", anchor=CENTER)    
        self.searchResults.column("Phone Number", anchor=CENTER)

        #Create Tree View Headings
        self.searchResults.heading("#0", text="", anchor=W)
        self.searchResults.heading("First Name", text="First Name", anchor=W)
        self.searchResults.heading("Last Name", text="Last Name", anchor=W)
        self.searchResults.heading("ID", text="ID", anchor=W)
        self.searchResults.heading("Phone Number", text="Phone Number", anchor=W)
        
        #Place tree view into frame
        self.searchResults.grid(row=0, column=0)

        #Add search bar frame
        self.frame2 = LabelFrame(self.frame0.scrollable_frame, text="")
        self.frame2.pack()

        #Add search bar, search bar label and select button
        self.searchLabel = Label(self.frame2, text="Search:")
        self.searchBar = Entry(self.frame2)
        self.searchBarButton = Button(self.frame2, text="Go->", command=self.goButtonPressed)
        self.selectButton = Button(self.frame2, text="Select Record", command=self.selectRecordButtonPressed)

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
        self.addressLabel = Label(self.frame3, text="Address")
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
        self.archivedLabel = Label(self.frame3, text="Archived")

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
        self.archivedLabel.grid(row=8, column=1)

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
        self.archivedCheck = IntVar()

        self.editorCheck = Checkbutton(self.frame3, text="", variable=self.editor, state='disabled')
        self.reporterCheck = Checkbutton(self.frame3, text="", variable=self.reporter, state='disabled')
        self.accountingCheck = Checkbutton(self.frame3, text="", variable=self.accounting, state='disabled')
        self.managerCheck = Checkbutton(self.frame3, text="", variable=self.manager, state='disabled')
        self.archivedCheck = Checkbutton(self.frame3, text="", variable=self.archivedCheck, state='disabled')

        self.editorCheck.grid(row=7, column=2)
        self.reporterCheck.grid(row=7, column=3)
        self.accountingCheck.grid(row=7, column=4)
        self.managerCheck.grid(row=9, column=0)
        self.archivedCheck.grid(row=9, column=1)

        #Create Employee Action Button Frame
        self.frame4 = LabelFrame(self.frame0.scrollable_frame, text="Employee Actions", padx=20, pady=20)
        self.frame4.pack(pady=20)

        #Create Buttons and place in grid
        self.editButton = Button(self.frame4, text="Edit Employee Info", command=self.editButtonPressed)
        self.archiveEmployeeButton = Button(self.frame4, text="Archive", command=self.archiveEmpButtonPressed)
        self.unarchiveEmployeeButton = Button(self.frame4, text="Unarchive", command=self.unArchiveEmpButtonPressed)
        self.saveChangesButton = Button(self.frame4, text="Save Changes", command=self.saveButtonPressed)
        self.addPTOButton = Button(self.frame4, text="Add PTO", command=self.addPTOButtonPressed)
        self.resetPTOButton = Button(self.frame4, text="Clear Used PTO", command=self.resetPTOButtonPressed)
        self.changePaymentTypeButton = Button(self.frame4, text="Change Payment Type", command=self.changePaymentTypePressed)
        self.addReceiptButton = Button(self.frame4, text="Add Receipt", command=self.addReceiptButtonPressed)
        self.addTimeCardButton = Button(self.frame4, text="Add Time Card", command=self.addTimeCardButtonPressed)

        self.editButton.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.archiveEmployeeButton.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.unarchiveEmployeeButton.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.saveChangesButton.grid(row=1, column=2, padx=5, pady=5, sticky=EW, columnspan=2)
        self.addPTOButton.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        self.resetPTOButton.grid(row=0, column=4, padx=5, pady=5, sticky=W)
        self.changePaymentTypeButton.grid(row=0, column=5, padx=5, pady=5, sticky=W)
        self.addReceiptButton.grid(row=0, column=6, padx=5, pady=5, sticky=W)
        self.addTimeCardButton.grid(row=0, column=7, padx=5, pady=5, sticky=W)

        #Create Company Buttons Frame
        self.frame5 = LabelFrame(self.frame0.scrollable_frame, text="Company Actions", padx=20, pady=20)
        self.frame5.pack(pady=20)

        #Create Company Buttons and place in grid
        self.addEmployeeButton = Button(self.frame5, text="Add Employee", command=self.addEmpButtonPressed)
        self.paymentReportButton = Button(self.frame5, text="Generate Payment Report", command=self.paymentReportButtonPressed)
        self.employeeReportButton = Button(self.frame5, text="Generate Employee Data Report", command=self.empReportButtonPressed)

        self.addEmployeeButton.grid(row=0, column=0, padx=5, pady=5)
        self.paymentReportButton.grid(row=0, column=1, padx=5, pady=5)
        self.employeeReportButton.grid(row=0, column=2, padx=5, pady=5)

        #Create your actions button frame
        self.frame6 = LabelFrame(self.frame0.scrollable_frame, text="Your Actions", padx=20, pady=20)
        self.frame6.pack(pady=20)

        #Create your Buttons and place in grid
        self.usePTOButton = Button(self.frame6, text="Use PTO", command=self.usePTOButtonPressed)
        self.changePasswordButton = Button(self.frame6, text="Change Password", command=self.changePasswordButtonPressed)
        self.logOutButton = Button(self.frame6, text="Log Out", command=self.logoutButtonPressed)

        self.usePTOButton.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.changePasswordButton.grid(row=0, column=1, padx=5, pady=5)
        self.logOutButton.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.frame0.pack(expand=1,  fill=Y)

        self.setInitialState()
        #self.selectRecordButtonPressed()


   
        

    #Functions

    def setInitialState(self):
        #This function sets up initial state of buttons before selecting an employee
        self.editButton['state'] = 'disabled'
        self.addPTOButton['state'] = 'disabled'
        self.archiveEmployeeButton['state'] = 'disabled'
        self.unarchiveEmployeeButton['state'] = 'disabled'
        self.saveChangesButton['state'] = 'disabled'
        self.changePaymentTypeButton['state'] = 'disabled'
        self.resetPTOButton['state'] = 'disabled'
        self.addReceiptButton['state'] = 'disabled'
        self.addTimeCardButton['state'] = 'disabled'

        if not self.loggedInUser.Permissions.Reporting_Permission or not self.loggedInUser.Permissions.Manager_Permission:
            self.paymentReportButton['state'] = 'disabled'
            self.employeeReportButton['state'] = 'disabled'
            

        if not self.loggedInUser.Permissions.Manager_Permission:
            self.addEmployeeButton['state'] = 'disabled'
            
    


    def goButtonPressed(self):
        "This function searches the database and displays relative inforation in the tree view"

        #Clear former rows
        formerRows = self.searchResults.get_children()
        for row in formerRows:
            self.searchResults.delete(row)

        #Find the list of employees you searched for
        if self.searchBar.get() in ['1', 'System', 'Admin']:
            queryResults = database.search_employees('0')
        else:
            queryResults = database.search_employees(self.searchBar.get())
        
        #Put employees into treeview
            iid = 0
            for item in queryResults:
                self.searchResults.insert(parent='', index='end', iid=iid, text="", values=(item.EmpId,item.First_Name, item.Last_Name, item.Phone_Number))
                iid += 1

    def selectRecordButtonPressed(self):
        """This function takes the record you clicked on and displays the employees 
        information in the boxes on the GUI"""

        try:
            curEmp = self.searchResults.focus()
            userID = self.searchResults.item(curEmp)['values'][0]  
            selectedUser = database.get_employee(userID)
            self.selectedUser = selectedUser
        except:
            errorWindow("Please select a record")
            self.setInitialState()

        

        #Set states to normal to be able to populate them with data
        self.IDLabelText['state'] = 'normal'
        self.firstNameLabelText['state'] = 'normal'
        self.lastNameLabelText['state'] = 'normal'
        self.addressLabelText['state'] = 'normal'
        self.cityLabelText['state'] = 'normal'
        self.stateLabelText['state'] = 'normal'
        self.zipLabelText['state'] = 'normal'
        self.phoneLabelText['state'] = 'normal'
        self.payTypeLabelText['state'] = 'normal'

        self.salaryLabelText['state'] = 'normal'
        self.commissionLabelText['state'] = 'normal'
        self.hourlyLabelText['state'] = 'normal'
        self.ssnLabelText['state'] = 'normal'
        self.currentPTOLabelText['state'] = 'normal'
        self.usedPTOLabelText['state'] = 'normal'
        self.limitPTOLabelText['state'] = 'normal'
        self.paymentOptionMenu.configure(state='normal')


        #Delete former selected items
        self.IDLabelText.delete(0, 'end') 
        self.firstNameLabelText.delete(0, 'end')
        self.lastNameLabelText.delete(0, 'end')
        self.addressLabelText.delete(0, 'end')
        self.cityLabelText.delete(0, 'end')
        self.stateLabelText.delete(0, 'end')
        self.zipLabelText.delete(0, 'end')
        self.phoneLabelText.delete(0, 'end')
        self.payTypeLabelText.delete(0, 'end')

        self.salaryLabelText.delete(0, 'end')
        self.commissionLabelText.delete(0, 'end')
        self.hourlyLabelText.delete(0, 'end')
        self.ssnLabelText.delete(0, 'end')
        self.currentPTOLabelText.delete(0, 'end')
        self.usedPTOLabelText.delete(0, 'end')
        self.limitPTOLabelText.delete(0, 'end')



        #Populate data
        self.IDLabelText.insert(0, selectedUser.EmpId) 
        self.firstNameLabelText.insert(0, selectedUser.First_Name)
        self.lastNameLabelText.insert(0, selectedUser.Last_Name)
        self.addressLabelText.insert(0, selectedUser.Address.Street_Address)
        self.cityLabelText.insert(0, selectedUser.Address.City)
        self.stateLabelText.insert(0, selectedUser.Address.State)
        self.zipLabelText.insert(0, selectedUser.Address.Zip_Code)
        self.phoneLabelText.insert(0, selectedUser.Phone_Number)

        if selectedUser.Pay_Type == 1:
            self.payTypeLabelText.insert(0, "Salaried")
            if self.loggedInUser.Permissions.Manager_Permission or self.loggedInUser.Permissions.Accounting_Permission:
                self.salaryLabelText.insert(0, selectedUser.Salary)
        elif selectedUser.Pay_Type == 2:
            self.payTypeLabelText.insert(0, "Commissioned")
            if self.loggedInUser.Permissions.Manager_Permission or self.loggedInUser.Permissions.Accounting_Permission:
                self.commissionLabelText.insert(0, selectedUser.Commission)
                self.salaryLabelText.insert(0, selectedUser.Salary)
        else:
            self.payTypeLabelText.insert(0, "Hourly")
            if self.loggedInUser.Permissions.Manager_Permission or self.loggedInUser.Permissions.Accounting_Permission:
                self.hourlyLabelText.insert(0, selectedUser.Hourly)
        
        if self.loggedInUser.Permissions.Manager_Permission or self.loggedInUser.Permissions.Accounting_Permission:
            self.ssnLabelText.insert(0, selectedUser.Credentials.SSN) 

        self.currentPTOLabelText.insert(0, selectedUser.PTO.Current_PTO)
        self.usedPTOLabelText.insert(0, selectedUser.PTO.Used_PTO)
        self.limitPTOLabelText.insert(0, selectedUser.PTO.PTO_Limit)

        if selectedUser.Pay_Method == 1:
            self.paymentOption.set(self.paymentOptions[0])
        else:
            self.paymentOption.set(self.paymentOptions[1])

        #Disable areas again to prevent editing
        self.IDLabelText['state'] = 'disabled'
        self.firstNameLabelText['state'] = 'disabled'
        self.lastNameLabelText['state'] = 'disabled'
        self.addressLabelText['state'] = 'disabled'
        self.cityLabelText['state'] = 'disabled'
        self.stateLabelText['state'] = 'disabled'
        self.zipLabelText['state'] = 'disabled'
        self.phoneLabelText['state'] = 'disabled'
        self.payTypeLabelText['state'] = 'disabled'

        self.salaryLabelText['state'] = 'disabled'
        self.commissionLabelText['state'] = 'disabled'
        self.hourlyLabelText['state'] = 'disabled'
        self.ssnLabelText['state'] = 'disabled'
        self.currentPTOLabelText['state'] = 'disabled'
        self.usedPTOLabelText['state'] = 'disabled'
        self.limitPTOLabelText['state'] = 'disabled'
        self.paymentOptionMenu.configure(state='disabled')

        #Display selected employees permissions
        if selectedUser.Permissions.Editing_Permission:
            self.editorCheck['state'] = 'normal'
            self.editorCheck.select()
            self.editorCheck['state'] = 'disabled'
        else:
            self.editorCheck['state'] = 'normal'
            self.editorCheck.deselect()
            self.editorCheck['state'] = 'disabled'
            

        if selectedUser.Permissions.Accounting_Permission:
            self.accountingCheck['state'] = 'normal'
            self.accountingCheck.select()
            self.accountingCheck['state'] = 'disabled'
        else:
            self.accountingCheck['state'] = 'normal'
            self.accountingCheck.deselect()
            self.accountingCheck['state'] = 'disabled'

        if selectedUser.Permissions.Reporting_Permission:
            self.reporterCheck['state'] = 'normal'
            self.reporterCheck.select()
            self.reporterCheck['state'] = 'disabled'
        else:
            self.reporterCheck['state'] = 'normal'
            self.reporterCheck.deselect()
            self.reporterCheck['state'] = 'disabled'

        if selectedUser.Permissions.Manager_Permission:
            self.managerCheck['state'] = 'normal'
            self.managerCheck.select()
            self.managerCheck['state'] = 'disabled'
        else:
            self.managerCheck['state'] = 'normal'
            self.managerCheck.deselect()
            self.managerCheck['state'] = 'disabled'

        if selectedUser.Archived:
            self.archivedCheck['state'] = 'normal'
            self.archivedCheck.select()
            self.archivedCheck['state'] = 'disabled'
        else:
            self.archivedCheck['state'] = 'normal'
            self.archivedCheck.deselect()
            self.archivedCheck['state'] = 'disabled'
        



        #Display certain buttons to logged in employee after selecting an employee

        if self.loggedInUser.Permissions.Manager_Permission:
            self.editButton['state'] = 'normal'
            self.addPTOButton['state'] = 'normal'
            self.saveChangesButton['state'] = 'normal'
            self.changePaymentTypeButton['state'] = 'normal'
            self.resetPTOButton['state'] = 'normal'

            if self.selectedUser.Pay_Type == 3:
                self.addTimeCardButton['state'] = 'normal'
                self.addReceiptButton['state'] = 'disabled'
            elif self.selectedUser.Pay_Type == 2:
                self.addReceiptButton['state'] = 'normal'
                self.addTimeCardButton['state'] = 'disabled'
            else:
                self.addTimeCardButton['state'] = 'disabled'
                self.addReceiptButton['state'] = 'disabled'
                
            if selectedUser.Archived:
                self.archiveEmployeeButton['state'] = 'disabled'
                self.unarchiveEmployeeButton['state'] = 'normal'
            else:
                self.archiveEmployeeButton['state'] = 'normal'
                self.unarchiveEmployeeButton['state'] = 'disabled'

        if self.loggedInUser.Permissions.Editing_Permission:
            self.editButton['state'] = 'normal'
            self.addPTOButton['state'] = 'normal'
            self.saveChangesButton['state'] = 'normal'
    

    def editButtonPressed(self):

        """This function unlocks the text areas and allows editing of an employee"""
        #Set the text entry states to normal
        self.firstNameLabelText['state'] = 'normal'
        self.lastNameLabelText['state'] = 'normal'
        self.addressLabelText['state'] = 'normal'
        self.cityLabelText['state'] = 'normal'
        self.stateLabelText['state'] = 'normal'
        self.zipLabelText['state'] = 'normal'
        self.phoneLabelText['state'] = 'normal'
        self.paymentOptionMenu.configure(state='normal')
        self.editorCheck['state'] = 'normal'
        self.accountingCheck['state'] = 'normal'
        self.reporterCheck['state'] = 'normal'
        self.managerCheck['state'] = 'normal'

    
    def archiveEmpButtonPressed(self):
        """"This will archive the currently selected employee"""
        self.selectedUser.Archived = True
        self.selectedUser.save()
        self.selectRecordButtonPressed()
        errorWindow('Employee Archived!')
        

    def unArchiveEmpButtonPressed(self):
        """This will unarchive the currently selected employee"""
        self.selectedUser.Archived = False
        self.selectedUser.save()
        self.selectRecordButtonPressed()
        errorWindow('Employee Unarchived!')
        
        

    def addPTOButtonPressed(self):
        """This button brings up the screen to add more PTO"""
        morePTO = addPTOWindow(self.selectedUser)
       

    def changePaymentTypePressed(self):
        """This button brings up the screen to change the selected users payment type/pay amount"""
        newPayment = paymentWindow(self.selectedUser)
        

    def saveButtonPressed(self):
        """This function saves the edited information for the currently selected employee"""
        #Initialize variables for text entry spaces
        firstName = self.firstNameLabelText.get()
        lastName = self.lastNameLabelText.get()
        address = self.addressLabelText.get()
        city = self.cityLabelText.get()
        state = self.stateLabelText.get()
        zipcode = self.zipLabelText.get()
        phone = self.phoneLabelText.get()
        editing = self.editor.get()
        reporting = self.reporter.get()
        accounting = self.accounting.get()
        manager = self.manager.get()

        allFields = [firstName, lastName, address, city, state, zipcode, phone] 

        states = ['alaska', 'alabama', 'arkansas', 'american samoa', 'arizona', ' alifornia', 'colorado',
         'connecticut', 'district of columbia', 'delaware', 'florida', 'georgia', 'guam', 'hawaii', 'iowa',
          'idaho', 'illinois', 'indiana', 'kansas', 'kentucky', 'louisiana', 'massachusetts', 'maryland', 
          'maine', 'michigan', 'minnesota', 'missouri', 'mississippi', 'montana', 'north carolina', 
          ' north dakota', 'nebraska', 'new hampshire', 'new jersey', 'new mexico', 'nevada', 'new york',
           'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'puerto rico', 'rhode island', 'south carolina', 
           'south dakota', 'tennessee', 'texas', 'utah', 'virginia', 'virgin islands', 'vermont', 'washington', 
           'wisconsin', 'west virginia', 'wyoming']
        
        #Error checking to make sure state is valid and all fields are filled out
        empty = 0

        for field in allFields:
            if len(field) == 0:
                empty += 1
        
        if empty > 0:
            errorWindow("Please fill out all fields")
        elif state.lower() not in states:
            errorWindow("Please type a valid state-also no abbreviations")
        elif re.search('[a-zA-Z]', phone):
            errorWindow("Only numbers allowed for phone number")
        elif re.search('[a-zA-Z]', zipcode):
            errorWindow("Only numbers allowed for zipcode")
        elif not zipcode.isalnum():
            errorWindow('Only enter numbers, no special characters or spaces for zipcode')
        else:
            #Update employee
            managerperm = False
            accountperm = False
            reportperm = False
            editperm = False

            if manager == 1:
                managerperm = True
            if accounting == 1:
                accountperm = True
            if reporting == 1:
                reportperm = True
            if editing == 1:
                editperm = True

            self.selectedUser.First_Name = firstName
            self.selectedUser.Last_Name = lastName
            self.selectedUser.Phone_Number = phone
            self.selectedUser.Address.Street_Address = address
            self.selectedUser.Address.City = city
            self.selectedUser.Address.State = state
            self.selectedUser.Address.Zip_Code = zipcode
            self.selectedUser.Permissions.Accounting_Permission = accountperm
            self.selectedUser.Permissions.Editing_Permission = editperm
            self.selectedUser.Permissions.Reporting_Permission = reportperm
            self.selectedUser.Permissions.Manager_Permission = managerperm
            if self.paymentOption.get() == "Direct Deposit":
                self.selectedUser.Pay_Method = 1
            else:
                self.selectedUser.Pay_Method = 2

            self.selectedUser.save()
            errorWindow("Employee info updated!")
            self.selectRecordButtonPressed()

    def addEmpButtonPressed(self):
        """This function brings up the new employee window"""
        newEmp = addEmpWindow()
        

    def paymentReportButtonPressed(self):
        """This function brings up the payment report button"""
        empReporting(self.selectedUser, 'payment')
        print("Payment report generated")

    def empReportButtonPressed(self):
        """This function brings up the employee report button"""
        empReporting(self.selectedUser, 'employee')
        print("Emp report generated")

    def usePTOButtonPressed(self):
        """This function brings up the window to use PTO for logged in user"""
        lessPTO = usePTOWindow(self.loggedInUser)
        

    def changePasswordButtonPressed(self):
        """This function brings up the window to change the password for a user"""
        newPassword = changeUserPassword(self.loggedInUser)

    def logoutButtonPressed(self):
        """This function logs out the user"""
        self.window.destroy()
        login = LoginScreen()
            
    def resetPTOButtonPressed(self):
        """This function resets the users PTO"""
        self.selectedUser.PTO.Used_PTO = 0
        self.selectedUser.save()
        errorWindow("Used PTO reset to 0! Select record again to see update")

    def addReceiptButtonPressed(self):
        addingReceipt = addReceiptWindow(self.selectedUser)
    
    def addTimeCardButtonPressed(self):
        addingTimeCard = addTimeCardWindow(self.selectedUser)

    
        
        