import ClockContainer
from tkinter import *

# function part


def show_world_time(event):
    screen.show_frame("WorldTime")


def show_home(event):
    screen.show_frame("Home")


def show_pomodoro(event):
    screen.show_frame("Pomodoro")


def show_to_do_list(event):
    screen.show_frame("ToDoList")


def refresh(event):
    global screen
    screen.destroy()
    # set up the screen
    screen = ClockContainer.Clock()
    screen.iconbitmap(".\\data\\icon.ico")
    screen.title("Pocket Clock")
    screen.resizable(False, False)
    screen.geometry("600x500+400+150")

    # change the <Control-h> to the keyboard shortcut you want, this keyboard shortcut will return to the home page (if you aren't using Windows)
    screen.bind("<Control-h>", show_home)
    # change the <Control-p> to the keyboard shortcut you want, this keyboard shortcut will return to the pomodoro page (if you aren't using Windows)
    screen.bind("<Control-P>", show_pomodoro)
    # if you like, you can change it
    screen.bind("<Shift-Tab>", show_to_do_list)
    screen.bind("<Control-w>", show_world_time)
    screen.bind("<Control-r>", refresh)
    screen.mainloop()


# set up the screen
screen = ClockContainer.Clock()
screen.iconbitmap(".\\data\\icon.ico")
screen.title("Pocket Clock")
screen.resizable(False, False)
screen.geometry("600x500+400+150")

# change the <Control-h> to the keyboard shortcut you want, this keyboard shortcut will return to the home page (if you aren't using Windows)
screen.bind("<Control-h>", show_home)
# change the <Control-p> to the keyboard shortcut you want, this keyboard shortcut will return to the pomodoro page (if you aren't using Windows)
screen.bind("<Control-P>", show_pomodoro)
screen.bind("<Shift-Tab>", show_to_do_list)  # if you like, you can change it
screen.bind("<Control-w>", show_world_time)
screen.bind("<Control-r>", refresh)
screen.mainloop()
