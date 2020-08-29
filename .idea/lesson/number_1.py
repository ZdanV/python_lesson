
# relize task Leshi

def function_part ( input ):

    number_input = input / 5 * 1.04
    print(number_input)

    temp_sum = number_input # промежуточный счетчик для проверки итоговой суммы

    for a in range(0, 4):
        number_input = round(number_input / 1.02, 2)
        print(number_input)
        temp_sum += number_input # счетчик итоговой суммы

    print()
    print(temp_sum) # вывод итоговой суммы

function_part(float(input()))





