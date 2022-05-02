import tkinter as tk 
class ToDoList(tk.Frame):
    def __init__(self, parent, controller):
        self.listOfTodo = []
        def addToDo(self, content):
            pass

        tk.Frame.__init__(self, parent)
        # status
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
        todo_label = tk.Button(master=status, text="ToDoList", font=("Consolas", 16), bg="white", fg="black", border=0, width=10, height=0)
        todo_label.place(x=0, y=109)
        
        # limit: 9

        interface = tk.Label(self, width=477, height=500, bg="white")
        interface.place(x=123, y=0)
        add_todo_btn = tk.Button(master=interface, text="+", font=("Consolas", 16), bg="white", fg="black", border=0, width=10, height=0)
        add_todo_btn.place(x=400, y=460)


