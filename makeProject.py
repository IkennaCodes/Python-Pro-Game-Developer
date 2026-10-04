# tkinter is a graphical library of python
from tkinter import *

# creating the window of the app
window = Tk()

# define the size of the window
window.geometry("800x600")

# give a title of the app
window.title("Make your PROJECT!")

# give colour to the window
window.config(background = "#848484")

# creates and displays the heading on the screen
heading = Label(window, text = "Make your PROJECT!", font = ("Lexend", 30, "bold"), background = "#848484", fg = "white")
heading.place(x = 120, y = 50)

# creates and displays the name label on the screen
name = Label(window, text = "Name your project:", font = ("Arial", 15), background = "#848484", fg = "white")
name.place(x = 50, y = 130)

# create an entry box for name
nameEntry = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
nameEntry.place(x = 220, y = 133)

# creates and displays the age label on the screen
age = Label(window, text = "Pick a template:", font = ("Arial", 15), background = "#848484", fg = "white")
age.place(x = 50, y = 180)

# create an entry box for age
ageEntry = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
ageEntry.place(x = 200, y = 183)


submitButton = Button(window, text = "Create Project", command = window.destroy)
submitButton.place(x = 400, y = 300)

# ensures it stays on screen
window.mainloop()