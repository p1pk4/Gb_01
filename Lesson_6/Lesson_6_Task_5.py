'''
Реализовать класс Stationery (канцелярская принадлежность).
#
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
Task 5.
'''


from colorama import Fore, Style


class Stationery:
    
    title = print('Проект - HELLO')

    def draw(self):
        print('Запуск отрисовки.\n')


class Pen(Stationery):
    
    def draw(self):
        print('Рисуем ручкой:')
        print(Style.BRIGHT + Fore.BLUE)
        print("                **    **  ********  **        **            **      ")
        print("               **    **  ********  **        **         **     **   ")
        print("              ********  **        **        **         **      **  ")
        print("             ********  ********  **        **         **      **  ")
        print("            **    **  **        **        **         **      **  ")
        print("           **    **  ********  ********  ********    **    **   ")
        print("          **    **  ********  ********  ********       **      ")
        print(Style.NORMAL + Fore.WHITE)


class Pencil(Stationery):

    def draw(self):
        print('\nРисуем карандашом:')
        print(Style.BRIGHT + Fore.RED)
        print("               *    *  *******  *        *            *   ")
        print("              *    *  *        *        *         *      *  ")
        print("             ******  *******  *        *         *      *  ")
        print("            *    *  *        *        *         *      *  ")
        print("           *    *  *******  *******  *******       *    ")
        print(Style.NORMAL + Fore.WHITE)


class Handle(Stationery):

    def draw(self):
        print('\nРисуем маркером:')
        print(Style.BRIGHT + Fore.GREEN)
        print("               ***    ***  ********   ***        ***             ***   ")
        print("              ***    ***  ***        ***        ***         ***      ***  ")
        print("             **********  ***        ***        ***         ***      ***  ")
        print(Style.NORMAL + Fore.WHITE)
        print('Маркер кончился.')

start_painting = Stationery()
start_painting.title
start_painting.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()