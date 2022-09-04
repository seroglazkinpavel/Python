#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# исходная строка
line = 'осталабвись строки и перабвенос слова перекрабвесток пабвереоборудование'

# делим строку на слова
'''words = line.split(' ')
print(words)
# фрагмент, по которому будем удалять слова
fragment = 'абв'
# новый список оставшихся слов
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
print(new_words)
# собираем строку используя в качестве разделителя пробел
print(' '.join(new_words))'''

# Исправил с учетом вашего замечания

words = line.split(' ')
print(words)
fragment = 'абв'

new_words = [word for word in words if fragment not in word]
print(new_words)

print(' '.join(new_words))