import tkinter as tk

class Pomodoro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        status = tk.Frame(master=self, width=123, height=500, bg="black")
        status.pack(fill=tk.Y, side=tk.LEFT)
        
        self.time_break = False
        self.main = False
        self.stop = False
        self.totalSec = 0

        def start():
            if self.main == False and self.time_break == False and self.stop == False:
                self.main = True
            elif self.main == False and self.time_break == True and self.stop == True:
                self.time_break = False
                self.main = True
                self.stop = False
            elif self.main == True and self.time_break == False and self.stop == True:
                self.main = False
                self.time_break = True
                self.stop = False
            print("Main: ",self.main, "Time break: ",self.time_break, "Stop: ",self.stop)
            count_pomodoro()
        def stop():
            if self.main == True and self.time_break == False and self.stop == False:
                self.stop = True
                self.time_break = True
                self.main = False
            elif self.main == False and self.time_break == True and self.stop == False:
                self.stop = True
                self.time_break = False
                self.main = True
            time_label.after_cancel(update)

            print("Main: ",self.main, "Time break: ",self.time_break, "Stop: ",self.stop)
        def count_pomodoro(): 
            if self.totalSec < 20 and self.main == True and self.time_break == False and self.stop == False:
                self.totalSec += 1
                print(self.totalSec)
                time = "00:00:%s" %(str(self.totalSec).zfill(2))
                time_label.config(text=time)
            elif self.totalSec == 20 and self.main == True and self.time_break == False and self.stop == False:
                self.totalSec = 0
                self.main = False
                self.time_break = True
                print(self.totalSec)
                time = "00:00:%s" %(str(self.totalSec).zfill(2))
                time_label.config(text=time)
            elif self.totalSec < 10 and self.main == False and self.time_break == True and self.stop == False:
                self.totalSec += 1
                print(self.totalSec)
                time = "00:00:%s" %(str(self.totalSec).zfill(2))
                time_label.config(text=time)
            elif self.totalSec == 10 and self.main == False and self.time_break == True and self.stop == False:
                self.main = True
                self.time_break = False
                self.totalSec = 0
                print(self.totalSec)
                time = "00:00:%s" %(str(self.totalSec).zfill(2))
                time_label.config(text=time)
            global update
            update = time_label.after(1000, count_pomodoro)

        countdown_button = tk.Button(
            master=status, text="Countdown", font=("Consolas", 16), bg="black", fg="white", command=lambda: controller.show_frame("Countdown"), border=0)
        countdown_button.place(x=0, y=0)

        finish_button = tk.Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, command = lambda : controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)

        stopwatch_button = tk.Button(master=status, text="Stopwatch", font=(
            "Consolas", 16), bg="black", fg="white", border=0, width=10, height=0, command=lambda: controller.show_frame("Stopwatch"))
        stopwatch_button.place(x=0, y=75)
        pomodoro_label = tk.Button(master=status, text="Pomodoro", font=("Consolas", 16), bg="white", fg="black", border=0, width=10, height=0)
        pomodoro_label.place(x=0, y=109)
        # main part
        interface = tk.Frame(self,  bg="white", width=controller.width - 123)
        interface.pack(side=tk.RIGHT, fill=tk.Y)

        time = "00:00:00"
        time_label = tk.Label(interface, bg="white", fg="black", text=time, font=('Consolas', 30))
        time_label.place(x=145, y=60)
        
        start_button = tk.Button(
                interface, text="Start", font=("Consolas", 20), command=start)
        start_button.place(x=100, y=200)

        stop_button = tk.Button(
            interface, text="Stop", font=("Consolas", 20), command=stop)
        stop_button.place(x=270, y=200) 
