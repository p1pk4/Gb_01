'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
#
Task 2.
'''

class Zero_error:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def zero_calc(num1, num2):
        try:
            result = num1 / num2
            if num2 != 0:
                print(result)
        except ZeroDivisionError:
            print('На 0 делить нельзя!\nПопробуйте еще раз: ')
            while num2 == 0:
                num2 = int(input())
                if num2 != 0:
                    break
            print(num1 / num2)

Zero_error.zero_calc(int(input()), int(input()))