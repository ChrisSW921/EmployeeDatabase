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

        #Create tree view in frame
        frame1 = LabelFrame(self.window, text="", padx=10, pady=10)
        frame1.pack(padx=10, pady=10)
        searchResults = ttk.Treeview(frame1)
        searchResults['columns'] = ("First Name", "Last Name", "ID", "Phone Number")

        # Format tree view
        searchResults.column("#0", width=0, minwidth=0)
        searchResults.column("First Name", anchor=CENTER)
        searchResults.column("Last Name", anchor=CENTER)    
        searchResults.column("ID", anchor=CENTER)
        searchResults.column("Phone Number", anchor=CENTER)

        #Create Headings
        searchResults.heading("#0", text="", anchor=W)
        searchResults.heading("First Name", text="First Name", anchor=W)
        searchResults.heading("Last Name", text="Last Name", anchor=W)
        searchResults.heading("ID", text="ID", anchor=W)
        searchResults.heading("Phone Number", text="Phone Number", anchor=W)

        #Add Data
        searchResults.insert(parent='', index='end', iid=0, text="", values=("John", "Smith", 123, 8017852099))
        #Place tree view
        searchResults.grid(row=0, column=0)

        #Add search bar frame
        frame2 = LabelFrame(self.window, text="")
        frame2.pack()
        #Add search bar and label
        searchLabel = Label(frame2, text="Search:")
        searchBar = Entry(frame2)
        searchLabel.grid(row=0, column=0)
        searchBar.grid(row=0, column=1)
        searchBarButton = Button(frame2, text="Go->")
        searchBarButton.grid(row=0, column=2)
    
        
        


if __name__ == '__main__':

    test = Login()

    #root = Tk()

    # root.geometry('425x225')
    # application = Login(root)

    #root.mainloop()
   # test = MainMenu('jack')