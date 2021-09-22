'''
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
#
Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Предусмотрите условие его завершения.
#
Например, в первом задании выводим целые числа, начиная с 3. 
При достижении числа 10 — завершаем цикл. 
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
#
Task 6.
'''

from itertools import count, cycle

start_number = 10
iterable = 'Woopy'
iterations_count = 0

def int_generator(start_number):
    for el in count(start_number):
        if el > start_number + 10:
            break
        yield el

for el in int_generator(5):
    print(el)

for i in cycle(iterable):
    if i == iterable[0]:
        iterations_count += 1
    if iterations_count < 2:
        print(i)
    else:
        break