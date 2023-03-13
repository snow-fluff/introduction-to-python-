# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('Введите размер массива: '))
minNum = int(input('Введите минимальную границу: '))
maxNum = int(input('Введите максимальную границу: '))

array = []
arrayInd = []

for i in range(n):
    array.append(random.randint(0,9))
print(array)

for i in range(n):
    if minNum <= array[i] <= maxNum:
        arrayInd.append(i)

print(arrayInd)