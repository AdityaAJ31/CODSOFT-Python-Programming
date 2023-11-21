from tkinter import *
from tkinter import messagebox, simpledialog

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()

def edit_task(event):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        current_task = tasks[selected_task_index[0]]
        edited_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=current_task)
        if edited_task:
            tasks[selected_task_index[0]] = edited_task
            update_task_list()

def update_task_list():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

gui = Tk()
gui.title("To-Do List (CODSOFT TASK - 1)")

entry = Entry(gui, width=40)
entry.pack(pady=10)

add_button = Button(gui, text="Add Task", command=add_task)
add_button.pack()

task_listbox = Listbox(gui, width=40, selectmode=SINGLE)
task_listbox.pack(pady=10)

delete_button = Button(gui, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox.bind("<Double-Button-1>", edit_task)

gui.mainloop()