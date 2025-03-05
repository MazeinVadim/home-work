class A:

    def __init__(self, x=10):
        self.x = x

class B(A):

    def __init__(self):
        super().__init__() # Вызываем инициализатор родительского класса, чтобы установить self.x
        self.y = self.x + 5

# Пример использования
a = A()
print(f'Объект класса А: x = {a.x}')

b = B()
print(f'Объект класса B: y = {b.y}')

print(f'Cумма объектов классов A и B: {a.x + b.y}')