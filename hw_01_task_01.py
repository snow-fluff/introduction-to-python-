# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

inNumber = int(input('Введите трехзначное число: '))
if inNumber < 100 or inNumber > 999:
    print('Число не трехзначное!')
else:
    print(inNumber, ' -> ', inNumber//100 + (inNumber//10)%10 + inNumber%10, ' (',inNumber//100, '+',(inNumber//10)%10, '+',inNumber%10, ')')