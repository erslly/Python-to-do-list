import tkinter as tk
from tkinter import messagebox

TASKS_FILE = "tasks.txt"

def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file: 
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:  
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        save_tasks()
    else:
        messagebox.showwarning("Uyarı", "Lütfen silmek için bir görev seçin!")

def delete_all_tasks():
    task_listbox.delete(0, tk.END)
    save_tasks()

def mark_task_complete():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} ✓")
        save_tasks()
    else:
        messagebox.showwarning("Uyarı", "Lütfen tamamlanmış olarak işaretlemek için bir görev seçin!")

root = tk.Tk()
root.title("Yapılacaklar Listesi")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Görev Ekle", width=15, font=("Helvetica", 12), command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=45, height=15, font=("Helvetica", 12))
task_listbox.pack(pady=20)

delete_button = tk.Button(root, text="Görev Sil", width=15, font=("Helvetica", 12), command=delete_task)
delete_button.pack(pady=5)

delete_all_button = tk.Button(root, text="Tümünü Sil", width=15, font=("Helvetica", 12), command=delete_all_tasks)
delete_all_button.pack(pady=5)

complete_button = tk.Button(root, text="Tamamlandı", width=15, font=("Helvetica", 12), command=mark_task_complete)
complete_button.pack(pady=5)

load_tasks()

root.mainloop()