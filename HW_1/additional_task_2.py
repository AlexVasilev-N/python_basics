"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |

"""

number = int(input("Введите 3х значное число: "))

num1 = number // 100
num2 = number // 10 % 10
num3 = number % 10

result = num1 + num2 + num3

print(num1, num2, num3)
print(f" Сумма чисел равна >>> {result}")

result2 = (number // 100) + (number // 10 % 10) + (number % 10)
print(result2)
