# -*- coding: utf-8 -*-

# положить в массив два значения
# начал цикл игры:
#     ждать от пользователя команды
#     когда получим команду, обработать массив
#     найти пустые клетки
#     если есть пустые клетки, случайно выбрать одну из них
#     и положить туда либо 2, либо 4
#     если пустых клеток нет и нельзя двигать маасив, игра закончане

import random

# Красивый вывод массива
def pretty_mas(mas):
    print('-' * 8)
    for row in mas:
        print(*row)
    print('-' * 8)


# получаем номер ячейки на игровом поле (от 1 до 16)
def get_number_from_index(i, j):
    return i * 4 + j + 1


# получаем координаты ячейки по номеру ячейки на игровом поле
def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


# вставляем 2 или 4 в массив
def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


# получаем список пустых ячеек
def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


# создаем начальный массив
mas = [[0] * 4 for i in range(4)]

# проставляем 2 случайных значения
mas[1][2] = 2
mas[3][0] = 4

print(get_empty_list(mas))
pretty_mas(mas)




