"""GUI Code File"""
print("Why")

from tkinter import *
from tkinter import ttk

class Login:

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        ttk.Button(text='LOGIN',command=self.loginUser).grid(row=3,column=2)


    def loginUser(self):
        root.destroy()
        menu = MainMenu(Tk())


class MainMenu:

    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry('1000x1000')
        Label(text = ' Welcome ',font='Times 15').grid(row=1,column=1,pady=20)

if __name__ == '__main__':

    root = Tk()
    root.geometry('425x225')
    application = Login(root)

    root.mainloop()


#Set up home page, showing certain buttons to create user to only select access levels. Home page
#will include option to update/delete/view employees as well as to create new users. 


#Set up necessary pop ups for error validation, deleted and saved messages. 