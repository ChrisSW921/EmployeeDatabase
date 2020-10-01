from tkinter import *
from tkinter import ttk

class addEmpWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add New Employee")
        self.window.geometry('500x300')