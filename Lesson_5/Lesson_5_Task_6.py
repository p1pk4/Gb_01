'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
#
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
#
Task 6.
'''

import re
my_dict = {}

with open('t6.txt') as educations:
    for line in educations:
        lesson, *lessons_other = line.split()
        lesson_hours = [int(i.rstrip('(л)(пр)(лаб)')) for i in lessons_other if i != '—']
        my_dict.update({lesson.rstrip(':'): sum(lesson_hours)})

print(my_dict)


# with open('t6.txt', 'r', encoding='utf-8') as educations:
#     for line in educations.readlines():
#         names, hours = line.rstrip('\n').split(': ')
#         print(hours)
#         # nums = re.findall(r'\d+', line)
#         # print(type(nums))
#         # print(list(nums))
