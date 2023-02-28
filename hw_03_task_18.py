# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('Введите размер массива: '))
array = []

for i in range(n):
    array.append(random.randint(0,9))
print(array)

x = int(input('Введите искомое число (от 0 до 9): '))
i = 1
findNum = array[0]

while i < len(array):
    if x == array[i] or (abs(x - array[i]) < abs(x - findNum)): 
        findNum = array[i]
    i += 1

print("->", findNum)