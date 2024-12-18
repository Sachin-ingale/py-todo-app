import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("300x500+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete (ANCHOR)




def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        

        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(END, task) 
    except FileNotFoundError:
        with open("tasklist.txt", "w") as file:
            pass

# icon
image_icon = PhotoImage(file="task.png")
root.iconphoto(False, image_icon)

# top bar
TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=20, y=15) 

noteImage = PhotoImage(file="task.png")
Label(root, image=noteImage, bg="#32405b").place(x=250, y=15)

heading = Label(root, text="ALL TASK", font="arial 16 bold", fg="white", bg="#32405b")
heading.place(x=100, y=10)

# main
frame = Frame(root, width=300, height=40, bg="white")
frame.place(x=0, y=130)

task = StringVar()
task_entry = Entry(frame, width=14, font="arial 16", bd=0)
task_entry.place(x=10, y=5)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 16 bold", width=5, bg="#5a95ff", fg="#fff", bd=0,command=addTask)
button.place(x=220, y=0)

# listbox
frame1 = Frame(root, bd=3, width=300, height=200, bg="#32405b")
frame1.pack(pady=(120, 0))
listbox = Listbox(frame1, font=('arial', 10), width=28, height=10, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff") 
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Call the function to load tasks from the file
openTaskFile()

# delete
Delete_icon = PhotoImage(file="delete.png")
Button(root, image=Delete_icon, bd=0,command=deleteTask).pack(side=BOTTOM, pady=10,)

name_label = Label(root, text="Developed by Sachin Ingale", bg="#fff", font="arial 10 italic")
name_label.pack(side=BOTTOM, pady=10)

root.mainloop()
