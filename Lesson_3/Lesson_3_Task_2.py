'''
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.
#
# Task 2.
'''

def birth_year():
    """Возвращает год рождения.

    Пользовательский ввод.
    Отлавливает ValueError.
    Проверяет введенный диапазон.

    """
    print("Введите ваш год рождения: ")
    for _ in range(20):
        try:
            year = int(input())
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз: ")
            continue
        while year <= 0:
            print("Марти Макфлай, ты ли это? Попробуйте еще раз: ")
            year = int(input())
            if year > 10000:
                print("Марти Макфлай, ты ли это? Попробуйте еще раз: ")
                year = int(input())
            else:
                break
        break
    return year


def email():
    """Возвращает email.
    
    Проверяет есть ли символ '@' в пользовательском вводе.

    """
    print("Введите ваш email: ")
    mail = input()
    dog = "@"
    while dog in mail:
        break
    else:
        print("Собачкам не нравится когда про них забывают =(\nВведите почту еще раз: ")
        mail = input()
    return mail


def mnumber():
    """Возвращает номер телефона.

    Проверяет количество введенных цифр.
    При не правильном вводе публикует номер на всех сайтах интернета.

    """
    print("Введите ваш номер телефона: ")
    for _ in range(20):
        try:
            number = int(input())
            number = str(number)
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз: ")
            continue
        # Вызывается только если пользователь ввел не 11 цифр.
        while len(number) < 11:
            print("Мы никому не скажем ваш номер телефона! Попробуйте еще раз: ")
            number = int(input())
            number = str(number)
            if len(number) == 11:
                print("Публикую номер в интернете на всех сайтах...")
                percent = 100
                for j in range(-1,percent,20):
                    j += 1
                    print(f".......{j}" + "%")
                print("Номер опубликован!\nХорошего дня!")
        break
    return number


def user_info():
    """Возвращает функции и переменные, выводит на экран все одной строкой.

    name, surname, city - пользовательский ввод.
    birth_year(), email(), mnumber() принимают разные значения и возвращают в эту функцию.
    
    """
    print("Введите ваше имя: ")
    name = input()
    print("Введите вашу фамилию: ")
    surname = input()
    print("Введите ваш город проживания: ")
    city = input()
    return name, surname, city, birth_year(), email(), mnumber()

def how_many_times(a):
    """Количество вызывов функции user_info
    
    a -- По умолчанию 1.
    """
    for i in range(a):
        i += 1
        print(f"{i} анкета.")
        print(user_info())
    
how_many_times(a = 1)