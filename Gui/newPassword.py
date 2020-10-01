from tkinter import *
from tkinter import ttk

class changePasswordWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Password")
        self.window.geometry('500x300')