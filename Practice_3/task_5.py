#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input())
def func_fib_minus(n):
    f1 = 1
    f2 = 1
    list = []
    while n > -1:
        f2, f1 = f1, f2 - f1
        list.append(f1)
        n -= 1
    return list[::-1]
#print(func_fib_minus(n))
def func_fib(n):
    f1 = 1
    f2 = 1
    list = [1, 1]
    while n > 2:
        f1, f2 = f2, f2 + f1
        list.append(f2)
        n -= 1
    return list
#print(func_fib(n))

print(func_fib_minus(n) + func_fib(n))


