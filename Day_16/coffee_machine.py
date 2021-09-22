from Day_16.Mpney_machine import MoneyMachine
from Day_16.menu import Menu


class CoffeeMachine:

    def __init__(self, status, water=300, milk=200, coffee=75):
        self.status = status
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.menu = Menu()
        self.choice = None
        self.money_machine = MoneyMachine()

    def press_power_button(self):
        if self.status == 'ON':
            self.status = 'OFF'
        else:
            self.status = 'ON'

    def display_menu(self):
        print(self.menu.print_menu())
        self.__get_choice()

    def __get_choice(self):
        choice = int(input("What do you want to have?\n"))
        self.choice = choice

    def process_choice(self):
        if self.choice == 5:
            return self.print_report()
        self.money_machine.insert_coins()
        if not self.money_machine.is_inserted_money_sufficient(self.choice):
            print(f"Insufficient amount , your money ${self.money_machine.refund_money()}is refunded")
            return None
        if not self.check_resources():
            print(f"Insufficient resources , your money ${self.money_machine.refund_money()}is refunded")
            return None
        print(f"Here is: ${self.money_machine.money_to_return()} in change.")
        self.__make_choice()
        print(f"Enjoy your coffee")
        self.money_machine.add_profit()

    def check_resources(self):
        milk_needed, water_needed, coffee_needed = self.menu.get_quantity(self.choice)
        if (self.milk >= milk_needed) and (self.water >= water_needed) and (self.coffee >= coffee_needed):
            return True
        return False

    def __make_choice(self):
        milk_qty, water_qty, coffee_qty = self.menu.get_quantity(self.choice)
        self.__update_qty(milk_qty, water_qty, coffee_qty)

    def print_report(self):
        print(f"Water:{self.water}\n"
              f"Milk:{self.milk}\n"
              f"Coffee:{self.coffee}\n"
              f"profit:{self.money_machine.print_profit()}")

    def __update_qty(self, milk_qty, water_qty, coffee_qty):
        self.milk -= milk_qty
        self.water -= water_qty
        self.coffee -= coffee_qty
