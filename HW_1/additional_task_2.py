"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |

"""

number = int(input("Введите 3х значное число: "))

# Вариант 1
num1 = number // 100
num2 = number // 10 % 10
num3 = number % 10

result = num1 + num2 + num3
print(f" Сумма чисел равна >>> {result}")

# Вариант 2
result2 = (number // 100) + (number // 10 % 10) + (number % 10)
print(f" Сумма чисел равна >>> {result2}")

# Вариант 3 (в данном случае мы проверяем что пользователь ввел
# именно 3х значное число)

while True:
    if 99 < number < 999:
        result3 = (number // 100) + (number // 10 % 10) + (number % 10)
        print(f" Сумма чисел равна >>> {result3}")
        break
    else:
        print("число не трехзначное ")
        break

# Вариант 4
number_2 = (input("Введите 3х значное число: "))
sum_of_numbers = 0
if len(number_2) == 3:

    for i in range(len(number_2)):
        sum_of_numbers = sum_of_numbers + int(number_2[i])
        i = +1
    print(sum_of_numbers)

else:
    print(f" -> {number_2} >>> не трехзначное число, либо не число вовсе")

