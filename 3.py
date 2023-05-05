import tkinter as tk

def calculate():
    n = int(entry_n.get())

    # Решаем рекуррентное соотношение для чисел Фибоначчи
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            result = a + b
            a, b = b, result

    # Выводим результат на экран
    result_label.config(text="Результат: {}".format(result))

# Создаем окно
window = tk.Tk()
window.iconbitmap('icon1.ico')
window.geometry('550x300')
window.title("Числа Фибоначчи")

# Создаем виджеты
text_name = tk.Label(window, text="Введите индекс числа Фибаначчи:",font = ("Comic Sans MS",20,'italic'))
label_n = tk.Label(window, text="n:",font = ("Comic Sans MS",16,'italic'))
entry_n = tk.Entry(window,width=70)
calculate_button = tk.Button(window,
             text = 'Решить',
             command = calculate,
             font = ("Calibri",20,'italic'),
             bg = 'green',
             activebackground='red',
             activeforeground= 'white')
result_label = tk.Label(window, text="Результат:",font = ("Calibri",20,'italic'),
             bg = 'lime')

# Устанавливаем изображение на кнопку calculate_button
img = tk.PhotoImage(file="knp1.gif")



# Размещаем виджеты на экране
text_name.grid(row = 0,column = 1)
label_n.grid(row=1, column=0)
entry_n.grid(row=1, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

# Запускаем главный цикл обработки событий
window.mainloop()
