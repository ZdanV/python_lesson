
age = int(input())
height = float(input())
weight = float(input())

bmi = weight / height ** 2
bmi = round(bmi, 2)

if age < 10 or height <= 0 or height > 300 or weight <= 0 or weight > 500:
    print('ошибочные входные данные')
elif age < 45:
    if bmi < 18.5:
        disc = 'не достаточной массой тела.'
    elif bmi < 25 and bmi >= 18.5:
        disc = 'нормальной массой тела.'
    elif bmi < 29.99 and bmi >= 25:
        disc = 'избыточной массой тела.'
    else:
        disc = 'ожирением.'
    print('bmi=', bmi, 'Вы относитесь к группе людей с', disc)
elif age >= 45:
    if bmi < 22:
        disc = 'не достаточной массой тела.'
    elif bmi < 26.99 and bmi >= 22:
        disc = 'нормальной массой тела.'
    elif bmi < 31.99 and bmi >= 27:
        disc = 'избыточной массой тела.'
    else:
        disc = 'ожирением.'
    print('bmi=', bmi, 'Вы относитесь к группе людей с', disc)

