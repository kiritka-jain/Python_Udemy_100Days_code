class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.nickel_qty = 0
        self.dime_qty = 0
        self.quarter_qty = 0
        self.penny_qty = 0
        self.inserted_val = 0
        self.choice = None
        self.drink_val = {
            1: 1.0,
            2: 3.0,
            3: 2.5,
            4: 1.5
        }

    def insert_coins(self):
        self.nickel_qty = int(input("Enter the nickel coins\n"))
        self.dime_qty = int(input("Enter the dime coins\n"))
        self.quarter_qty = int(input("Enter the quarter coins\n"))
        self.penny_qty = int(input("Enter the penny coins\n"))

    def __inserted_coin_value(self):
        quarter = 0.25
        dime = 0.10
        nickle = 0.05
        penny = 0.01
        self.inserted_val = (nickle * self.nickel_qty) + (dime * self.dime_qty) + \
                            (quarter * self.quarter_qty) + (penny * self.penny_qty)
        return self.inserted_val

    def is_inserted_money_sufficient(self, choice):
        total_inserted_value = self.__inserted_coin_value()
        self.choice = choice
        if total_inserted_value >= self.drink_val[self.choice]:
            return True
        return False

    def money_to_return(self):
        total_inserted_value = self.__inserted_coin_value()
        drink_value = self.drink_val[self.choice]
        if total_inserted_value >= drink_value:
            balance = total_inserted_value - drink_value
            return round(balance,2)

    def refund_money(self):
        return self.__inserted_coin_value()

    def add_profit(self):
        profit = self.drink_val[self.choice]
        self.profit += profit

    def print_profit(self):
        return self.profit




