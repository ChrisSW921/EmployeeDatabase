from tkinter import *
from tkinter import ttk

class usePTOWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Use PTO")

        #Create frame
        frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        frame1.pack()

        #Create labels/text areas and buttons and put on screen
        titleLabel = Label(frame1, text="Use PTO")
        hoursLabel = Label(frame1, text="Hours:")
        inputTextBox = Entry(frame1)
        saveButton = Button(frame1, text="Save")
        cancelButton = Button(frame1, text="Cancel", command=self.cancelButtonPressed)

        titleLabel.grid(row=0, column=1)
        hoursLabel.grid(row=1, column=0)
        inputTextBox.grid(row=1, column=1)
        saveButton.grid(row=2, column=0)
        cancelButton.grid(row=2, column=1)

    def saveButtonPressed(self):
        print("Saved")

    def cancelButtonPressed(self):
        self.window.destroy()
        print("canceled")