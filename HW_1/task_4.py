"""
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

income = int(input("Введите оборот компании: "))
cost = int(input("Введите сумму расходов компании: "))

fin_result = income - cost

if fin_result > 0:
    ratio = income / cost
    print(
        f"Ваша прибыль равна: {fin_result}, Вы молодец!! Работаете в плюс \n "
        f"Соотношение составляет {ratio}")

    worked_count = int(input("Введите количество сотрудников: "))
    profit_of_worker = fin_result // worked_count
    print(f"Прибыль на одного сотрудника составляет: {profit_of_worker}")

elif not fin_result:
    print("Нет прибыли нет убытков! Надо что-то делать ")
else:
    print(f"Казна пустеет, ваши убытки: {fin_result}")
