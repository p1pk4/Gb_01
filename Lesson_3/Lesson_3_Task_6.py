'''
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Task 6.
'''

def int_func():
    '''Принимает слова и возвращает каждое слово с большой буквы.
    
    '''
    some_text = input()
    print(some_text.title())

print(int_func.__doc__)
int_func()