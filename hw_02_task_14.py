# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))
i = power = 1
list_1 = []


while power <= n:
    list_1.append(power) 
    power = pow(2, i)
    i += 1    

print(list_1)
    