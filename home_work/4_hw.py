# Задача 1
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rectangle_area(self):
        print(f'Площать: {self.width * self.height}')

    def rectangle_perimeter(self):
        print(f'Периметр: {2 * (self.width + self.height)}')

rec_1 = Rectangle(10, 20)
rec_2 = Rectangle(20, 40)
rec_3 = Rectangle(30, 35)

print('Прямоугольник 1')
rec_1.rectangle_area()
rec_1.rectangle_perimeter()
print('Прямоугольник 2')
rec_2.rectangle_area()
rec_2.rectangle_perimeter()
print('Прямоугольник 3')
rec_3.rectangle_area()
rec_3.rectangle_perimeter()
print('\n')

# Задача 2

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'Cложение: {self.a + self.b}')

    def multiplication(self):
        print(f'Умножение: {self.a * self.b}')

    def division(self):
        print(f'Деление: {self.a // self.b}')

    def subtraction(self):
        print(f'Вычитание: {self.a - self.b}')

result = Math(10, 6)

result.addition()
result.multiplication()
result.division()
result.subtraction()
print('\n')

# Задача 3

class Button:

    def __init__(self, text, typ='Кнопка', loc=''):
        self.text = text
        self.typ = typ
        self.loc = loc

    def click(self):
        return 'Клик по кнопке {}'.format(self.text)

text_box_button = Button('"Text Box"')
check_box_button = Button('"Check Box"')
radio_button = Button('"Radio Button"')
web_tables_button = Button('"Web Tables"')
buttons_button = Button('"Buttons"')
links_button = Button('"Links"')
broken_links_button = Button('"Broken links - Images"')
upl_and_dow_button = Button('"Upload and Download"')
dy_properties_button = Button('"Dynamic Properties"')
practice_form = Button('"Practice Form"')
print('--Elements--')
print(text_box_button.click())
print(check_box_button.click())
print(radio_button.click())
print(web_tables_button.click())
print(buttons_button.click())
print(links_button.click())
print(broken_links_button.click())
print(upl_and_dow_button.click())
print(dy_properties_button.click())

print('--Forms--')
print(practice_form.click())