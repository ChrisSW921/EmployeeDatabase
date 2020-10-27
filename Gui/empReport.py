from tkinter import *
from tkinter import ttk

class empReporting:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Employee Report")

        #Create frame
        self.frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        self.frame1.pack()

        #Create labels/text areas and buttons and put on screen
        self.titleLabel = Label(self.frame1, text="")
        self.hoursLabel = Label(self.frame1, text="Include Archived Emps ->", padx=20, pady=20)

        self.archived = IntVar()

        self.archivedBox = Checkbutton(self.frame1, text="", variable=self.archived, state='normal', padx=20, pady=20) 
        self.generateButton = Button(self.frame1, text="Generate")
        self.cancelButton = Button(self.frame1, text="Cancel", command=self.cancelButtonPressed)

        self.titleLabel.grid(row=0, column=1)
        self.hoursLabel.grid(row=1, column=0)
        self.archivedBox.grid(row=1, column=1)
        self.generateButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        