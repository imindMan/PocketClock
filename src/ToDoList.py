from tkinter import *
class ToDoList(Frame):
    def __init__(self, parent, controller):
        self.listOfTodo = []
        self.content = ""
        def launchFirst():
            window_launch = Tk()
            window_launch.geometry("600x500+400+150")
            window_launch.title("Set the content of the to do list")
            window_launch.resizable(False, False)
            icon = PhotoImage(
    file="H:\\K.DONG\\My book\\Learn to code\\Pocket Clock\\data\\icon.png")  # change this path to your path to the icon.png
            window_launch.iconphoto(False, icon)
            
        Frame.__init__(self, parent)
        # status
        status = Frame(master=self, width=123, bg="black")
        status.pack(fill=Y, side=LEFT)
        # countdown status
        countdown_label = Label(
            master=status, text="Countdown", font=("Consolas", 18), bg="white", fg="black")
        countdown_label.place(x=0, y=0)
        # finish status
        finish_button = Button(master=status, text="Finish", font=(
            "Consolas", 18), bg="black", fg="white", height=0, width=10, border=0, command=lambda: controller.show_frame("Finish"))
        finish_button.place(x=-1, y=34)
        # stopwatch status
        stopwatch_button = Button(master=status, text="Stopwatch", font=(
            "Consolas", 16), bg="black", fg="white", border=0, width=10, height=0, command=lambda: controller.show_frame("Stopwatch"))
        stopwatch_button.place(x=-1, y=75)
        todo_label = Button(master=status, text="ToDoList", font=("Consolas", 16), bg="white", fg="black", border=0, width=10, height=0)
        todo_label.place(x=0, y=109)
        
        # limit: 9

        interface = Label(self, width=477, height=500, bg="white")
        interface.place(x=123, y=0)
        add_todo_btn = Button(master=interface, text="+", font=("Consolas", 16), bg="white", fg="black", border=0, width=10, height=0, command=launchFirst)
        add_todo_btn.place(x=400, y=460)
        
