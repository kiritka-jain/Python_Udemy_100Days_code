class Menu:
    def __init__(self):
        self.menu = {
            1: 'milk',
            2: 'cappuccino',
            3: 'latte',
            4: 'espresso',
            5: 'report'
        }

    def print_menu(self):
        return self.menu

    def get_quantity(self, choice):
        if choice == 1:
            milk_qty = 100
            water_qty = 0
            coffee_qty = 0
            return milk_qty, water_qty, coffee_qty
        if choice == 2:
            milk_qty = 50
            water_qty = 250
            coffee_qty = 24
            return milk_qty, water_qty, coffee_qty
        if choice == 3:
            milk_qty = 150
            water_qty = 200
            coffee_qty = 24
            return milk_qty, water_qty, coffee_qty
        if choice == 4:
            milk_qty = 0
            water_qty = 50
            coffee_qty = 18
            return milk_qty, water_qty, coffee_qty
