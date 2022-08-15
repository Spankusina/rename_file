import os

def rename():
    i = 0
    for adress, dirs, files in os.walk(path):
        for file in files:
            if '_compressed' in file:
                full = os.path.join(adress, file)
                new_file = file.replace('_compressed', '')
                new_full = os.path.join(adress, new_file)
                os.rename(full, new_full)
                i += 1
    return i


path = input('Введите адрес папки ')
#path = r'E:\Programm\rename_files\files'


count = rename()
print('Переименовано ', count, 'файлов')





