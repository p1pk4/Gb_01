'''
# Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и dict.
#
# Task 3.
'''

# dict
Seasons = {
    # key:value,
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}

print('Enter the month number: ')
num_dict = int(input())

for i in range(num_dict):
    if 1 <= num_dict <= 2 or num_dict == 12:
        # Вызов по переменной.
        print(Seasons[num_dict]) 
        break
    elif 3 <= num_dict <= 5:
        # Вызов по индексу.
        print(Seasons[3]) 
        break
    elif 6 <= num_dict <= 8:
        print(Seasons[6])
        break
    elif 9 <= num_dict <= 11:
        print(Seasons[9])
        break
    else:
        print('Wrong number. Try again:')
        num_dict = int(input())


# list
seasons_list = ['Winter','Spring', 'Summer', 'Autumn']

print('Enter the month number: ')
num_list = int(input())

for j in range(num_list):
    if 1 <= num_list <= 2 or num_list == 12:
        print(seasons_list[0])
        break
    elif 3 <= num_list <= 5:
        print(seasons_list[1])
        break
    elif 6 <= num_list <= 8:
        print(seasons_list[2])
        break
    elif 9 <= num_list <= 11:
        print(seasons_list[3])
        break
    else:
        print('Wrong number. Try again:')
        num_list = int(input())