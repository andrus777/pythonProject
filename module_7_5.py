import os
import time

directory = 'd:\\Диалог'
tab = "   "

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        print(f'{tab}Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

    for dir in dirs:
        dirpath = os.path.join(root, file)
        print(f'{tab}Обнаружена папка: {dir}, Путь: {os.path.join(root, dir)}, Размер: {os.path.getsize(os.path.join(root, dir))} байт, '
              f'Время изменения: {time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(dirpath)))}, Родительская директория: {os.path.dirname(dirpath)}')
    tab = tab + "   "
