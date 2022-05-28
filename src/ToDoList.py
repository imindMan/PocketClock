import tkinter as tk
from tkinter import messagebox
import time


class ToDoList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.listOfTodo = []
        self.content = ""

        self.closeToDo = False
        self.updateTime = None
        self.checkList = 0

        def count():

            new_list = [self.listOfTodo[i][1]
                        for i in range(len(self.listOfTodo) - 1)]
            time_now = time.strftime("%d-%b-%g %I:%M:%S %p")
            print(time_now)

            if time_now not in new_list:
                self.updateTime = controller.after(1, count)
            else:
                controller.after_cancel(self.updateTime)
                messagebox.showwarning("System", "To do call!")
                self.checkList += 1
                if self.checkList == len(self.listOfTodo) - 1:
                    return
                count()

        def callToDo():
            self.listOfTodo = []
            f = open(
                ".\\src\\todo.txt", "r")
            get = f.read().split("\n\n")

            for i in get:
                self.listOfTodo.append(i)
            f.close()
            for i in range(len(self.listOfTodo)):
                self.listOfTodo[i] = self.listOfTodo[i].split("\n")

            self.index = [
                [0, 0],
                [0, 1],
                [0, 2],
                [1, 0],
                [1, 1],
                [1, 2],
                [2, 0],
                [2, 1],
                [2, 2]
            ]
            for i in range(len(self.listOfTodo) - 1):
                print(self.listOfTodo[i][0],
                      self.index[i][0], self.index[i][1])
                bruh_lbl = tk.Label(todo_interface, width=22, height=9,
                                    relief="sunken", text=self.listOfTodo[i][0] + "\n" + self.listOfTodo[i][1])
                bruh_lbl.grid(
                    row=self.index[i][0], column=self.index[i][1])

            self.closeToDo = False

        def addTodo():
            def apply():

                todobox_name = self.todoname_entry.get()
                todobox_time = self.time_entry.get()

                f = open(
                    ".\\src\\todo.txt", "a")
                f.write(todobox_name + " \n" + todobox_time + "\n\n")
                f.close()
                print("Apply success!")
                todobox.destroy()
                self.closeToDo = True
            todobox = tk.Tk()
            todobox.geometry("400x140+500+200")
            todobox.title("Set the content of the to do list")
            todobox.iconbitmap(".\\data\\icon.ico")
            todobox.resizable(False, False)

            info_lbl = tk.Label(master=todobox, text="New to do list",
                                font=("Consolas", 18), fg="black",  width=20)
            info_lbl.grid(row=0, column=1, sticky="w")

            todoname_lbl = tk.Label(master=todobox, text="Name:", font=(
                "Consolas", 12), fg="black")
            todoname_lbl.grid(row=1, column=0, sticky="w")

            self.todoname_entry = tk.Entry(
                master=todobox, font=("Consolas", 12), width=40)
            self.todoname_entry.grid(row=1, column=1, sticky="w")

            time_end = tk.Label(master=todobox, font=("Consolas", 12),
                                text="Time end (e.g 01-Jan-22 23:00:00 AM): ")
            time_end.grid(row=2, column=0, columnspan=2, sticky="w")
            self.time_entry = tk.Entry(
                master=todobox, font=("Consolas", 12), width=50)
            self.time_entry.grid(row=3, column=0, columnspan=2, sticky="w")

            btn_submit = tk.Button(master=todobox, text="Apply", font=(
                "Consolas", 12), command=apply)
            btn_submit.grid(row=4, column=1)
            if self.closeToDo:
                callToDo()

        # status
        status = tk.Frame(master=self, width=123, bg="black")
        status.pack(fill=tk.Y, side=tk.LEFT)
        # countdown status
        countdown_label = tk.Button(
            master=status, text="Countdown", font=("Consolas", 16), bg="black", fg="white", command=lambda: controller.show_frame("Countdown"))
        countdown_label.place(x=0, y=0)
        # finish status
        finish_button = tk.Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, border=0, command=lambda: controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)
        # stopwatch status
        stopwatch_button = tk.Button(master=status, text="Stopwatch", font=(
            "Consolas", 16), bg="black", fg="white", border=0, width=10, height=0, command=lambda: controller.show_frame("Stopwatch"))
        stopwatch_button.place(x=-1, y=75)
        todo_label = tk.Button(master=status, text="ToDoList", font=(
            "Consolas", 16), bg="white", fg="black", border=0, width=10, height=0)
        todo_label.place(x=0, y=109)

        # limit: 9

        interface = tk.Label(self, width=477, height=500, bg="white")
        interface.place(x=123, y=0)
        add_todo_btn = tk.Button(master=interface, text="+", font=("Consolas", 16),
                                 bg="white", fg="black", border=0, width=10, height=0, command=addTodo)
        add_todo_btn.place(x=400, y=460)
        todo_interface = tk.Label(self, width=477, height=30, bg="white")
        todo_interface.place(x=123, y=0)

        # for i in range(3):
        #     for j in range(3):
        #         print(i, j)
        #         bruh_lbl = Label(todo_interface, width=22,
        #                          height=9, relief="sunken", text="Bruh")
        #         bruh_lbl.grid(row=i, column=j)
        callToDo()
        if len(self.listOfTodo) == 1:
            pass
        else:
            count_btn = tk.Button(master=interface, text="Count!", font=(
                "Consolas", 16), bg="white", fg="black", border=0, width=0, height=0, command=count)
            count_btn.place(x=350, y=460)
