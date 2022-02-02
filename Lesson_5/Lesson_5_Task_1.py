'''
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных будет свидетельствовать пустая строка.
#
Task 1.
'''


print('Input strings: ')

with open('t1.txt', 'w+', encoding='utf-8') as f_obj:
    
    while True:
        user_input = input()
        f_obj.write(user_input + '\n')
        if not user_input:
            break