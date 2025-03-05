class Car:

    def __init__(self, color="Не указан", typ="Не указан", year=None):
        self.color = color
        self.type = typ
        self.year = year

    def start_engine(self):
        print("Автомобиль заведен.")

    def stop_engine(self):
        print("Автомобиль заглушен.")

    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self.year = year
            print(f"Год выпуска автомобиля установлен: {year}")
        else:
            print("Ошибка: Год выпуска должен быть положительным целым числом.")

    def set_type(self, car_type):
        if isinstance(car_type, str):
            self.type = car_type
            print(f"Тип автомобиля установлен: {car_type}")
        else:
            print("Ошибка: Тип автомобиля должен быть строкой.")

    def set_color(self, color):
        if isinstance(color, str):
            self.color = color
            print(f"Цвет автомобиля установлен: {color}")
        else:
            print("Ошибка: Цвет автомобиля должен быть строкой.")

my_car = Car()

print(f"Цвет автомобиля: {my_car.color}")
print(f"Тип автомобиля: {my_car.type}")
print(f"Год выпуска автомобиля: {my_car.year}")

my_car.set_color("Красный")
my_car.set_type("Седан")
my_car.set_year(2011)

print(f"\nЦвет автомобиля: {my_car.color}")
print(f"Тип автомобиля: {my_car.type}")
print(f"Год выпуска автомобиля: {my_car.year}")

print(my_car.start_engine())
print(my_car.stop_engine())

my_car.set_year("Восемнадцать")