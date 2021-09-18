"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

Task 1.
"""

print("Сегодня зарплата? y/n")
today = input()


def salary_func(hours, rph):
    """Расчет заработной платы сотрудника.

    hours -- Выработка в часах.
    rph -- Ставка в час. Задается пользователем.
    prize -- Если надо, прибавляем премию.
    salary -- Зарплата.
    """

    salary = hours * rph

    print('Даем премению? y/n')
    prize_input = input()

    if prize_input == 'Y' or prize_input == 'y':
        print('Сколько премия?')
        prize = int(input())
        salary += prize
        print(salary)

    else:
        print('Зарплата: {salary}. Премию не дали.')
    return salary


if today == 'Y' or today == 'y':
    print('Введите выроботку в часах и ставку')
    salary_func(hours= int(input()),rph=int(input()))
else:
    print('Сегодня зарплаты не будет!')