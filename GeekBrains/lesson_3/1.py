# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1 Создайте функцию, принимающую на вход Имя, возраст и город проживания человека Функция должна
# возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# def main(name, age, city):
#     return f'{name}, {age} год(а), проживает в городе {city}'
#
#
# if __name__ == '__main__':
#
#     result = main(input('Введите имя'), input('Введите возраст'), input('Введите город проживания'))
#     print(result)

print((lambda name,age,city:f'{name}, {age} год(а), проживает в городе {city}')
      (input('Введите имя'), input('Введите возраст'), input('Введите город проживания')))