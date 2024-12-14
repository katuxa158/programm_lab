import tkinter.font
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from random import randint
import os

root = tk.Tk()  # создание основного окна
root.title("Меню")  # заголовок окна
root.geometry("500x300")  # установка размеров окна
root.resizable(0, 0) # запрет на изменение размера окна

def lab2():
    """
    Открытие окна с функционалом 2 лабораторной работы.
    """
    window_lab2 = tk.Toplevel() # создание дочернего окна (на уровень выше)
    window_lab2.title("Функции и условия") # заголовок окна
    window_lab2.geometry("400x200") # размер окна
    window_lab2.resizable(0, 0) # запрет на изменение размера окна
    window_lab2.grab_set() # запрет на использование основного окна, пока работает это

    # создание доски с двумя колонками в соотношении 1:4 по ширине
    window_lab2.columnconfigure(0, weight=1)
    window_lab2.columnconfigure(1, weight=4)

    # метод, считающий все операции с двумя числами
    def start_operations():
        """
        Вычисление суммы, разницы, произведения и частного двух чисел,
        введёных в соответствующие поля.

        В результате происходит вывод всех операций в текстовое поле окна.
        """
        number_1 = int(number_1_entry.get()) # вытаскивание первого числа с перевод его в целое число (изначально это просто строка)
        number_2 = int(number_2_entry.get()) # так же со вторым числом
        result_string = "" # строка, в которой будем хранить результат
        sum = number_1 + number_2 # суммируем числа
        difference = number_1 - number_2 # вычитаем числа
        product = number_1 * number_2 # перемножаем числа
        quotient = 0 # деление изначально будет равно нулю
        if number_2 == 0: # если второе число равно нулю, то выдадим ошибку
            quotient = 'на ноль делить нельзя' # ошибка будет в виде этой строки
        else: # если второе число не равно нулю
            quotient = number_1 / number_2 # то поделим первое на второе
        # сохраним результаты вычислений всех операций с разделением красной строкой
        result_string += f'{number_1} + {number_2} = {sum}\n'
        result_string += f'{number_1} - {number_2} = {difference}\n'
        result_string += f'{number_1} * {number_2} = {product}\n'
        result_string += f'{number_1} / {number_2} = {quotient}\n'

        # текстовое поле вывода заблокировано изначально, поэтому откроем на время и запишем результат
        result_textbox.config(state=tk.NORMAL) # открытие доступа к полю
        result_textbox.delete('1.0', tk.END) # полное отчищение поля (это для случая, если там есть текст от предыдущих вычислений)
        result_textbox.insert(tk.END, result_string) # заполнение поля строкой с результатами
        result_textbox.config(state=tk.DISABLED) # закрытие доступа к полю

    # далее идут элементы графической программы
    # ttk.Label, ttk,Entry - создание элементов (строка, поле ввода и т.д.)
    # .grid - задание расположения
    # column=0 означает позицию в первой колонке
    # row=1 означает позицию во второй строке
    # columnspan=2, заполнение двух столбцов элементов (по умолчанию занимается один)
    # padx - отступ по оси X
    # pady - отступ по оси Y
    # sticky нужно для расположения в рамках выбранной через row и column ячейки (EW - вытянуть во всё поле)

    # Надпись "первое число" и её расположение
    number_1_label = ttk.Label(window_lab2, text="Первое число:")
    number_1_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)

    # Поле ввода для первого числа и его расположение
    number_1_entry = ttk.Entry(window_lab2)
    number_1_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

    # Надпись "второе число" и её расположение
    number_2_label = ttk.Label(window_lab2, text="Второе число:")
    number_2_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

    # Поле ввода для второго числа и его расположение
    number_2_entry = ttk.Entry(window_lab2)
    number_2_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    # Кнопка вычисления операций с числами и её расположение
    # В command указана команда для вычисления операций, которая находится выше
    result_button = ttk.Button(window_lab2, text="Рассчитать", command=start_operations)
    result_button.grid(column=0, row=3, columnspan=2, sticky=tk.EW, padx=5, pady=5)

    # Текстовое поле с результатами и его расположение
    result_textbox = tk.Text(window_lab2, height=4, state=tk.DISABLED)
    result_textbox.grid(column=0, row=4, columnspan=2, padx=10, pady=10)


def lab3():
    """
    Открытие окна с функционалом 3 лабораторной работы.
    """
    window_lab3 = tk.Toplevel() # создание дочернего окна (на уровень выше)
    window_lab3.title("Циклы и списки") # заголовок окна
    window_lab3.geometry("400x350") # размер окна
    window_lab3.resizable(0, 0) # запрет на изменение размера окна
    window_lab3.grab_set() # запрет на использование основного окна, пока работает это

    # создание доски с одной колонкой, заполняющей всю ширину окна
    window_lab3.columnconfigure(0, weight=1)

    # метод, генерирующий числа
    def get_random_numbers():
        """
        Генерация 10 случайных чисел в диапазоне от 1 до 100.

        В результате происходит вывод всех сгенерированных чисел в первое текстовое поле окна.
        """
        numbers_list = [randint(1, 100) for _ in range(10)] # генерация 10 случайных чисел от 1 до 100
        result_string = "" # строка результата

        # цикл прохода по числам для заполнения строки результата числами через пробел
        for number in numbers_list:
            result_string += str(number) + ' '

        # текстовое поле вывода сгерерированных чисел заблокировано изначально, поэтому откроем на время и запишем результат
        random_textbox.config(state=tk.NORMAL) # открытие доступа к полю
        random_textbox.delete('1.0', tk.END) # полное отчищение поля (это для случая, если там есть текст от генераций)
        random_textbox.insert(tk.END, result_string) # заполнение поля строкой с результатами
        random_textbox.config(state=tk.DISABLED) # закрытие доступа к полю

        # Аналогично очистим поле с операциями, так как на новом массиве они будут не актуальны
        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete('1.0', tk.END)
        result_textbox.config(state=tk.DISABLED)

    # метод, сортирующий числа по возрастанию
    def sorted_numbers_asc():
        """
        Сортировка чисел из текстового поля сгенерированных чисел по возрастанию.

        В результате происходит вывод чисел во второе текстовое поле окна.
        """
        numbers_list_str = random_textbox.get("1.0", tk.END) # получим строку сгенерированных чисел
        numbers_list = [int(number) for number in numbers_list_str.split()] # сохранение строки чисел в список формата целых чисел
        numbers_list.sort() # сортировка (по умолчанию по возрастанию)
        result_string = "" # строка для сохранения результата

        # сохранение отсортированных чисел в строку через пробел
        for number in numbers_list:
            result_string += str(number) + ' '

        # текстовое поле заблокировано изначально, поэтому откроем на время и запишем результат
        result_textbox.config(state=tk.NORMAL) # открытие доступа к полю
        result_textbox.delete('1.0', tk.END) # полное отчищение поля (это для случая, если там есть текст от предыдущих вычислений)
        result_textbox.insert(tk.END, result_string) # заполнение поля строкой с результатами
        result_textbox.config(state=tk.DISABLED) # закрытие доступа к полю

    # метод, сортирующий числа по убыванию
    # аналогично методу сортировки по возрастанию (выше)
    def sorted_numbers_desc():
        """
        Сортировка чисел из текстового поля сгенерированных чисел по убыванию.

        В результате происходит вывод чисел во второе текстовое поле окна.
        """
        numbers_list_str = random_textbox.get("1.0", tk.END)
        numbers_list = [int(number) for number in numbers_list_str.split()]
        numbers_list.sort(reverse=True) # только здесь reverse=True для сортировки убыванию
        result_string = ""
        for number in numbers_list:
            result_string += str(number) + ' '

        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete('1.0', tk.END)
        result_textbox.insert(tk.END, result_string)
        result_textbox.config(state=tk.DISABLED)

    # метод, ищущий максмальное значение среди чисел
    def get_max_value():
        """
        Поиск максимального значения из текстового поля сгенерированных чисел по возрастанию.

        В результате происходит вывод максимума во второе текстовое поле окна.
        """
        numbers_list_str = random_textbox.get("1.0", tk.END) # получим строку сгенерированных чисел
        numbers_list = [int(number) for number in numbers_list_str.split()] # сохранение строки чисел в список формата целых чисел
        max_value = max(numbers_list) # вычисление максимального
        result_string = f'max = {max_value}' # сохранение результата в строку

        # текстовое поле заблокировано изначально, поэтому откроем на время и запишем результат
        result_textbox.config(state=tk.NORMAL) # открытие доступа к полю
        result_textbox.delete('1.0', tk.END) # полное отчищение поля (это для случая, если там есть текст от предыдущих вычислений)
        result_textbox.insert(tk.END, result_string) # заполнение поля строкой с результатами
        result_textbox.config(state=tk.DISABLED) # закрытие доступа к полю

    # метод, ищущий минимальное значение среди чисел
    # аналогично методу поиска максимума (выше)
    def get_min_value():
        """
        Поиск минимальное значения из текстового поля сгенерированных чисел по возрастанию.

        В результате происходит вывод минимума во второе текстовое поле окна.
        """
        numbers_list_str = random_textbox.get("1.0", tk.END)
        numbers_list = [int(number) for number in numbers_list_str.split()]
        min_value = min(numbers_list) # только здесь ищется минимум
        result_string = f'min = {min_value}'

        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete('1.0', tk.END)
        result_textbox.insert(tk.END, result_string)
        result_textbox.config(state=tk.DISABLED)

    # метод, вычисляющий сумму всех сгенерированных чисел
    def get_sum():
        """
        Вычисление суммы чисел из текстового поля сгенерированных чисел по возрастанию.

        В результате происходит вывод суммы во второе текстовое поле окна.
        """
        numbers_list_str = random_textbox.get("1.0", tk.END) # получим строку сгенерированных чисел
        numbers_list = [int(number) for number in numbers_list_str.split()] # сохранение строки чисел в список формата целых чисел
        summa = sum(numbers_list) # поиск суммы
        result_string = f'sum = {summa}' # сохранение результата в строку

        # текстовое поле заблокировано изначально, поэтому откроем на время и запишем результат
        result_textbox.config(state=tk.NORMAL) # открытие доступа к полю
        result_textbox.delete('1.0', tk.END) # полное отчищение поля (это для случая, если там есть текст от предыдущих вычислений)
        result_textbox.insert(tk.END, result_string) # заполнение поля строкой с результатами
        result_textbox.config(state=tk.DISABLED) # закрытие доступа к полю

    # далее идут элементы графической программы
    # ttk.Label, ttk,Entry - создание элементов (строка, поле ввода и т.д.)
    # .grid - задание расположения
    # column=0 означает позицию в первой колонке
    # row=1 означает позицию во второй строке
    # columnspan=2, заполнение двух столбцов элементов (по умолчанию занимается один)
    # padx - отступ по оси X
    # pady - отступ по оси Y
    # sticky нужно для расположения в рамках выбранной через row и column ячейки (EW - вытянуть во всё поле)

    # Кнопка для генерации 10 случайных чисел и её расположение
    # В command указана команда для этого, которая находится выше
    random_button = ttk.Button(window_lab3, text="Сгенерировать 10 случайных чисел", command=get_random_numbers)
    random_button.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

    # Текстовое поле для вывода чисел и его расположение
    random_textbox = tk.Text(window_lab3, height=1, state=tk.DISABLED)
    random_textbox.grid(column=0, row=1, padx=10, pady=10)

    # Заголовок "операции" и его расположение
    number_2_label = ttk.Label(window_lab3, text="Операции")
    number_2_label.grid(column=0, row=2, sticky=tk.N, padx=10, pady=5)

    # Текстовое поле для результата операций и его расположение
    result_textbox = tk.Text(window_lab3, height=1, state=tk.DISABLED)
    result_textbox.grid(column=0, row=3, padx=10, pady=10)

    # Кнопка для сортировки чисел по возрастанию и её расположение
    # В command указана команда для этого, которая находится выше
    sort_asc_button = ttk.Button(window_lab3, text="Отсортировать по возрастанию", command=sorted_numbers_asc)
    sort_asc_button.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)

    # Кнопка для сортировки чисел по убыванию и её расположение
    # В command указана команда для этого, которая находится выше
    sort_desc_button = ttk.Button(window_lab3, text="Отсортировать по убыванию", command=sorted_numbers_desc)
    sort_desc_button.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

    # Кнопка для вычисления максимального значения среди чисел и её расположение
    # В command указана команда для этого, которая находится выше
    max_value_button = ttk.Button(window_lab3, text="Максимальное значение", command=get_max_value)
    max_value_button.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5)

    # Кнопка для вычисления минимального значения среди чисел и её расположение
    # В command указана команда для этого, которая находится выше
    min_value_button = ttk.Button(window_lab3, text="Минимальное значение", command=get_min_value)
    min_value_button.grid(column=0, row=7, sticky=tk.EW, padx=5, pady=5)

    # Кнопка для вычисления суммы чисел и её расположение
    # В command указана команда для этого, которая находится выше
    sum_button = ttk.Button(window_lab3, text="Сумма чисел", command=get_sum)
    sum_button.grid(column=0, row=8, sticky=tk.EW, padx=5, pady=5)


def lab4():
    """
    Открытие окна с функционалом 4 лабораторной работы.
    """
    window_lab4 = tk.Toplevel() # создание дочернего окна (на уровень выше)
    window_lab4.title("Файлы") # заголовок окна
    window_lab4.geometry("400x350") # размер окна
    window_lab4.resizable(0, 0) # запрет на изменение размера окна
    window_lab4.grab_set() # запрет на использование основного окна, пока работает это

    # создание доски с двумя колонками в соотношении 1:4 по ширине
    window_lab4.columnconfigure(0, weight=1)
    window_lab4.columnconfigure(1, weight=4)

    # метод создания файла со случайными числами
    def create_file():
        """
        Создание файла с 10 случайнами числами и сохранение этого файла в папке на рабочем столе.

        При успешном создании файла появится сообщение об этом.
        """
        file_name = file_name_entry.get() # достаём имя файла из текстового поля
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Рабочий стол') # получение пути к рабочему столу
        try:
            # если папки не существует, создадим папку 'lab6_files'
            os.makedirs(os.path.join(desktop_path, 'lab6_files'))
        except FileExistsError:
            # если существует, сообщим об этом в консоли
            print("Папка уже существует")

        # создание пути к файлу
        file_path = os.path.join(desktop_path, f'lab6_files\{file_name}.txt')

        # работа с файлом
        # w+ - режим работы с файлом (открывает файл для чтения и записи и создает новый файл, удаляя существующий)
        my_file = open(file_path, 'w+')

        # цикл для заполнения файла 10 случайными числами
        for i in range(10):
            random_number = randint(0, 100)  # генерация случайного целого числа от 0 до 20
            random_number_str = str(random_number)  # перевод числа в формат строки, т.к. текстовый файл хранит только строки
            my_file.write(random_number_str + '\n')  # запись числа в формате строки с красной строкой после него
        my_file.close()  # завершение работы с файлом

        # вывод окна сообщения об успешной операции
        showinfo(
            title='Успешно!',
            message=f'Файл создан и сохранён в {file_path}'
        )

    # метод выбора файла для чтения
    def select_file():
        """
        Чтение выбранного текстового файла.
        Файл должен содержать только случайные числа, разделённые между собой пробелом.

        При успешном чтении файла в текстовом поле выведется список чисел из файла и их среднее арифметическое.
        """
        # доступные 2 типа файлов (сначала название типа, потом доступный формат)
        filetypes = (
            ('Текстовые файлы', '*.txt'),
            ('Все файлы', '*.*')
        )

        # окно, дающее выбрать файл
        filename = fd.askopenfilename(
            title='Выбор файла', # заголовок окна
            initialdir=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Рабочий стол'), # папка, которая открывается при появлении окна
            filetypes=filetypes # доступные типы файлов, что указаны выше
        )

        message = f'Выбранный файл:\n {filename}' # сохранение в строку информации о файле
        select_file_label.config(text=message) # сохранение сообщения в строке в графической программе

        numbers_list = []  # создание массива для хранения чисел

        # работа с файлом
        # r - режим работы с файлом (открывает файл для чтения)
        with open(filename, 'r') as my_file:
            # цикл обхода файла по строкам
            for line in my_file:
                number = int(line)  # перевод числа в формате строки в формат целого числа
                numbers_list.append(number)  # добавление числа в массив

        result_string = '' # строка для сохранения результатов

        # цикл для сохранения чисел через пробел в строку результата
        for number in numbers_list:
            result_string += str(number) + ' '

        sa = sum(numbers_list) / len(numbers_list) # вычисление среднего арифметического
        result_string += f'\nСреднее арифметическое = {sa}' # сохранение ср.арифмитеческого строку результата после красной строки

        # текстовое поле вывода заблокировано изначально, поэтому откроем на время и запишем результат
        result_file_read_textbox.config(state=tk.NORMAL) # открытие доступа к полю
        result_file_read_textbox.delete('1.0', tk.END) # полное отчищение поля (это для случая, если там есть текст от предыдущих вычислений)
        result_file_read_textbox.insert(tk.END, result_string) # заполнение поля строкой с результатами
        result_file_read_textbox.config(state=tk.DISABLED) # закрытие доступа к полю

    # далее идут элементы графической программы
    # ttk.Label, ttk,Entry - создание элементов (строка, поле ввода и т.д.)
    # .grid - задание расположения
    # column=0 означает позицию в первой колонке
    # row=1 означает позицию во второй строке
    # columnspan=2, заполнение двух столбцов элементов (по умолчанию занимается один)
    # padx - отступ по оси X
    # pady - отступ по оси Y
    # sticky нужно для расположения в рамках выбранной через row и column ячейки (EW - вытянуть во всё поле)

    # Заголовок раздела и его расположение
    create_file_label = ttk.Label(window_lab4, text="Создание файла")
    create_file_label.grid(column=0, row=0, columnspan=2, sticky=tk.N, padx=10, pady=5)

    # Надпись "Название файла" и её расположение
    file_name_label = ttk.Label(window_lab4, text="Название файла:")
    file_name_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

    # Поле ввода для названия файла и его расположение
    file_name_entry = ttk.Entry(window_lab4)
    file_name_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    # Кнопка вычисления создания файла с введённым названием
    # В command указана команда для создания файла, которая находится выше
    open_file_in_button = ttk.Button(window_lab4, text="Создать файл с случайными числами", command=create_file)
    open_file_in_button.grid(column=0, row=2, columnspan=2, sticky=tk.EW, padx=5, pady=5)

    # Пустая строка чисто ради отступа и её расположение
    empty_label = ttk.Label(window_lab4)
    empty_label.grid(column=0, row=3, columnspan=2, sticky=tk.N, padx=10, pady=20)

    # Заголовок раздела и его расположение
    read_file_label = ttk.Label(window_lab4, text="Чтение файла")
    read_file_label.grid(column=0, row=4, columnspan=2, sticky=tk.N, padx=10, pady=5)

    # Кнопка выбора файла в формате .txt
    # В command указана команда для выбора файла для чтения, которая находится выше
    open_file_in_button = ttk.Button(window_lab4, text="Выбрать файл", command=select_file)
    open_file_in_button.grid(column=0, row=5, columnspan=2, sticky=tk.EW, padx=5, pady=5)

    # Текстовое поле с результами прочитанного файла и его расположение
    result_file_read_textbox = tk.Text(window_lab4, height=2, state=tk.DISABLED)
    result_file_read_textbox.grid(column=0, row=6, columnspan=2, sticky=tk.EW, padx=5, pady=5)

    # Надпись для хранения информации о выбранном файле
    select_file_label = ttk.Label(window_lab4, text="")
    select_file_label.grid(column=0, row=7, columnspan=2, sticky=tk.N, padx=10, pady=5)



# создание полотна для помещения в него элементов
menu = tk.Frame(root)
# помещение элемента в основное окно
# (.pack - помещение на основном окне, ну или упаковка другими словами)
# (BOTH - растяжение по вертикали и горизонтали)
# (expand=True - заполнение всего пространства полотна)
menu.pack(fill=tk.BOTH, expand=True)

# Формирование шрифта (сначала семейство шрифта Calibri, потом размер 12, потом указание на его жирность)
font = font.Font(family="Calibri", size=12, weight="bold")

# Создание заголовка меню с выбором созданного шрифта + серого фона и помещение (.pack) этого в полотно
label = tk.Label(menu, text="Лабораторная работа №6", bg="gray", font=font)
label.pack(fill='x')

# Создание кнопки для 2 лабы с выбором функции, открывающей новое окно, и помещение (.pack) этой кнопки на полотно
button_2 = ttk.Button(menu, text="Лаб_2. Функции и условия", command=lab2)
button_2.pack(fill=tk.BOTH, expand=True)

# Создание кнопки для 3 лабы с выбором функции, открывающей новое окно, и помещение (.pack) этой кнопки на полотно
button_3 = ttk.Button(menu, text="Лаб_3. Циклы и списки", command=lab3)
button_3.pack(fill=tk.BOTH, expand=True)

# Создание кнопки для 4 лабы с выбором функции, открывающей новое окно, и помещение (.pack) этой кнопки на полотно
button_4 = ttk.Button(menu, text="Лаб_4. Файлы", command=lab4)
button_4.pack(fill=tk.BOTH, expand=True)

# Создание кнопки выхода с указанием команды на завершение программы (root.destroy) и помещение этой кнопки на полотне
button_exit = ttk.Button(menu, text="Выход", command=root.destroy)
button_exit.pack(fill=tk.BOTH, expand=True)

# Зацикливание основного окна для работы программы
root.mainloop()