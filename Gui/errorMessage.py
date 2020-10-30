from tkinter import *
from tkinter import ttk


class errorWindow:
    def __init__(self, message):
        self.message = message
        self.window = Tk()
        self.window.title("Attention")

        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)

        self.frame1.pack()

        self.errorMessage = Label(self.frame1, text=self.message)
        self.okButton = Button(self.frame1, text='OK', command=self.okButtonPressed)

        self.errorMessage.grid(row=0, column=0)
        self.okButton.grid(row=1,column=0, padx=15)
        

    def okButtonPressed(self):
        self.window.destroy()
        print("Done")


