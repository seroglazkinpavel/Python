#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
list = [2, 3, 5, 9, 3]

def my_func(list):
    s = 0
    list_1 = []
    for i in list:
        if i % 3 == 0:
            list_1.append(i)
    for i in set(list_1):
        s += i
    return s

print(my_func(list))

