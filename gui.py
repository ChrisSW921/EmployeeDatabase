"""GUI Code File"""
from tkinter import *
from tkinter import ttk

#Set up login page with username and password
class Login:

    def __init__(self):

        self.root = Tk()
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        ttk.Button(text='LOGIN',command=self.loginUser).grid(row=3,column=2)
        self.root.mainloop()


    def loginUser(self):
        self.root.destroy()
        #code to create user from data in username field
        user = "Fake user"
        menu = MainMenu(user)

#Set up home page, showing certain buttons to create user to only select access levels. Home page
#will include option to update/delete/view employees as well as to create new users. 

class MainMenu:

    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Main Menu")
        self.window.geometry('1500x1000')

        #Create tree view frame
        frame1 = LabelFrame(self.window, text="")
        frame1.pack()

        #Create tree view
        searchResults = ttk.Treeview(frame1)
        searchResults['columns'] = ("First Name", "Last Name", "ID", "Phone Number")

        # Format tree view
        searchResults.column("#0", width=0, minwidth=0)
        searchResults.column("First Name", anchor=CENTER)
        searchResults.column("Last Name", anchor=CENTER)    
        searchResults.column("ID", anchor=CENTER)
        searchResults.column("Phone Number", anchor=CENTER)

        #Create Tree View Headings
        searchResults.heading("#0", text="", anchor=W)
        searchResults.heading("First Name", text="First Name", anchor=W)
        searchResults.heading("Last Name", text="Last Name", anchor=W)
        searchResults.heading("ID", text="ID", anchor=W)
        searchResults.heading("Phone Number", text="Phone Number", anchor=W)

        #Add sample data into tree view
        searchResults.insert(parent='', index='end', iid=0, text="", values=("John", "Smith", 123, 8017452099))
        searchResults.insert(parent='', index='end', iid=1, text="", values=("Mary", "Oaks", 225, 8017052087))
        
        #Place tree view into frame
        searchResults.grid(row=0, column=0)

        #Add search bar frame
        frame2 = LabelFrame(self.window, text="")
        frame2.pack()

        #Add search bar, search bar label and select button
        searchLabel = Label(frame2, text="Search:").grid(row=0, column=0)
        searchBar = Entry(frame2).grid(row=0, column=1)
        searchBarButton = Button(frame2, text="Go->").grid(row=0, column=2)
        selectButton = Button(frame2, text="Select Record").grid(row=1, column=1)

        #Add employee information area
        frame3 = LabelFrame(self.window, text="Employee Information")
        frame3.pack()

        #Add employee information labels and put on grid
        IDLabel = Label(frame3, text="ID").grid(row=0, column=0) 
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

        #Add employee text boxes/checkmarks and put into frame
        IDLabelText = Entry(frame3).grid(row=1, column=0)
        firstNameLabelText = Entry(frame3).grid(row=1, column=1)
        lastNameLabelText = Entry(frame3).grid(row=1, column=2)
        addressLabelText = Entry(frame3).grid(row=1, column=3)
        cityLabelText = Entry(frame3).grid(row=1, column=4) 
        stateLabelText = Entry(frame3).grid(row=3, column=0)
        zipLabelText = Entry(frame3).grid(row=3, column=1)
        phoneLabelText = Entry(frame3).grid(row=3, column=2) 
        payTypeLabelText = Entry(frame3).grid(row=3, column=3)
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

        #Create Employee Action Button Frame
        frame4 = LabelFrame(self.window, text="Employee Actions", padx=20, pady=20)
        frame4.pack()

        #Create Buttons and place in grid
        paymentReportButton = Button(frame4, text="Generate Payment Report").grid(row=0, column=2, padx=5, pady=5)
        employeeReportButton = Button(frame4, text="Generate Employee Data Report").grid(row=0, column=1, padx=5, pady=5)
        editButton = Button(frame4, text="Edit Selected Employee").grid(row=0, column=0, padx=5, pady=5)
        changePasswordButton = Button(frame4, text="Change Password").grid(row=0, column=3, padx=5, pady=5)
        addEmployeeButton = Button(frame4, text="Add Employee").grid(row=0, column=4, padx=5, pady=5)
        archiveEmployeeButton = Button(frame4, text="Archive Employee").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        unarchiveEmployeeButton = Button(frame4, text="Unarchive Employee").grid(row=1, column=1, padx=5, pady=5, sticky=W)
        saveChangesButton = Button(frame4, text="Save Changes").grid(row=1, column=2, padx=5, pady=5, sticky=W)
        requestPTOButton = Button(frame4, text="Request PTO").grid(row=1, column=3, padx=5, pady=5, sticky=W)
        
        


if __name__ == '__main__':

    test = Login()

    #root = Tk()

    # root.geometry('425x225')
    # application = Login(root)

    #root.mainloop()
   # test = MainMenu('jack')