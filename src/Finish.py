import time
import tkinter as tk
from tkinter import messagebox


class Finish(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # status
        self.update_time = None

        def print_time():
            time_access = f"{day_of_week.get()} {day_of_month.get()}-{month.get()}-{year.get()} {time_entry.get()}"
            time_now = time.strftime("%a %d-%b-%G %I:%M:%S %p")
            if time_access != time_now:
                self.update_time = controller.after(1, print_time)
            else:
                controller.after_cancel(self.update_time)
                messagebox.showwarning("System", "Work's end!")

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
        interface = tk.Frame(self,  bg="white", width=controller.width - 123)
        interface.pack(side=tk.RIGHT, fill=tk.Y)

        info_label = tk.Label(interface, bg="white", fg="black",
                              text="Select the full end-work time", font=("Consolas", 15))
        info_label.place(x=40, y=60)
        options_day_of_week = [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]
        options_month = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
        ]
        options_year = [
            i for i in range(2022, 2041)
        ]
        day_of_week = tk.StringVar(value="Mon")
        day_of_month = tk.StringVar(value="1")
        month = tk.StringVar(value="Jan")
        year = tk.StringVar(value="2022")
        day_of_week_menu = tk.OptionMenu(
            interface, day_of_week, *options_day_of_week)
        day_of_week_menu.config(width=2)
        day_of_week_menu.place(x=40, y=90)
        day_of_month_menu = tk.OptionMenu(
            interface, day_of_month, *[i for i in range(1, 32)])
        day_of_month_menu.config(width=1)
        day_of_month_menu.place(x=90, y=90)
        month_menu = tk.OptionMenu(interface, month, *options_month)
        month_menu.config(width=2)
        month_menu.place(x=133, y=90)
        year_menu = tk.OptionMenu(interface, year, *options_year)
        year_menu.config(width=2)
        year_menu.place(x=173, y=90)

        time_entry = tk.Entry(
            interface, textvariable=tk.StringVar(value="00:00:00 AM"), font=("Consolas", 17), width=12)
        time_entry.place(x=234, y=90)
        accept_button = tk.Button(
            interface, text="Count!", font=("Consolas", 20), command=print_time)
        accept_button.place(x=140, y=200)
