import tkinter as tk


class Stopwatch(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        # the status
        status = tk.Frame(master=self, width=123, height=500, bg="black")
        status.pack(side=tk.LEFT, fill=tk.Y)

        countdown_label = tk.Button(
            master=status, text="Countdown", font=("Consolas", 16), bg="black", fg="white", border=0, command=lambda: controller.show_frame("Countdown"))
        countdown_label.place(x=0, y=0)

        finish_button = tk.Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, border=0, command=lambda: controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)

        stopwatch_button = tk.Label(master=status, text="Stopwatch", font=(
            "Consolas", 18), bg="white", fg="black", border=0, width=10, height=0)
        stopwatch_button.place(x=-1, y=75)
        # main section
        interface = tk.Frame(self,  bg="white", width=controller.width - 123)
        interface.pack(side=tk.RIGHT, fill=tk.Y)
