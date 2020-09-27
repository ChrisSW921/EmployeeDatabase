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
        searchResults.insert(parent='', index='end', iid=0, text="", values=("John", "Smith", 123, 8017852099))
        
        #Place tree view into frame
        searchResults.grid(row=0, column=0)

        #Add search bar frame
        frame2 = LabelFrame(self.window, text="")
        frame2.pack()

        #Add search bar, search bar label and select button
        searchLabel = Label(frame2, text="Search:")
        searchBar = Entry(frame2)
        searchLabel.grid(row=0, column=0)
        searchBar.grid(row=0, column=1)
        searchBarButton = Button(frame2, text="Go->")
        searchBarButton.grid(row=0, column=2)
        selectButton = Button(frame2, text="Select Record")
        selectButton.grid(row=1, column=1)

        #Add employee information area
        frame3 = LabelFrame(self.window, text="Employee Information")
        frame3.pack()

        #Add employee information labels
        IDLabel = Label(frame3, text="ID")
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

        #Add employee text boxes/checkmarks
        IDLabelText = Entry(frame3)
        firstNameLabelText = Entry(frame3)
        lastNameLabelText = Entry(frame3)
        addressLabelText = Entry(frame3)
        cityLabelText = Entry(frame3)
        stateLabelText = Entry(frame3)
        zipLabelText = Entry(frame3)
        phoneLabelText = Entry(frame3)
        payTypeLabelText = Entry(frame3)
        payMethodLabelText = Entry(frame3)
        salaryLabelText = Entry(frame3)
        hourlyLabelText = Entry(frame3)
        commissionLabelText = Entry(frame3)
        currentPTOLabelText = Entry(frame3)
        usedPTOLabelText = Entry(frame3)
        limitPTOLabelText = Entry(frame3)
        ssnLabelText= Entry(frame3)

        editor = IntVar()
        reporter = IntVar()
        accounting = IntVar()
        manager = IntVar()

        editorCheck = Checkbutton(frame3, text="", variable=editor)
        reporterCheck = Checkbutton(frame3, text="", variable=reporter)
        accountingCheck = Checkbutton(frame3, text="", variable=accounting)
        managerCheck = Checkbutton(frame3, text="", variable=manager)

        #Put employee labels into frame
        IDLabel.grid(row=0, column=0) 
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

        #Put employe text areas into frame
        IDLabelText.grid(row=1, column=0) 
        firstNameLabelText.grid(row=1, column=1) 
        lastNameLabelText.grid(row=1, column=2) 
        addressLabelText.grid(row=1, column=3) 
        cityLabelText.grid(row=1, column=4) 
        stateLabelText.grid(row=3, column=0) 
        zipLabelText.grid(row=3, column=1) 
        phoneLabelText.grid(row=3, column=2) 
        payTypeLabelText.grid(row=3, column=3) 
        payMethodLabelText.grid(row=3, column=4) 
        salaryLabelText.grid(row=5, column=0) 
        hourlyLabelText.grid(row=5, column=1) 
        commissionLabelText.grid(row=5, column=2) 
        currentPTOLabelText.grid(row=5, column=3) 
        usedPTOLabelText.grid(row=5, column=4) 
        limitPTOLabelText.grid(row=7, column=0) 
        ssnLabelText.grid(row=7, column=1)

        #Put checkboxes into frame
        editorCheck.grid(row=7, column=2)
        reporterCheck.grid(row=7, column=3)
        accountingCheck.grid(row=7, column=4)
        managerCheck.grid(row=9, column=0)


        
        


if __name__ == '__main__':

    test = Login()

    #root = Tk()

    # root.geometry('425x225')
    # application = Login(root)

    #root.mainloop()
   # test = MainMenu('jack')