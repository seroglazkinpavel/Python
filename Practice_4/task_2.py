#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

from random import randint
n = 10
num_list = [randint(0, n) for i in range (n)]
print(num_list)

my_set = [i for i in set(num_list)]
print(my_set)

