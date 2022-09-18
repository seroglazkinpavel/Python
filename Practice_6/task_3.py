#27.Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел

my_str = '45 74 21 90'.split(' ')
print(my_str)
my_list = list(map(int, my_str))
print(my_list)
max_numb = max(my_list)
min_numb = min(my_list)
print(f'max = {max_numb} и min = {min_numb}')

#Использование функции map