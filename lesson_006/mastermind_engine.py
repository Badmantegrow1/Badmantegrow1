import random
MAX_COUNT_NUMBERS = 4
MAX_NUMBERS = 9
_the_hidden_number = []
num = {}
count = 0


def put_numbers():
    global _the_hidden_number
    _the_hidden_number = []
    list_rand = list(range(1, MAX_NUMBERS))
    random.shuffle(list_rand)
    for i in range(1, MAX_COUNT_NUMBERS + 1):
        _the_hidden_number.append(list_rand[i])
    return _the_hidden_number


def check_the_number(my_numbers):
    _my_number = []
    global num
    global count
    num = {'bulls': [0], 'cows': [0]}
    win = []
    lose = []
    for i in my_numbers:
        _my_number.append(int(i))
    for i in range(len(_my_number)):
        if _the_hidden_number[i] == _my_number[i]:
            win.append(_my_number[i])
        elif _my_number[i] in _the_hidden_number:
            lose.append(_my_number[i])
        else:
            continue
    if win == _the_hidden_number:
        is_gameover()
    num['bulls'] = len(win)
    num['cows'] = len(lose)
    count += 1


def result():
    if num['bulls'] != 0 and num['cows'] == 0:
        print('Быки', num['bulls'])
    elif num['cows'] != 0 and num['bulls'] == 0:
        print('Коровы', num['cows'])
    elif num['bulls'] < len(_the_hidden_number) and num['cows'] != 0:
        print('Быки', num['bulls'], 'Коровы', num['cows'])
    else:
        print('Нет совпадений')


def is_gameover():
    return num['bulls'] == len(_the_hidden_number)


def count_num():
    print('Выполнено ходов', count)
