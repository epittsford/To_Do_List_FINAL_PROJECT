import tkinter as tk
from tkinter import messagebox




class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        # Create Frames
        self.top_frame = tk.Frame(master)
        self.mid_frame = tk.Frame(master)
        self.bot_frame = tk.Frame(master)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        # Create Widgets
        self.title_label = tk.Label(self.top_frame, text="To-Do List", font=("Helvetica", 20))
        self.title_label.pack()

        self.task_label = tk.Label(self.mid_frame, text="Task:")
        self.task_entry = tk.Entry(self.mid_frame)
        self.task_label.pack(side="left")
        self.task_entry.pack(side="left")

        self.add_button = tk.Button(self.mid_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left")

        self.complete_button = tk.Button(self.mid_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side="left")

        self.clear_button = tk.Button(self.mid_frame, text="Clear List", command=self.clear_list)
        self.clear_button.pack(side="left")

        self.save_button = tk.Button(self.mid_frame, text="Save List", command=self.save_list)
        self.save_button.pack(side="left")

        self.load_button = tk.Button(self.mid_frame, text="Load List", command=self.load_list)
        self.load_button.pack(side="left")

        self.exit_button = tk.Button(self.bot_frame, text="Exit", command=master.quit)
        self.exit_button.pack()

        self.task_listbox = tk.Listbox(self.bot_frame, width=50)
        self.task_listbox.pack()

        self.refresh_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if not task:
            tk.messagebox.showerror("Error", "Please enter a task.")
            return
        self.tasks.append(task)
        self.task_entry.delete(0, "end")
        self.refresh_listbox()

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            task = self.task_listbox.get(selection)
            self.tasks.remove(task)
            self.refresh_listbox()

    def clear_list(self):
        self.tasks = []
        self.refresh_listbox()

    def save_list(self):
        with open("todolist.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_list(self):
        try:
            with open("todolist.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.refresh_listbox()
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No saved list found.")

    def refresh_listbox(self):
        self.task_listbox.delete(0, "end")
        for task in self.tasks:
            self.task_listbox.insert("end", task)


root = tk.Tk()
app = TodoList(root)
root.mainloop()