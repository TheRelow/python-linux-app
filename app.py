import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

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

# Создаем объект шрифта Montserrat
montserrat_font = Font(family="Montserrat", size=12)

label = tk.Label(root, text="Нажмите кнопку для приветствия", padx=20, pady=20, font=montserrat_font)
label.pack()

button_hello = tk.Button(root, text="Приветствие", command=show_message, font=montserrat_font)
button_hello.pack()

button_change_text = tk.Button(root, text="Изменить текст метки", command=change_label_text, font=montserrat_font)
button_change_text.pack()

button_clear_text = tk.Button(root, text="Очистить текст метки", command=clear_label_text, font=montserrat_font)
button_clear_text.pack()

entry = tk.Entry(root, font=montserrat_font)
entry.pack()

button_submit = tk.Button(root, text="Отправить", command=submit, font=montserrat_font)
button_submit.pack()

root.mainloop()