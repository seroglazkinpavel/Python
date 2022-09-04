#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

input_data = 'C:\\Users\\MSI\\PycharmProjects\\Python\\Python\\Practice_5\\42input_data.txt'
output_data = 'C:\\Users\\MSI\\PycharmProjects\\Python\\Python\\Practice_5\\42output_data.txt'
with open(input_data, 'r') as data:
    my_input_data = data.read()

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        # Если предыдущие и текущие символы не совпадают...
        if char != prev_char:
            # ...затем добавим количество и символ в нашу кодировку
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Или увеличим наш счетчик, если символы действительно совпадают
            count += 1
    else:
        # Завершите кодировку
        encoding += str(count) + prev_char
        return encoding
encoded_val = rle_encode(my_input_data)
print(encoded_val)

with open(output_data, 'r') as data:
    my_input_data = data.read()

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # Если символ является числовым...
        if char.isdigit():
            # ...добавим его в нашу строку
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decoded_val = rle_decode('6A1F2D7C1A17E')
print(decoded_val)
