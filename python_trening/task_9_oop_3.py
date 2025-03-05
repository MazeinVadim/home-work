class Soda:

    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')
        else:
            print('Обычная газировка')

drink = Soda()
drink2 = Soda('Малина')
drink.show_my_drink()
drink2.show_my_drink()
