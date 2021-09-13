import art

print(art.logo)


def add(num_1, num_2):
    result = num_1 + num_2
    return result


def sub(num_1, num_2):
    result = num_1 - num_2
    return result


def product(num_1, num_2):
    result = num_1 * num_2
    return result


def division(num_1, num_2):
    result = num_1 / num_2
    return result


calculation_process = {'+': add, '-': sub, '/': division, '*': product}
def calculator():
    calculation_continue = True
    first_num = float(input("What's the first number?"))
    while calculation_continue:
        for operations in calculation_process:
            print(operations)
        operation = input("Pick on operation:")
        second_num = float(input("What's the second number"))

        operation_to_perform = calculation_process[operation]
        final_answer = operation_to_perform(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {final_answer}")
        further_calculation = input("Type 'y' to further calculating withe the answer, or type 'n' to exit.")
        if further_calculation == 'y':
            first_num = final_answer
        else:
            calculation_continue = False
            calculator()

calculator()
