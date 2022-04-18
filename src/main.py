import ClockContainer
from tkinter import *

# function part


def show_home(event):
    screen.show_frame("Home")


def show_pomodoro(event):
    screen.show_frame("Pomodoro")

def show_to_do_list(event):
    screen.show_frame("ToDoList")

# set up the screen
screen = ClockContainer.Clock()
icon = PhotoImage(
    file="H:\\K.DONG\\My book\\Learn to code\\Pocket Clock\\data\\icon.png")  # change this path to your path to the icon.png
screen.iconphoto(False, icon)
screen.title("Pocket Clock")
screen.resizable(False, False)
screen.geometry("600x500+400+150")

# change the <Control-h> to the keyboard shortcut you want, this keyboard shortcut will return to the home page (if you aren't using Windows)
screen.bind("<Control-h>", show_home)
# change the <Control-p> to the keyboard shortcut you want, this keyboard shortcut will return to the pomodoro page (if you aren't using Windows)
screen.bind("<Control-P>", show_pomodoro)
screen.bind("<Shift-Tab>", show_to_do_list)
screen.mainloop()
