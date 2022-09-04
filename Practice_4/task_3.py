#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Необходимые материалы для выполнения задания
#Модуль itertools - сборник полезных итераторов.
#itertools.zip_longest(*iterables, fillvalue=None) - как встроенная функция zip, но берет самый длинный итератор, а более короткие дополняет fillvalue.
#символов ** соответствует ^
#itertools.chain(*iterables) создает итератор, который возвращает элементы из первой iterables, пока она не будет исчерпана, а затем переходит к следующей iterables, пока все итерируемые последовательности не будут исчерпаны.
from random import randint
import itertools

k = randint(2, 7)
#print('k =', k)
def get_ratios(k):
    ratios = [randint(0, 100) for i in range (k + 1)]
    #print('коэффициенты =', ratios)
    #Если 1 коэффициент окажется = 0
    while ratios[0] == 0:
        ratios[0] = randint(1, 100)
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    #print('количества k x =', var)
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'

    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

path = 'C:\\Users\\MSI\\PycharmProjects\\Python\\Python\\Practice_4\\file.txt'
with open(path, 'w') as data:
    data.write(polynom1)