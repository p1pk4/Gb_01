'''
Task 1.
Поработайте с переменными, создайте несколько, выведите на экран. 
Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
'''
print('Сколько попыток ты хочешь использовать?')
attempt = int(input())
some_text = 'что-нибудь'
if attempt > 5:
    while attempt > 5:
        print('Это будет слишком долго, давай поменьше:')
        attempt = int(input())
else: 
    if attempt <= 5:
        print(f'Отлично, у тебя {attempt} попыток!')
        print('Введите что-нибудь: ')
        some_text = input()
        while some_text != 'что-нибудь':
            attempt -= 1
            print(f'Неверно, у тебя осталось {attempt} попыток, попробуй еще раз:')
            some_text = input()
            if attempt == 0:
                print('У тебя закончились попытки, приходи завтра.')
                break
        if some_text == 'что-нибудь':
            print('Молодец!:)')