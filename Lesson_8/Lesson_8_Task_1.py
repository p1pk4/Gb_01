'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. 
#
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#
Проверить работу полученной структуры на реальных данных.
#
Task 1.
'''

from datetime import date

class Data:
    

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def str_to_int(cls):
        '''
            Метод должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
        '''
        print('Преобразование str к типу "Число".')
        a.year = int(a.year)
        a.month = int(a.month)
        a.day = int(a.day)

    @staticmethod
    def valid_data(year, month, day):
        '''
            Метод должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
        '''
        try:
            date(year, month, day)
            print('С датой все ок!')
            return True
        except:
            print('Неверно ввели дату!')
            return False

a = Data('1983', '11', '18')
a.str_to_int()
a.valid_data(1454, 11, 18)