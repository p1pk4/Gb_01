'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
#
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
#
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
Task 4.
'''


import sys
import time


class Car:

    def __init__(self, car_brand, name, color, speed, is_police):
        self.car_barnd = car_brand
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        
    def show_speed(lamborghini, police_car):
        
        if  lamborghini.speed > 300:
            print('Вот это скорость!\n')
        elif police_car.speed < 300:
            print('Скорость большая, но спорткар не догнать.')

    def go(self):
        print('Машина завелась.')

    def stop(self):
        print('Машина остановилась.\n')

    def turn(self):
        print(f'Полицейский {police_car.car_barnd} {police_car.name} повернул в сторону нарушителей.\n')


class TownCar(Car):

    def about_town_car(self):
        """
            Выводим на экран всю информацию о машине которую передали в конструктор.

        """
        for i in f'\033[38;5;196mМарка - {vaz.car_barnd}.\nМодель - {vaz.name}.\nЦвет - {vaz.color}. \nСкорость - {vaz.speed}. \nПолицейская - {vaz.is_police}.\033[0;0m\n':
            time.sleep(0.03)
            sys.stdout.write(i)
            sys.stdout.flush()

    def show_speed(self):
        
        if vaz.speed > 60:
            print('Стоп! Превышение скорости!')


class SportCar(Car):

    def about_sport_car(self):
        """
            Выводим на экран всю информацию о машине которую передали в конструктор.
            
        """
        for i in f'\033[38;5;220mМарка - {lamborghini.car_barnd}.\nМодель - {lamborghini.name}.\nЦвет - {lamborghini.color}. \nСкорость - {lamborghini.speed}. \nПолицейская - {lamborghini.is_police}.\033[0;0m\n':
            time.sleep(0.03)
            sys.stdout.write(i)
            sys.stdout.flush()


class WorkCar(Car):

    def about_work_car(self):
        """
            Выводим на экран всю информацию о машине которую передали в конструктор.

        """
        for i in f'\033[38;5;250mМарка - {benson.car_barnd}.\nМодель - {benson.name}.\nЦвет - {benson.color}. \nСкорость - {benson.speed}. \nПолицейская - {benson.is_police}.\033[0;0m\n':
            time.sleep(0.03)
            sys.stdout.write(i)
            sys.stdout.flush()

    def show_speed(self):
        
        if benson.speed > 40:
            print('Стоп! Превышение скорости!')    


class PoliceCar(Car):

    def about_police_car(self):
        """
            Выводим на экран всю информацию о машине которую передали в конструктор.

        """
        for i in f'\033[38;5;32mМарка - {police_car.car_barnd}.\nМодель - {police_car.name}.\nЦвет - {police_car.color}. \nСкорость - {police_car.speed}. \nПолицейская - {police_car.is_police}.\033[0;0m\n':
            time.sleep(0.03)
            sys.stdout.write(i)
            sys.stdout.flush()


vaz = TownCar('VAZ', '2109', 'cherry', 120, False)
vaz.about_town_car()
vaz.show_speed()
vaz.stop()

lamborghini = SportCar('Lamborghini', 'Aventador', 'gold', 350, False)
lamborghini.about_sport_car()
lamborghini.go()
lamborghini.show_speed(lamborghini)

benson = WorkCar('Reno', 'Aviato', 'white', 50, False)
benson.about_work_car()
benson.show_speed()
benson.stop()

police_car = PoliceCar('Ford', 'CrownVictoria', 'blue', 250, True)
police_car.about_police_car()
police_car.show_speed(police_car)
police_car.turn()