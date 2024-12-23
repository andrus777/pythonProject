from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = dict()
    file = open(file_name, 'w', encoding = 'utf-8')
    string_num = 1
    for s in strings:
        byte_num = file.tell()
        file.write(s +'\n')
        strings_positions[(string_num, byte_num)] = s
        string_num += 1
        byte_num = file.tell()
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

