import tkinter as tk
from tkinter import messagebox
import json

class ToDoListApp:
    def __init__(self):
        self.tasks = []

        self.root = tk.Tk()
        self.root.title("To-Do List App")

        self.task_title_label = tk.Label(self.root, text="Task Title:")
        self.task_title_label.pack()

        self.task_title_entry = tk.Entry(self.root)
        self.task_title_entry.pack()

        self.task_description_label = tk.Label(self.root, text="Task Description:")
        self.task_description_label.pack()

        self.task_description_entry = tk.Entry(self.root)
        self.task_description_entry.pack()

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack()

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.view_task_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.view_task_button.pack()

        self.save_tasks_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_button.pack()

        self.load_tasks_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_tasks_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

    def add_task(self):
        title = self.task_title_entry.get()
        description = self.task_description_entry.get()

        if title and description:
            self.tasks.append((title, description))
            self.task_listbox.insert(tk.END, f"{title} - {description}")
            self.task_title_entry.delete(0, tk.END)
            self.task_description_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a title and description for the task!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()

        if selected_index:
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected task?")
            if confirmed:
                self.task_listbox.delete(selected_index)
                del self.tasks[selected_index[0]]
        else:
            messagebox.showerror("Error", "Please select a task to delete!")

    def view_tasks(self):
        if self.tasks:
            messagebox.showinfo("Tasks", "\n".join([f"{title} - {description}" for title, description in self.tasks]))
        else:
            messagebox.showinfo("Tasks", "No tasks found!")

    def save_tasks(self):
        if self.tasks:
            filename = tk.filedialog.asksaveasfilename(defaultextension="to do list", filetypes=[("JSON Files", "*.json5")])
            if filename:
                try:
                    with open(filename, 'w') as file:
                        json.dump(self.tasks, file)
                    messagebox.showinfo("Save Tasks", "Tasks saved successfully!")
                except IOError:
                    messagebox.showerror("Save Tasks", "Error saving tasks to file!")
        else:
            messagebox.showwarning("Save Tasks", "No tasks to save!")

    def load_tasks(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            try:
                with open(filename, 'r') as file:
                    self.tasks = json.load(file)
                self.task_listbox.delete(0, tk.END)
                for title, description in self.tasks:
                    self.task_listbox.insert(tk.END, f"{title} - {description}")
                messagebox.showinfo("Load Tasks", "Tasks loaded successfully!")
            except IOError:
                messagebox.showerror("Load Tasks", "Error loading tasks from file!")
            except json.decoder.JSONDecodeError:
                messagebox.showerror("Load Tasks", "Invalid file format!")
        else:
            messagebox.showwarning("Load Tasks", "No file selected!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
