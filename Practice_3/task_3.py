#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

'''def find_diff(mynums):
    nums = [round(x - int(x), 3) for x in (mynums)]
    return max(nums) - min(nums)

print(find_diff(list))'''
for i in list:
    # функцией isinstance, она проверяет тип данных
    if isinstance(i, int):
        list.remove(i)

def func_str(list):
    j = 0
    list_float = []
    while len(list) > j:
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
    return round((max_ - min_), 3)
print(min_func(arr))

''' Но вообще, операция list[j]//1 (она в строке 14 применяется) - очень каверзная. Я вот Вашу программу запускал и она
выдала немного не тот результат, который должен быть. С дробными числами не всё так просто.'''


'''j = 0
list_float = []
while len(list) >j:
    list_float.append(str(list[j]))
    j += 1
print(list_float)
i = 0

while len(list_float) > i:
    j = 0
    while len(list_float[i]) > j:
        print(list_float[i][j], end =  ' ')
        j += 1
    i += 1'''