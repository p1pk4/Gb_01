'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
#
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров).
#
Task 3.
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}
        
    
class Position(Worker):
    
    def get_full_name(self):
        """
            Метод выводит на экран полное имя сотрудника и его доход.
        """
        
        print(f'Имя и фамилия сотрудника: {worker_one.name} {worker_one.surname}. Доход: {worker_one.get_total_income()}')
        print(f'Имя и фамилия сотрудника: {worker_two.name} {worker_two.surname}. Доход: {worker_two.get_total_income()}')
        print(f'Имя и фамилия сотрудника: {worker_three.name} {worker_three.surname}. Доход: {worker_three.get_total_income()}')

    def get_total_income(self):
        """
            Метод получения дохода с учетом премии.
        """
        
        return self._income['wage'] + self._income['bonus']
        # print(worker_one.get_total_income())

class InfoAboutWorkers(Position, Worker):

    def __init__(self):
        self.get_full_name()
        # self.get_total_income()
        
worker_one = Position('Dylan', 'Oneil', 'Doctor', '8000', '16000')
worker_two = Position('Sara', 'Ohara', 'Barmen', '5500', '6500')
worker_three = Position('Roza', 'Griffin', 'CEO', '17000', '34000')

workers_info = InfoAboutWorkers()