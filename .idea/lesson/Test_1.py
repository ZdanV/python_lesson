
# Теперь сделай валидацию вводимых пользователям данных.
# Если он введёт какую-то ахинею, напиши ему, что он дурак и снова предложи ввести данные, на этот раз нормальные.
# Добавь, чтоб можно было вводить также кол-во частей для разбиения,
# процент, на который нужно уменьшать каждое последующее число,
# коэффициент, на который умножается этот процент

def calculation_function (number, part, percent):

    number_1 = (number / part) + (number * percent / 2) - ((number * percent / 2) / part)
    print(number_1)
    count = number_1

    for i in range(1, part):
        number_1 -= (number / part * percent)
        print(number_1)

        count += number_1

    print(count)

while True: #проверка на чисо для ввода числа рассчета
    try:
        input_number = int(input('Веди целое число для рассчета: '))
        break
    except ValueError:
        print('НЕТ!!! Введи целое число, а не ерунду в виде строки или дроби!!!')

while True: #проверка на число (часть на которую делить)
    try:
        input_part = int(input('Введи количество частей на которое разделить число: '))
        break

    except ValueError:
        print('НЕТ!!! Введи целое число, а не ерунду в виде строки или дроби!!!')

while True: #проверка на чисо для ввода (процент понижения)
    try:
        input_percent = float(input('Введи процент, на который необходимо понижать последущую ставку: '))
        break

    except ValueError:
        print('НЕТ!!! Введи целое число, а не ерунду в виде строки или дроби!!!')

calculation_function(input_number, input_part, input_percent) #вывод функции