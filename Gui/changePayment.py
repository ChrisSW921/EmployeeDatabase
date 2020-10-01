from tkinter import *
from tkinter import ttk

class paymentWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Payment Method")
        self.window.geometry('500x300')

        #Create Frame
        frame1 = LabelFrame(self.window, text="")
        frame1.pack()

        