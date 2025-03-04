def task_func(a = (1, 2, 3, 4)):
    return a[1]

print(task_func(), '\n')


def compute_surface(radius, pi=3.14159):
    return pi * radius * radius

print(compute_surface(2), '\n')


def string_length(s: str = '') -> int:
    return len(s)

print(string_length('String length'), '\n')


def too_string_length(a: list, b: list) -> int:
    return (max(len(a), len(b)))

print(too_string_length([1, 2, 3], ['Mazein', 'Ivanov', 'Ilichev', 'Ievlev']), '\n')

def append_list(my_list: list):
    my_list.append('test')
    return my_list

print(append_list(['one', 2, 3]), '\n')

def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print(sum_list([1, 2, 3]))

