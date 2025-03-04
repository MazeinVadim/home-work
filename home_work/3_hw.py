# Задача 1
def largest_number(num_1, num_2):
    print(max(num_1, num_2))

largest_number(89, 168)


# Задача 2
def number_difference(num_1, num_2):
    if num_1 - num_2 == 135 or num_2 - num_1 == 135 or num_1 - num_2 == -135 or num_2 - num_1 == -135:
        print('YES')
    elif num_1 + num_2 == 135 or num_2 + num_1 == 135 or num_1 + num_2 == -135 or num_2 + num_1 == -135:
        print('YES')
    else:
        print('NO')

number_difference(-335, 205)


# Задача 3
def seasons(num):
    if num in range(1, 3) or num == 12:
        print('Зима')
    elif num in range(3, 6):
        print('Весна')
    elif num in range(6, 9):
        print('Лето')
    elif num in range(9, 12):
        print('Осень')
    else:
        print('Введите число от 1 до 12')

seasons(1)

#Задача 4
def numbers_more(num_1, num_2, num_3):
    if num_1 > 10 and num_2 > 10 and num_3 > 10:
        print('YES')
    else:
        print('NO')

numbers_more(11, 15, 14)

#Задача 5
def numbers_positive(num_1, num_2, num_3, num_4, num_5):
    pos_int = 0
    if num_1 > 0:
        pos_int += 1
    if num_2 > 0:
        pos_int += 1
    if num_3 > 0:
        pos_int += 1
    if num_4 > 0:
        pos_int += 1
    if num_5 > 0:
        pos_int += 1

    print(pos_int)

numbers_positive(1, 2, 0, 0, 1)

#Задача 6
def number_days(year, month):
    days = (year * 12 * 29) + (month * 29)
    print(days)

number_days(7, 6)