#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = 10
def my_list(n):
    list_n = []
    for i in range(1, n):
        list_n.append(i)
    return list_n
list_n =  my_list(n)
print(list_n)
def slice_list(list):
    s = 0
    i = 0
    while  len(list_n[1::2]) > i:
        s += list_n[1::2][i]
        i += 1
    return s
print(slice_list(list_n))
