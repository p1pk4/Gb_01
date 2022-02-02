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
    """\n\033[38;5;45mРасчет массы асфальта.

    Значения длины, ширины, массы и толщины задаются в экземпляре класса.
    Расчет в методе 'calc_of_mass'. 
    Формула: __length * __width * __weight * __thickness --> result\033[0;0m
    """
    def __init__(self, __length, __width, __weight, __thickness):
        self.__length = __length
        self.__width = __width
        self.__weight = __weight
        self.__thickness = __thickness

    def calc_of_mass(self):
        result = new_road.__length * new_road.__width * new_road.__weight * new_road.__thickness
        print(result)
        return result
        
print(Road.__doc__)
# Экземпляр класса с защищенными атрибутами. 
new_road = Road(5000, 20, 25, 5)
new_road.calc_of_mass()


# Сначала сделал с наследованием и переопределением, потом переделал по условию.
class SecondRoad:
    # __length = 0
    # __width = 0
    # __weight = 0
    # __thickness = 0
    pass

class NewSecondRoad(SecondRoad):
    __length = 5000
    __width = 20
    __weight = 25
    __thickness = 5

    def calc_of_mass(self):
        result = new_second_road.__length * new_second_road.__width * new_second_road.__weight * new_second_road.__thickness
        print(f'\nВторая дорога - {result}')
        
# Экземпляр класса с защищенными атрибутами. 
new_second_road = NewSecondRoad()
new_second_road.calc_of_mass()