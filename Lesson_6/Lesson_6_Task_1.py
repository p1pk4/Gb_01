'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
Задачу можно усложнить, реализовав проверку порядка режимов, 
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
#
Task 1.
'''

import time
import sys


class TrafficLight():

    # Запуск светофора.
    def running(self):
        
        # Таймеры каждого света.
        def red_pause():
            timer = 7
            print(f'\033[38;5;196mКрасный! Надо подождать еще {timer} секунд.\033[0;0m')
            for i in '7 6 5 4 3 2 1\n':
                time.sleep(0.2)
                sys.stdout.write(i)
                sys.stdout.flush()
            # time.sleep(7)
        def yellow_pause():
            timer = 2
            print(f'\n\033[38;5;220mЖелтый! Через {timer} секунды можно будет ехать.\033[0;0m')
            for i in '2 1\n':
                time.sleep(0.2)
                sys.stdout.write(i)
                sys.stdout.flush()
            # time.sleep(2)
        def green_pause():
            timer = 10
            print(f'\n\033[38;5;46mЗеленый! Поехали. У нас есть {timer} секунд.\033[0;0m')
            for i in '10 9 8 7 6 5 4 3 2 1\n':
                time.sleep(0.2)
                sys.stdout.write(i)
                sys.stdout.flush()
            # time.sleep(10)
        
        red_pause()
        yellow_pause()
        green_pause()

start_traffic_light = TrafficLight()
start_traffic_light.running()