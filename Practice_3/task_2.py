#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

num_list = [2, 3, 4, 5, 6]
def my_func(num_list):
    n = 1
    num_list_1 = []
    while len(num_list) > n:
        num_list_1.append(num_list[n - 1] * num_list[-n])
        n += 1
    return num_list_1

temp = []
for x in my_func(num_list):
    if x not in temp:
        temp.append(x)
        ints_list = temp
print(temp)