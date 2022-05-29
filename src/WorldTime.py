import tkinter as tk
from datetime import datetime
import pytz


class WorldTime(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def show_time():
            list_of_regions = pytz.all_timezones
            if region_entry.get() not in list_of_regions:
                return

            UTC = pytz.utc
            time = pytz.timezone(region_entry.get())
            date = datetime.now(time)
            utc = date.astimezone(UTC)
            text_display = region_entry.get() + \
                " is " + utc.strftime("%d-%b-%G %I:%M:%S %p")
            display_lbl = tk.Label(
                interface, bg="white", fg="black", text=text_display, font=("Consolas", 16))
            display_lbl.place(x=19, y=100)
            self.update()
        status = tk.Frame(master=self, width=123, height=500, bg="black")
        status.pack(fill=tk.Y, side=tk.LEFT)
        countdown_button = tk.Button(
            master=status, text="Countdown", font=("Consolas", 16), bg="black", fg="white", command=lambda: controller.show_frame("Countdown"), border=0)
        countdown_button.place(x=0, y=0)

        finish_button = tk.Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, command=lambda: controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)

        stopwatch_button = tk.Button(master=status, text="Stopwatch", font=(
            "Consolas", 16), bg="black", fg="white", border=0, width=10, height=0, command=lambda: controller.show_frame("Stopwatch"))
        stopwatch_button.place(x=0, y=75)
        WorldTime_label = tk.Button(master=status, text="WorldTime", font=(
            "Consolas", 16), bg="white", fg="black", border=0, width=10, height=0)
        WorldTime_label.place(x=0, y=109)

        interface = tk.Frame(self,  bg="white", width=controller.width - 123)
        interface.pack(side=tk.RIGHT, fill=tk.Y)

        choose_lbl = tk.Label(interface, bg="white", fg="black",
                              text="Choose the region: ", font=("Consolas", 16))
        choose_lbl.place(x=19, y=19)

        # year_menu = tk.OptionMenu(interface, year, *options_year)
        # year_menu.config(width=2)
        # year_menu.place(x=173, y=90)

        region_entry = tk.Entry(interface, font=("Consolas", 16))
        region_entry.place(x=19, y=50)

        submit_button = tk.Button(interface, text="Submit!", font=(
            "Consolas", 16), command=show_time)
        submit_button.place(x=140, y=200)
