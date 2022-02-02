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

# char = '-'
# my_list = ['Один', "Два ", "Три ", "Четыре "]

my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

with open('t4.txt') as file_t4, open('t4_2.txt', 'w', encoding='utf-8') as file_t4_write:
    for line in file_t4.readlines():
        words, numbers = line.rstrip().split(" - ")
        file_t4_write.write(f'{my_dict[words]} - {numbers}\n')