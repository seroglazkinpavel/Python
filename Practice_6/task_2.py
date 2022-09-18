#29.Найти НОК двух чисел
from math import lcm

a = 6
b = 8

f = lambda a, b: lcm(a, b)
print(f(6, 8))

#Использование lambda