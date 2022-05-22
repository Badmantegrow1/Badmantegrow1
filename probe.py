# a = input().split()
# b = []
# while a[0] != 'end':
#     b.append(a)
#     a = input().split()
# print(b)

# for i in range(len(b)):
#     s = []
#     for j in range(len(b)):
#         s.append(b[i-1][j]+b[i-2][j]+b[i][j-1]+b[i][j-2])
#     print(*s, end=' ')
#     print()

#         break
# res_1 = a[0:s]
# numbers = [int(i) for i in input().split()]
# numbers.sort()
# num = []
# a = [(i for i in range(len(numbers)-1) if numbers[i] == numbers[i+1])]
# print(a)
#     else:
#         continue
# for i in num:
#     print(i, end=' ')

# numbers = [int(i) for i in input().split()]
# numbers.sort()
# num = set()
# for i in range(len(numbers)-1):
#     if numbers[i] == numbers[i+1]:
#         num.add(numbers[i])
#     else:
#         continue
# for i in num:
#     print(i, end=' ')
# a = [i*j for i in [1, 2, 3, 4, 5] for j in [1, 2, 3] if i*j > 10]
# print(a)

# a = {
#     'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
#     'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
#     'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
#     'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
#     'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
#     'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
#     'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
#     'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
#     'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
# }
# b = [(elem, a[elem]['age']) for elem in a if a[elem]['age'] > 2000]
# print(b)
#
# s = 'lksdfklfmlmaMLMDSFM3434Mknkn3knk3'
# b = [i for i in s if i.isalpha()]
# print(b)
# n = 5
# m = 5
# b = [[i * j for i in range(1, n + 1)] for j in range(1, m + 1)]
# for i in b:
#     print(i)
# # print(b)
#
# def func(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr *= i
#         yield pr
#
#
# for i in func(10):
#     print(i, end=' ')

# def func(n):
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#         print(p, end=' ')
#
#
# func(10)
# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()
# from random import randint
#
# global count, ai, repetition
# count = 4 #количество цифр в загадываемом слове
# ai = True #если True то число генерируется самостоятельно, иначе вводится человеком
# repetition = False #указывает может ли повторятся цифра в загадываемом числе
#
# def viewsettings():
#     print("Количество цифр в загадываемом числе: ", count)
#     print("Генерация числа компьютером: ", ai)
#     print("Могут ли повторятся цифры в загадываемом числе: ", repetition)
# def settings():
#     word = input("""Введите название параметра, который Вы хотите изменить:
#     count - меняет количество цифр в загадываемом слове
#     ai - генерирует число компьютер или человек загадывает сам
#     repeat - могут ли повторятся цифры в загадываемом числе
#     back - если хотите назад
#     """)
#     if word == "count":
#         count = int(input("Введите количетсво цифр в загадываемом слове: "))
#     elif word == "ai":
#         ai = bool(input("Введите True если число генерируется само или False если нет: "))
#     elif word == "repeat":
#         repetition = bool(input("Введите True если цифры могут повторятся или False если нет: "))
#     elif word == "back":
#         pass
#     else:
#         print("ERROR: parameter by name '%s' not found. Please try again" % word)
#         settings()
#     print(count)
# def play():
#     print("Заданные настройки:")
#     viewsettings()
#     print()
#     if ai:
#         number = list()
#         for i in range(0, count):
#             if not repetition:
#                 while True:
#                     e = str(randint(0, 9))
#                     if not e in number:
#                         break
#             else:
#                 e = str(randint(0, 9))
#             number.append(e)
#     else:
#         number = list(input("Введите загадываемое число: "))
#         if len(number) != count:
#             print("Количество цифр в загадываемом числе не соответсвует настройкам!")
#             return
#         if repetition:
#             for i in number:
#                 if number.count(i) > 1:
#                     print("Цифра %s повторяется!" % i)
#                     return
#     game = True
#     while game:
#         numb = list(input("Введите число: "))
#         if numb == ['e', 'x', 'i', 't']:
#             print("Правильным числом было ", number)
#             return
#         if len(numb) != len(number):
#             print("Количество цифр в вводимом числе не равно количетсву цифр в загадываемом числе!")
#             continue
#         cows = 0
#         byki = 0
#         for i in numb:
#             try:
#                 if numb.index(i) == number.index(i):
#                     byki = byki + 1
#                 else:
#                     cows = cows + 1
#             except ValueError:
#                 pass
#         if byki == count:
#             print("Вы угадали число!!!")
#             return
#         else:
#             print("Коровы: {0}. Быки: {1}".format(cows, byki))
#
# print("Быки-Коровы, Александр Гунгер 2019")
# print("  ------------------------------  ")
# print("Для выхода из программы нажмите Ctrl+C")
# while True:
#     word = input("""      -     Для показа настроек введите viewsettings
#       -     Для изменения настроек введите settings
#       -     Для начала игры введите play
#       -     Для выхода из программы введите exit
# """)
#     if word == "viewsettings":
#         viewsettings()
#     elif word == "settings":
#         settings()
#     elif word == "play":
#         play()
#     elif word == "exit":
#         exit(0)
#     else:
#         print("ERROR: command by name '%s' not found. Please try again" % word)
