from Day_16.Mpney_machine import MoneyMachine
from coffee_machine import CoffeeMachine


if __name__ == "__main__":
    switch = input("coffee machine mode: 'ON' or 'OFF")
    machine = CoffeeMachine(switch)
    while machine.status == 'ON':
        print(machine.status)
        machine.display_menu()
        machine.process_choice()

