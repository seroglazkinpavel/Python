#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
#Первый способ
'''my_float = input('Введите число :').replace('.', '')
def my_func(my_float):
    x = abs(int(my_float))
    s = 0
    while x > 0:
        s = s + x % 10
        x = x // 10
    print(f'Сумма всех цифр: {s}')
my_func(my_float)'''

# Второй способ решения
# В ваш способе добавил if для ввода отрицательных значений
num = input().replace('.', '')
if num[0] == '-':
    num = num.replace('-', '')
cifers = list(num)
int_cifer = list(map(int, cifers))
print(sum(int_cifer))