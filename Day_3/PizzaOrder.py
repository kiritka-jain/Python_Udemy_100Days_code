def pizza_bill_calculator(size,pepporni,cheese):
    bill_amount = 0
    add_on = 0
    if size == 'S':
        bill_amount = 15
    elif size == "M":
        bill_amount = 20
    else:
        bill_amount = 25
    if pepporni =="Y":
        if size == 'S':
            add_on += 2
        else:
            add_on += 3
    if cheese =="Y":
        if size == 'S':
            add_on += 2
        else:
            add_on += 3
    total_bill = bill_amount+add_on
    return total_bill



print("Welcome to the python pizza's delivery")
pizza_size = input("What size pizza do you want? S, M or L")
add_pepperoni = input("Do you want to add the pepperoni? Y or N")
extra_cheese = input("Do you want to add the extra cheese? Y or N")
print(pizza_bill_calculator(pizza_size,add_pepperoni,extra_cheese))
