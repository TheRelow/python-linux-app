import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Привет", "Добро пожаловать в моё первое приложение с графическим интерфейсом!")

def change_label_text():
    label.config(text="Текст метки изменён!")

def clear_label_text():
    label.config(text="")

def submit():
    input_text = entry.get()
    if input_text:
        messagebox.showinfo("Введённый текст", f"Вы ввели: {input_text}")
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, введите текст!")

root = tk.Tk()
root.title("Моё первое приложение")

label = tk.Label(root, text="Нажмите кнопку для приветствия", padx=20, pady=20)
label.pack()

button_hello = tk.Button(root, text="Приветствие", command=show_message)
button_hello.pack()

button_change_text = tk.Button(root, text="Изменить текст метки", command=change_label_text)
button_change_text.pack()

button_clear_text = tk.Button(root, text="Очистить текст метки", command=clear_label_text)
button_clear_text.pack()

entry = tk.Entry(root)
entry.pack()

button_submit = tk.Button(root, text="Отправить", command=submit)
button_submit.pack()

root.mainloop()