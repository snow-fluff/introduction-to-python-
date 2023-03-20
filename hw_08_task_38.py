# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def menuHello():
    print("1.Добавить")
    print("2.Изменить")
    print("3.Удалить")
    print("4.Вывести всех")
    print("5.Поиск по фамилии")
    print("6.Выход")
    userInput = int(input())
    if userInput == 1:
        addData()
        return True
    if userInput == 2:
        delData(input("Введите имя или фамилию: "))
        addData()
        return True
    if userInput == 3:
        delData(input("Введите имя или фамилию: "))
        return True
    if userInput == 4:
        printAll()
        return True
    if userInput == 5:
        find(input("Введите имя или фамилию: "))
        return True
    if userInput == 6:
        return False

def addData():
    data = open('file.txt', 'a')
    print('\n'*5) 
    first_name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    mid_name = input("Введите отчество: ")
    number = input("Введите номер телефона: ")
    item = [first_name, second_name, mid_name, number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
    print('\n'*5)

def delData(text):
    print('\n'*5)
    delTrue = False
    data = open('file.txt')
    lines = data.readlines()
    for line in lines:
        if line.split(' ')[0] == text or line.split(' ')[1] == text:
            lines.remove(line)
            delTrue = True
    if delTrue == True:
        data = open('file.txt', 'w')
        data.writelines(lines)
        data.close()
    else:
        print("Совпадение не найдено!")
    print('\n')

def printAll():
    print('\n'*5)
    data = open('file.txt', 'r')
    lines = data.readlines()
    lines.sort()
    for line in lines:
        print(line)
    data.close()
    print('\n')

def find(text):
    data = open('file.txt', 'r')
    for line in data:
        if line.split(' ')[0] == text or line.split(' ')[1] == text:
            print(line)
            data.close()
    print("Совпадение не найдено!")
    data.close()
    print('\n')

flag = True
while(flag):
    flag = menuHello()