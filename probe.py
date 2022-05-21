a = input().split()
b = []
while a[0] != 'end':
    b.append(a)
    a = input().split()
print(b)

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
