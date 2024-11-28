import os
import time

directory = "."#Так как в разных операционных системах разная схема расположения папок,
               # тестировать проще всего в папке проекта

for root, dirs, files in os.walk(directory):# Обходим директорию с помощью os.walk
    for file in files:
        filepath = os.path.join(root, file)# Формируем полный путь к файлу
        filetime = os.path.getmtime(filepath)# Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))# Форматируем время
        filesize = os.path.getsize(filepath)# Получаем размер файла
        parent_dir = os.path.dirname(filepath)# Получаем родительскую директорию файла

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')