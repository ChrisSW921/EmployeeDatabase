"""GUI Code File"""
import sys
import os
sys.path.insert(0,os.getcwd())

from tkinter import *
from tkinter import ttk
from mainScreen import MainMenu
from morePTO import addPTOWindow
from lessPTO import usePTOWindow
from newPassword import changePasswordWindow
from newEmp import addEmpWindow
from errorMessage import errorWindow
from changePayment import paymentWindow
from empReport import empReporting

from Backend.employee import Employee
from Database import database


#Set up login page with username and password
class LoginScreen:
    """Login class. First class that employee will interact with.
    They will login with ID and their password"""

    def __init__(self):
        self.root = Tk()
        self.root.title('LOGIN SCREEN')

        Label(text = ' Employee ID ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        loginButton = Button(text='Login',command=self.loginUser)
        loginButton.grid(row=3,column=1)

        forgotPasswordButton = Button(text='Forgot Password', command=self.newPassword)
        forgotPasswordButton.grid(row=3, column=2)
        self.root.mainloop()


    def loginUser(self):
        """Logins the user with credentials"""
        try:
            userId = int(self.username.get())
            password = self.password.get()
            credentialsVerified = database.verify_credentials(userId, password)
            
            if(credentialsVerified):
                currentUser = database.get_employee(userId)
                self.root.destroy()
                MainMenu(currentUser)
            else:
                errorWindow("Username or password was wrong, please try again")

        except ValueError:
            errorWindow("Please enter an integer in the id field")

        except TypeError:
            errorWindow("Could not find employee under id: " + str(userId))

    def newPassword(self):
        """Opens new password window"""
        changePasswordWindow()




if __name__ == '__main__':
    test = LoginScreen()
