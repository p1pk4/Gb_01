'''
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
#
Task 4.
'''

char = '-'
my_list = ['Один', "Два ", "Три ", "Четыре "]
# new_numbers = []
with open('t4.txt') as f_obj4, open('t4_2.txt', 'w', encoding='utf-8') as f_obj4_w:
    for line in f_obj4.readlines():
        words, numbers = line.split("-")

    for el in my_list:
        f_obj4_w.writelines(el + char + '\n')