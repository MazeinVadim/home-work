# Задача 1
def task_1(age, price, name, colors, is_active):
    return type(age), type(price), type(name), type(colors), type(is_active)

print(task_1(30, 10.02, 'Vadim', ['red', 'green', 'blue'], True), '\n')


# Задача 2
def task_2(a = [1, 2, 3, 5, 8, 13, 21]):
    return a[0:3]

print('Fibonacci sequence:', task_2(), '\n')


# Задача 3
def task_3(a) -> int:
    return a ** 2

print(task_3(5))