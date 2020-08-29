# import math
#
# def f_x(x):
#    try:
#        y = 1 / (x+1) + x / (x-3)
#    except:
#        y = math.inf
#    return y
#
# t = float(input("t = "))
#
# y = f_x(t)
#
# print("f(", t, ") = ", y)

# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
# def compute_income(deposit, interest_rate, amount_months):
#     s = (deposit * ((1+(interest_rate/(12*100)))**amount_months))-deposit
#     return s
#     # вычислить прибыль
# x = float(input())
# k = float(input())
# n = int(input())
# # вычислить прибыль с помощью функции
# s = compute_income(x, k, n)
# #вывести результат
# print(round(s))

# def compute_income(deposit, interest_rate, amount_months):
#     z = (deposit * ((1 + (interest_rate / (12 * 100))) ** amount_months)) - deposit  # вычислить прибыль
#     return z
#
# k = float(input())  # занести процент вклада
# n = int(input())  # занести количество месяцев
# s = float(input())  # занести прибыль
#
# for x in range(1000, 260000):
#     # вычислить прибыль для вклада x с помощью функции  compute_income(x, ..., ...)
#     income = compute_income(x, k, n)
#     if round(income) == s:
#         print(x)

# import math
# def f_x(x):
#     try:
#         y = 1 / (x + 1) + x / (x - 3)
#     except:
#         y = math.inf
#     return y
# s = input(("x_list = "))
# str_list = s.split()
# x_list = [float(x) for x in str_list]
# for x in x_list:
#     y = f_x(x)
#     print("f(%4.2f) = %6.3f" % (x,  y))

# a = float(input("a = "))
# b = float(input("b = "))
# n = int(input("n = "))
# if n < 0 or a >= b:
#     print("Ошибочные входные данные")
# else:
#     h = (b - a) / (n - 1)
# x_list = [a + i * h for i in range(n)]
# f_list = [f_x(x) for x in x_list]
# for i in range(n):
#         print ("%4.1f : %6.3f" % (x_list[i], f_list[i]))
#    # вывод шапки таблицы
# print("-" * 17)
# print ("| %4s | %6s |" % ("x", "f(x)"))
# print("-" * 17)
# # вывод содержимого таблицы
# for i in range(n):
#     print ("| %4.1f | %6.3f |" % (x_list[i], f_list[i]))
# # вывод подчеркивания
# print("-" * 17)

