# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
# генератор.

my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
new_list= [i for i in my_list if i > my_list[my_list.index(i)-1]]
print(new_list)