'''
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
#
Task 2.
'''

file_zen = open('t2.txt', 'r', encoding='utf8')
str_count = 0
for line in file_zen.readlines():
    str_count +=1
    # Считаем количество слов в строче разделенных проблелом.
    line = line.split(' ')
    words = len(line)
    print(f'Количество слов в строке {str_count} = {words}')
print(f'Всего строк: {str_count}')

file_zen.close()
