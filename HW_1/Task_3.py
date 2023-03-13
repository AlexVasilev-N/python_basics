"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

number = int(input("Введите число N: "))

result = number + number
resulе2 = result + number



print(f"{number}{result}{resulе2}")
