from random import randint


class Man:

    def __init__(self, name):
        self.name = name
        self.foolness = 50
        self.home = None

    def __str__(self):
        return '{} - сытость {}'.format(
            self.name, self.foolness)

    def eat(self):
        if self.home.food >= 10:
            print("{} поел".format(self.name))
            self.foolness += 10
            self.home.food -= 10
        else:
            print("{} нет еды".format(self.name))

    def work(self):
        self.home.money += 50
        print('{} сходил на работу, денег стало {}'.format(self.name, self.home.money))
        self.foolness -= 10

    def game(self):
        print('{} играл в игры целый день'.format(self.name))
        self.foolness -= 10

    def go_shop(self):
        if self.home.money >= 50:
            print('{} сходил в магазин'.format(self.name))
            self.home.money -= 50
            self.home.food += 50
            self.foolness -= 10
        else:
            print('Деньги кончились!')

    def go_home(self, home):
        self.home = home
        self.foolness -= 10
        print('{} Заехал в новый дом'.format(self.name))

    def act(self):
        if self.foolness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.foolness < 20:
            self.eat()
        elif self.home.food < 20:
            self.go_shop()
        elif self.home.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.game()


class Home:
    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return "В доме еды осталось {}, денег осталось {}".format(self.food, self.money)


citizens = [
    Man(name='Вася'),
    Man(name='Петя'),
    Man(name='Ваня')
    ]

my_home = Home()
for citizen in citizens:
    citizen.go_home(home=my_home)


for day in range(1, 366):
    print('================= День {} ===================='.format(day))
    for citizen in citizens:
        citizen.act()
    print('================= В конце дня ===================')
    for citizen in citizens:
        print(citizen)
    print(my_home)
