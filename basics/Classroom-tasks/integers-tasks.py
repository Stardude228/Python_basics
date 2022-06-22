"""
  По теме: Числа
"""
"""
1) Напишите программу, которая просит пользователя ввести последовательно день своего рождения, затем месяц и в конце год рождения. На выходе программа должна выдавать вам сумму введенных чисел.

Пример:
Ввод: День рождения: 7
          Месяц рождения: 12
          Год рождения: 1998
Вывод: 2017
"""
birthday = int(input('День рождения:'))
birthMonth = int(input('Месяц рождения:'))
birthYear = int(input('Год рождения:'))
overall = birthday + birthMonth + birthYear
print('Вывод:', overall)

"""
2) Makers Bootcamp предоставляет скидки на обучение. Стоимость всего обучения без учета скидок составляет 600$. Напишите программу, которая будет принимать скидку на обучение и после выдавать вам сумму, которую вам остается оплатить за курс.

Примечание: при вводе не надо указывать знак %

Пример:
Ввод: Введите скидку: 7
Вывод: Оставшаяся сумма для платежа составляет 558$
"""
sale = int(input('Введите скидку: '))
restPayment = 600 - 600 * sale / 100
print("Оставшаяся сумма для платежа составляет", str(int(restPayment))+"$")

"""
3) Найдите площадь и длину круга по введенным пользователем данным. Округлите полученные числа до сотых (два знака после точки)

Примечание: Формула площади круга: πr2
Формула длины круга: 2πr, где r - радиус круга

Пример:
Ввод: Введите радиус круга: 7
Вывод: Площадь круга составляет 153.94
Длина круга составляет 43.98
"""
from math import pi
r = int(input('Введите радиус круга:'))
circleSquare = pi * r ** 2
circleLength = 2 * pi * r
print("Площадь круга равна: ", round(circleSquare, 2), "Длина круга равна: ", round(circleLength, 2))