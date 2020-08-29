import math


# вычислить численность населения для года t по формуле
def compute_population(t):
    C = 172  # миллиарда человек-лет
    T_1 = 2000  # на 2000 год
    t_2 = 45  # лер период

    N_t = (C / t_2) * ((math.pi / 2) - (math.atan((T_1 - t) / t_2)))
    return N_t


# ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list,
# преобразовав строковые значения в целые
years_list = [int(n) for n in years_str_list]

# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list
# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"

population_list = [compute_population(n) for n in years_list]

for i in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[i], population_list[i]))