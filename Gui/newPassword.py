from tkinter import *
from tkinter import ttk

class changePasswordWindow:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("Change Password")

        #Create frame
        frame1 = LabelFrame(self.window, text="", padx=20, pady=20)
        frame1.pack()

        #Create labels/text areas and buttons and put on screen
        oldPasswordLabel = Label(frame1, text="Old Password:").grid(row=0, column=0)
        newPasswordLabel = Label(frame1, text="New Password").grid(row=1, column=0)
        oldPasswordTextBox = Entry(frame1).grid(row=0, column=1)
        newPasswordTextBox = Entry(frame1).grid(row=1, column=1)
        saveButton = Button(frame1, text="Save").grid(row=2, column=0)
        cancelButton = Button(frame1, text="Cancel").grid(row=2, column=1)

        def saveButtonPressed():
            print("Saved")

        def cancelButtonPressed():
            print("canceled")