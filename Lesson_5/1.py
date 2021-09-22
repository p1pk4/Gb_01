'''
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных будет свидетельствовать пустая строка.
#
Task 1.
'''

with open('t1.txt', 'w', encoding='utf-8') as f_obj:
    print('Input strings: ')
    while True:
        
        user_input = input()
        f_obj.writelines(user_input.split('\n'))
        if not user_input:
            break
        
        # usess = user_input.split('\n')





    # for line in iter(input, ''):
    #     user_input = input()
    #     



    # if user_input == None:
    #     print('Strings zap')