from tkinter import *
from tkinter import ttk

class addPTOWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Add PTO")
        self.window.geometry('500x300')