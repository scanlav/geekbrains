# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

list_txt = ['Hello \n','World \n','Python \n','Swift \n']
with open('file_01.txt', 'w+') as file_obj:
    file_obj.writelines(list_txt)
with open('file_01.txt', 'r') as file_obj:
    letters = 0
    lines = 0
    num = 1
    for line in file_obj:
        lines += line.count('\n')
        letters = len(line) - 1
        print(f'Символов в строке #{num} - {letters}')
        num += 1
    print(f'Строк в файле {file_obj.name} - {lines}')

