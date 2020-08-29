
# Теперь сделай валидацию вводимых пользователям данных.
# Если он введёт какую-то ахинею, напиши ему, что он дурак и снова предложи ввести данные, на этот раз нормальные.
# Добавь, чтоб можно было вводить также кол-во частей для разбиения,
# процент, на который нужно уменьшать каждое последующее число,
# коэффициент, на который умножается этот процент

def calculation_function ():

    part_percent_plus = round(input_percent * input_part * 0.045 + 1, 2) #повышение первого часла
    part_percent_minus = round(input_percent / 10 + 1, 2) #понижение на заданный процент

    number_part = round(input_number / input_part * part_percent_plus, 2)
    print(number_part) # вывод первого  увеличенного числа
    count_control = number_part # счетчик итоговой суммы для проверки

    for i in range (1, input_part):
        number_part = round(number_part / part_percent_minus, 2)
        print(number_part) # вывод почледующих чисел умегьшенных на заданный процент
        count_control += number_part # счетчик итоговой суммы для проверки

    print(count_control)

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

calculation_function() #вывод функции