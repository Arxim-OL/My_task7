# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    num_str = 0
    for i in strings:
        file.tell()
        num_str += 1
        strings_positions [(num_str, file.tell())] = i
        file.write(f'{i}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)