#43.Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]   count()
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = [i for i in my_list if my_list.count(i) > 1 ]

print(new_list)

res = [x for x in my_list + new_list if x not in my_list or x not in new_list]
print(res)

# Использованы list comprehension