# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_list = []
while True:
    user_input = input('Введите текст: ')
    if user_input == '':
        print(user_list)
        exit()
    else:
        line = user_input + '\n'
        user_list.append(line)
    with open("user.txt", "w") as file_user:
        file_user.writelines(user_list)

