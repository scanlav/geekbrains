# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


workers = {'Ivanov': 15000, 'Petrov': 20000, 'Sidorov': 27000, 'Putin': 199900}
try:
    with open('file_02.txt', 'w') as file_obj:
        for last_name, salary in workers.items():
            file_obj.write(last_name + ': ' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка")
finally:
    file_obj.close()
sum_money = 0
count = 0
persons = []
with open('file_02.txt', 'r') as file_obj:
    for line in file_obj:
        print(line, end='')
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        sum_money += int(tokens[1])
        count += 1
result = sum_money / count
print(f"Сотрудники: {persons}")
print(f"Средний доход: {result}")

