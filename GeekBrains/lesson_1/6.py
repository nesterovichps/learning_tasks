# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
import random


def run(*args):
    if args:
        first_name, last_name, age, weight = args
    else:
        first_name = input('Input First Name ')
        last_name = input('Input Last Name ')
        age = input('Input First Age ')
        weight = input('Input First Weight ')
    age = int(age)
    weight = int(weight)
    print(f'First name {first_name} Last name {last_name} Age {age} Weight {weight}.')

    if age < 30 and 50 <= weight <= 120:
        print('хорошее состояние')
    elif age > 40 and not (50 <= weight <= 120):
        print('следует обратится к врачу!')
    elif age > 30 and not (50 <= weight <= 120):
        print('следует заняться собой')
    else:
        print('медицина бессильна')


if __name__ == '__main__':
    run('Ivanov', 'Ivan', random.randrange(110), random.randrange(200))
    # run()
