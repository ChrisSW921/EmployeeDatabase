from tkinter import *
from tkinter import ttk

class usePTOWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Use PTO")
        self.window.geometry('500x300')