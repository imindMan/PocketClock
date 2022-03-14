import tkinter as tk
from tkinter import messagebox

# Countdown page


class Countdown(tk.Frame):
    def __init__(self, parent, controller: tk.Tk):

        tk.Frame.__init__(self, parent)
        # some important variable
        self.running = False
        self.hour, self.minute, self.second = 0, 0, 0

        self.time_countdown = tk.StringVar(value="00:00:00")
        # functions

        def start():
            if not self.running:
                count_time()
                self.running = True

        def stop():
            if self.running:
                entry_time.after_cancel(update_time)
                self.running = False

        def count_time():
            total_time = list(map(int, self.time_countdown.get().split(":")))
            total_sec = total_time[0] * 3600 + \
                total_time[1] * 60 + total_time[2]
            if total_sec == 0:
                messagebox.showwarning("System", "Time's up!")
                stop()
            else:
                total_sec -= 1
                hour = int(total_sec / 3600)
                minute = int((total_sec % 3600) / 60)
                second = (total_sec % 3600) % 60
                time = "%s:%s:%s" % (str(hour).zfill(2), str(
                    minute).zfill(2), str(second).zfill(2))
                self.time_countdown.set(time)
                entry_time["textvariable"] = self.time_countdown
                global update_time
                update_time = entry_time.after(1000, count_time)

        status = tk.Frame(master=self, width=123, bg="black")
        status.pack(fill=tk.Y, side=tk.LEFT)
        # countdown status
        countdown_label = tk.Label(
            master=status, text="Countdown", font=("Consolas", 18), bg="white", fg="black")
        countdown_label.place(x=0, y=0)
        # finish status
        finish_button = tk.Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, border=0, command=lambda: controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)
        # stopwatch status
        stopwatch_button = tk.Button(master=status, text="Stopwatch", font=(
            "Consolas", 16), bg="black", fg="white", border=0, width=10, height=0, command=lambda: controller.show_frame("Stopwatch"))
        stopwatch_button.place(x=-1, y=75)

        # main section

        interface = tk.Label(self, width=477, height=500, bg="white")
        interface.place(x=123, y=0)

        entry_time = tk.Entry(interface, textvariable=self.time_countdown,
                              font=("Consolas", 30), width=8)
        entry_time.place(x=145, y=60)

        start_button = tk.Button(
            interface, text="Start", font=("Consolas", 20), command=start)
        start_button.place(x=100, y=200)

        stop_button = tk.Button(
            interface, text="Stop", font=("Consolas", 20), command=stop)
        stop_button.place(x=270, y=200)
