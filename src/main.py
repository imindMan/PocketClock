import ClockContainer
from tkinter import *


def show_home(event):
    screen.show_frame("Home")


screen = ClockContainer.Clock()
icon = PhotoImage(file=".\\data\\icon.png")
screen.iconphoto(False, icon)
screen.title("Pocket Clock")
screen.resizable(False, False)
screen.geometry("600x500+400+150")

screen.bind("<Control-h>", show_home)
screen.mainloop()
