import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    # Отримуємо введене значення з поля введення
    input_value = entry.get()

    try:
        # Перетворюємо введене значення в число
        input_value = float(input_value)

        # Перевірка на введення нуля або від'ємного числа
        if input_value <= 0:
            raise ValueError("Введено від'ємне число або нуль")

        # Обчислення квадратного кореня
        result = math.sqrt(input_value)

        # Оновлення відображення результату
        result_label.config(text=f"Квадратний корінь: {result}")
    except ValueError as e:
        # Вивід повідомлення про помилку
        messagebox.showerror("Помилка", str(e))

def on_closing():
    if messagebox.askokcancel("Вихід", "Ви впевнені, що хочете вийти?"):
        root.destroy()

# Створення головного вікна
root = tk.Tk()
root.title("Програма обчислення виразу")
root.geometry("400x150")

# Створення фрейму для елементів управління
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Створення елементів управління для обчислення квадратного кореня
label1 = tk.Label(control_frame, text="Розрахувати значення x", font=("Arial", 10))
label1.grid(row=0, column=0, padx=10)

entry = tk.Entry(control_frame, width=10)
entry.grid(row=0, column=1, padx=10)

button1 = tk.Button(control_frame, text="Обчислити", command=calculate)
button1.grid(row=0, column=2, padx=10)

# Створення фрейму для результатів
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

label2 = tk.Label(result_frame, text="Результат", font=("Arial", 10))
label2.grid(row=0, column=0, padx=10)

result_label = tk.Label(result_frame, text="", font=("Arial", 10))
result_label.grid(row=0, column=1, padx=10)

# Додавання деструктора
root.protocol("WM_DELETE_WINDOW", on_closing)

# Запуск головного циклу програми
root.mainloop()
