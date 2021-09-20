# Coffee Machine


import flavours


def machine_is_on():
    switch = input("Do you want to turn on the coffee machine? 'yes' or 'No'")
    if switch == 'yes':
        return True
    return False


def coin_value(total_penny, total_dime, total_nickel, total_quarter):
    penny = 0.01
    dime = 0.1
    nickel = 0.05
    quarter = 0.25
    total = (total_penny * penny) + (total_dime * dime) + (total_nickel * nickel) + (total_quarter * quarter)
    return total


def insert_coins():
    print("Please insert coins.")
    total_penny = int(input("How many pennies?"))
    total_dime = int(input("How many dimes?"))
    total_nickel = int(input("How many nickels?"))
    total_quarter = int(input("How many quarters?"))
    total_money_inserted = coin_value(total_penny, total_dime, total_nickel, total_quarter)
    return total_money_inserted


def money_to_return(choice, total_money_inserted):
    required_flavour_cost = flavours.MENU[choice]['cost']
    if total_money_inserted >= required_flavour_cost:
        money_return = total_money_inserted - required_flavour_cost
        return money_return
    return None


def amount_sufficient_or_not(option, money_inserted):
    money_left = money_to_return(option, money_inserted)
    if money_left is not None:
        return True
    return False


def print_report(resources_left):
    for resource in resources_left:
        if resource == 'milk' or resource == 'water':
            print(f"{resource}: {resources_left[resource]}ml")
        elif resource == 'coffee':
            print(f"{resource}: {resources_left[resource]}g")
        else:
            print(f"Money: ${resources_left[resource]}")


def resource_sufficient_or_not(resources_left, required_resources):
    for resource in required_resources:
        if resources_left[resource] < required_resources[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True


def resource_calculation(initial_resources, required_resource):
    ingredients_left_dict = {}
    for ingredient in required_resource:
        ingredient_left = initial_resources[ingredient] - required_resource[ingredient]
        ingredients_left_dict[ingredient] = ingredient_left
    return ingredients_left_dict


def make_coffee(resources_left, required_resource):
    resources_left_after_coffee = resource_calculation(resources_left, required_resource)
    for resources in resources_left_after_coffee:
        resources_left[resources] = resources_left_after_coffee[resources]
    return resources_left


def add_profit(choice):
    required_flavour_cost = flavours.MENU[choice]['cost']
    flavours.resources['money'] += required_flavour_cost
    return flavours.resources['money']


def run_machine():
    resources_left = flavours.resources
    option = input("What would you like? (espresso/latte/cappuccino)")
    if option != 'report':
        money_inserted = insert_coins()
        required_resource = flavours.MENU[option]['ingredients']
        amount_ok = amount_sufficient_or_not(option, money_inserted)
        if not amount_ok:
            print("Sorry that's not enough money. Money refunded.")
            return None

        resource_ok = resource_sufficient_or_not(resources_left, required_resource)
        if not resource_ok:
            return None

        add_profit(option)
        make_coffee(resources_left, required_resource)
        if money_to_return(option, money_inserted):
            change_to_return = money_to_return(option, money_inserted)
            print(f"Here is ${change_to_return} in change.")
        print(f"Here is your {option}☕ Enjoy!")
        return None

    if option == 'report':
        return print_report(resources_left)


if __name__ == '__main__':
    while machine_is_on():
        run_machine()
