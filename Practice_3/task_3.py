#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
for i in list:
    if i == int(i):
        list.remove(i)

def func_str(list):
    j = 0
    list_float = []
    while len(list) > j:
        list[j] - list[j]//1
        list_float.append(list[j] - list[j]//1)
        j += 1
    return list_float

arr = func_str(list)
def min_func(arr):
    min_ = arr[0]
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
            max_ = ele
        if ele < min_:
            min_ = ele
    return max_ - min_
print(min_func(arr))
