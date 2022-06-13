from random import randint


class Man:

    def __init__(self, name):
        self.name = name
        self.foolness = 50
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'Я {}, сытость {}'.format(
            self.name, self.foolness)

    def eat(self):
        if self.food >= 10:
            print("{} поел".format(self.name))
            self.foolness += 10
            self.food -= 10
        else:
            print("{} нет еды".format(self.name))

    def work(self):
        self.money += 50
        print('{} сходил на работу, денег стало {}'.format(self.name, self.money))
        self.foolness -= 10

    def game(self):
        print('{} играл в игры целый день'.format(self.name))
        self.foolness -= 10

    def go_shop(self):
        if self.money >= 50:
            print('{} сходил в магазин'.format(self.name))
            self.money -= 50
            self.food += 50
            self.foolness -= 10
        else:
            print('Деньги кончились!')

    def act(self):
        if self.foolness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.foolness < 20:
            self.eat()
        elif self.food < 20:
            self.go_shop()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.game()


vasya = Man(name='Вася')
petya = Man(name='Петя')
for day in range(1, 366):
    print('================= День {} ===================='.format(day))
    vasya.act()
    petya.act()
    print(vasya)
    print(petya)
