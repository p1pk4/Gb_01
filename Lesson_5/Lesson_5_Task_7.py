'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
#
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#
Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
#
Task 7.
'''

import json
from os import environ


result_list = []
dict_plus_profit = {}
dict_minus_profit = {}

with open('t7.txt') as file:
    average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)

        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_profit.update({name: profit})
        else:
            dict_minus_profit.update({name: profit})
    result_list.append(dict_plus_profit)
    result_list.append(dict_minus_profit)
    result_list.append({'average_profit': sum(average_profit_list)/len(average_profit_list)})

with open('t7.json', 'w') as file:
    
    json.dump(result_list, file, indent=2)