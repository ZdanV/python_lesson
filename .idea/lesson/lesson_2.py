#1.4.1
# v = float(input())
# if v <=0:
#     print("error")
# elif v <= 7.8:
#     print(0)
# elif 7.8 < v < 11.2:
#     print(1)
# elif 11.2 <= v <= 16.4:
#     print(2)
# elif v > 16.4:
#     print(3)
#
# #1.4.2
# from math import sqrt
# a = float(input())
# h = float(input())
#
# v = round((a ** 2 * h) / (4 * sqrt(3)), 3)
# s1 = (a**2 * sqrt(3)) / 4
# s2 = (3 * a / 2 ) * (sqrt(h**2 + (a**2 / 12)))
# s = round(s1+s2, 3)
#
# if v <= 0 or s <= 0:
#     print('error')
# else:
#     print(v,s)

#1.4.3
# year = int(input())
# if year < 1582:
#     print('error')
# elif year % 100 == 0 and year % 400 == 0:
#     print(366)
# elif year % 4 == 0 and year % 100 > 0:
#     print(366)
# elif year % 100 == 0:
#     print(365)
# else:print(365)

#1.4.4
# n = int(input())
# if n <= 0 or n > 99:
#     print('ошибка')
# elif n == 11 or n == 12 or n == 13 or n == 14:
#     print(n, 'рублей')
# elif n == 1 or n % 10 == 1:
#     print(n, 'рубль')
# elif n % 10 > 1 and n % 10 < 5:
#     print(n, 'рубля')
# else: print(n, 'рублей')

#1.4.5
# import math
# a = float(input())
# b = float(input())
# v = int(input())
# s = ((a ** 2) * 5) * (b /1_000) / v
# if s < 0 or a <= 0 or b <= 0 or v <=0:
#     print('error')
# else:
#     print(math.ceil(s))

#1.4.6
# h = int(input())
# m = int(input())
# s = int(input())
#
# if h < 0 or h > 11 or m < 0 or m > 59 or s < 0 or s > 59:
#     print('error')
# else:
#     degree_hour = h / 12 * 360
#     degree_minute = m / 60 * 30
#     degree_sec = s / 60 * 0.5
#
#     print(round(degree_hour + degree_minute + degree_sec, 2))










