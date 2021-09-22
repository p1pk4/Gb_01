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
one = 'Один dddd'
two = 'Два '
three = 'Три '
four = 'Четыре '
my_list = [one, "Два ", "Три ", "Четыре "]
with open('t4.txt') as f_obj4, open('t4_2.txt', 'w', encoding='utf-8') as f_obj4_w:
    for line in f_obj4.readlines():
        # print(line)
        words, numbers = line.split("-")
        
        new_numbers = numbers#.lstrip('\n').split(' ')
        new_words = words.split(' ')

        f_obj4_w.writelines(my_list[0])
        f_obj4_w.write(char)
        f_obj4_w.writelines(new_numbers)

# f_obj4_w = open('t4_2.txt', 'w', encoding='utf8')