# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
from learning_tasks.GeekBrains.lesson_5.task_4 import cd,ls,make_dir


def main():


    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    action = input()
    if action == '1':

        dir_name=input('Введите путь ')
        try:
            cd(dir_name)
        except FileNotFoundError:
            print('Путь не найден')
        except OSError:
            print('неверно введен путь')
    elif action == '2':
        ls()
    elif action == '3':
        del_folder=input('Имя папки для удаления')
        try:
            os.rmdir(f'{del_folder}')
            print(f'Папка {del_folder} удалена')
        except FileNotFoundError:
            print('Невозможно удалить. Папка не найдена')

    elif action == '4':
        dir_name = input('Имя папки ')
        make_dir(dir_name)

    else:
        main()



main()
