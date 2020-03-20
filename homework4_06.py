# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for i in count(start_number):
        if i > stop_number:
            break
        else:
            print(i)


def my_cycle_func(my_list, iteration):
    k = 0
    iter_var = cycle(my_list)
    while k < iteration:
        print(next(iter_var))
        k += 1


my_count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")))
my_cycle_func(my_list=[1, 2], iteration=int(input("enter iteration: ")))
