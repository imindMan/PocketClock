import time
import tkinter as tk


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def updateTime():
            time_now = time.strftime("%a %d-%b-%g %H:%M:%S %p")
            time_label.config(text=time_now)
            time_label.after(1, updateTime)
            # status
        status_frm = tk.Frame(self, bg="black", width=600, height=50)
        status_frm.place(x=0, y=0)

        Countdown_btn = tk.Button(
            status_frm, text="Countdown", font=("Consolas", 20), bg="black", fg="white", command=lambda: controller.show_frame("Countdown"), border=0)
        Countdown_btn.place(x=95, y=0)
        Finish_btn = tk.Button(
            status_frm, text="Finish", font=("Consolas", 20), bg="black", fg="white", command=lambda: controller.show_frame("Finish"), border=0)
        Finish_btn.place(x=250, y=0)

        Stopwatch_btn = tk.Button(
            status_frm, text="Stopwatch", font=("Consolas", 20), bg="black", fg="white", command=lambda: controller.show_frame("Stopwatch"), border=0)
        Stopwatch_btn.place(x=360, y=0)

        # main text

        main_text_label = tk.Label(
            self, text="Welcome Home", font=("Consolas", 40))
        main_text_label.place(x=136, y=200)
        time_label = tk.Label(self, font=("Consolas", 11))
        time_label.place(x=380, y=400)
        updateTime()
