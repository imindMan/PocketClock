import tkinter as tk


class Stopwatch(tk.Frame):

    def __init__(self, parent, controller: tk.Tk):

        tk.Frame.__init__(self, parent)
        self.running = False
        self.totalSec = 0
        # functions

        def start():
            if not self.running:
                countTime()
                self.running = True

        def stop():
            if self.running:
                lbl_time.after_cancel(update)
                self.running = False

        def reset():
            if self.running:
                lbl_time.after_cancel(update)
                self.running = False
            self.totalSec = 0
            lbl_time.config(text="00:00:00")

        def countTime():
            self.totalSec += 1
            hour = int(self.totalSec / 3600)
            minute = int((self.totalSec % 3600) / 60)
            second = (self.totalSec % 3600) % 60
            time = "%s:%s:%s" % (str(hour).zfill(2), str(
                minute).zfill(2), str(second).zfill(2))
            lbl_time.config(text=time)
            global update
            update = lbl_time.after(1000, countTime)
        # the status
        status = tk.Frame(master=self, width=123, height=500, bg="black")
        status.pack(side=tk.LEFT, fill=tk.Y)

        countdown_button = tk.Button(
            master=status, text="Countdown", font=("Consolas", 16), bg="black", fg="white", border=0, command=lambda: controller.show_frame("Countdown"))
        countdown_button.place(x=0, y=0)

        finish_button = tk.Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, border=0, command=lambda: controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)

        stopwatch_label = tk.Label(master=status, text="Stopwatch", font=(
            "Consolas", 18), bg="white", fg="black", border=0, width=10, height=0)
        stopwatch_label.place(x=-1, y=75)
        # main section
        interface = tk.Frame(self,  bg="white", width=controller.width - 123)
        interface.pack(side=tk.RIGHT, fill=tk.Y)
        lbl_time = tk.Label(interface, text="00:00:00",
                            font=("Consolas", 30), width=8, bg="white")
        lbl_time.place(x=145, y=60)

        start_button = tk.Button(
            interface, text="Start", font=("Consolas", 20), command=start)
        start_button.place(x=90, y=200)

        stop_button = tk.Button(interface, text="Stop",
                                font=("Consolas", 20), command=stop)
        stop_button.place(x=200, y=200)

        reset_button = tk.Button(
            interface, text="Reset", font=("Consolas", 20), command=reset)
        reset_button.place(x=300, y=200)
