# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

color = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
for i, val in enumerate(color):
    print(f'{i} : {val}')
color_selection = int(input("Выберите номер цвета: "))


def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point


def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=c1, width=1)
        point = end_point


start_point = [(100, 100, 150, 3), (100, 350, 150, 4), (350, 100, 100, 5), (350, 350, 100, 6)]

for _ in start_point:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    heads_start = _[3]
    if color_selection == 0:
        c1 = sd.COLOR_RED
    elif color_selection == 1:
        c1 = sd.COLOR_ORANGE
    elif color_selection == 2:
        c1 = sd.COLOR_YELLOW
    elif color_selection == 3:
        c1 = sd.COLOR_GREEN
    elif color_selection == 4:
        c1 = sd.COLOR_CYAN
    elif color_selection == 5:
        c1 = sd.COLOR_BLUE
    elif color_selection == 6:
        c1 = sd.COLOR_PURPLE
    else:
        print('Вы ввели неверное значение')
        break
    polygon(point_start, heads_start, length_start)
sd.pause()
