# from termcolor import cprint
from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        cprint('{} играл весь день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.money -= 50
            self.food += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='orange')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()

beavis = Man(name='Бивис')
butthead = Man(name='Батхед')


for day in range(1, 366):
    print('=============== день {} =============='.format(day))
    beavis.act()
    butthead.act()
    print(beavis)
    print(butthead)

