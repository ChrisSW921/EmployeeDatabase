"""GUI Code File"""
from tkinter import *
from tkinter import ttk
from mainScreen import MainMenu
from morePTO import addPTOWindow
from lessPTO import usePTOWindow
from newPassword import changePasswordWindow
from newEmp import addEmpWindow
from errorMessage import errorWindow
from changePayment import paymentWindow

#Set up login page with username and password
class Login:
    """Login class. First class that employee will interact with.
    They will login with ID and their password"""

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
        new = addEmpWindow("f")
        # menu = MainMenu(user)





if __name__ == '__main__':
    test = Login()
