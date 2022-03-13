import tkinter as tk
import datetime


class Finish(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # status
        status = tk.Frame(master=self, width=123, height=500, bg="black")
        status.pack(fill=tk.Y, side=tk.LEFT)

        countdown_label = tk.Button(
            master=status, text="Countdown", font=("Consolas", 16), bg="black", fg="white", command=lambda: controller.show_frame("Countdown"), border=0)
        countdown_label.place(x=0, y=0)

        finish_button = tk.Label(master=status, text="Finish", font=(
            "Consolas", 18), bg="white", fg="black", height=0, width=10)
        finish_button.place(x=-1, y=34)

        stopwatch_button = tk.Button(master=status, text="Stopwatch", font=(
            "Consolas", 16), bg="black", fg="white", border=0, width=10, height=0, command=lambda: controller.show_frame("Stopwatch"))
        stopwatch_button.place(x=0, y=75)
        # main
        interface = tk.Frame(self,  bg="black", width=controller.width - 123)
        interface.pack(side=tk.RIGHT, fill=tk.Y)
