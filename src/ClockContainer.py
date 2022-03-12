import tkinter as tk
import Countdown
import Stopwatch
import Finish
import Home

# The container to hold all of the page in application


class Clock(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        # loop to make a dictionary of pages
        for f in (Home.Home, Countdown.Countdown, Stopwatch.Stopwatch, Finish.Finish):
            name = str(f.__name__)
            frame = f(container, self)

            self.frames[name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        # default frame
        self.show_frame("Home")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
