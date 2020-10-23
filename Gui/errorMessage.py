from tkinter import *
from tkinter import ttk


class errorWindow:
    def __init__(self, message):
        self.message = message
        self.window = Tk()
        self.window.title("ERROR")

        errorMessage = Label(text=self.message)
        okButton = Button(text='OK')

        errorMessage.grid(row=0, column=0)
        okButton.grid(row=1,column=0, padx=15)
        

        def okButtonPressed():
            self.window.destroy()
            print("Done")


