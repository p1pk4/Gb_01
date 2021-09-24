'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными.
#
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: 
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. 
Проверить работу метода.
#
Например: 20м * 5000м * 25кг * 5см = 12500 т
#
Task 2.
'''

class Road:

    def __init__(self, __length, __width, __weight, __thickness):
        self.__length = __length
        self.__width = __width
        self.__weight = __weight
        self.__thickness = __thickness

    def calc_of_mass(self):
        result = new_road.__length * new_road.__width * new_road.__weight * new_road.__thickness
        print(result)
        return result
        
# Экземпляр класса с защищенными атрибутами. 
new_road = Road(5000, 20, 25, 5)
new_road.calc_of_mass()