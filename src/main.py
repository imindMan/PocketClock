import ClockContainer
from tkinter import *

# function part


def show_home(event):
    screen.show_frame("Home")


def show_pomodoro(event):
    screen.show_frame("Pomodoro")


# set up the screen
screen = ClockContainer.Clock()
icon = PhotoImage(
    file="H:\\K.DONG\\My book\\Learn to code\\Pocket Clock\\data\\icon.png")
screen.iconphoto(False, icon)
screen.title("Pocket Clock")
screen.resizable(False, False)
screen.geometry("600x500+400+150")

screen.bind("<Control-h>", show_home)
screen.bind("<Control-P>", show_pomodoro)
screen.mainloop()
