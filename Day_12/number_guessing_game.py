import random


def guess_a_number(num_to_compare):
    guessed_number = int(input("Guess a number"))
    if guessed_number == num_to_compare:
        return "You have guessed the correct number", False
    if guessed_number > num_to_compare:
        return "Too high", True
    return "Too low.", True


def get_chances(difficulty):
    if difficulty == 'hard':
        return 5
    return 10


def run_game():
    print("Welcome to number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    comp_number = random.randint(1, 101)
    game_continue = True
    difficulty = input("Choose a difficulty? 'easy' or 'hard'.")
    max_chance = get_chances(difficulty)
    for chances in range(1, max_chance + 1):
        if not game_continue:
            print("Game ends")
            return
        statement, game_continue = guess_a_number(comp_number)
        print(statement)
        print(f"You have {max_chance - chances} attempts left.")
    print(f"The number was: {comp_number}")


if __name__ == '__main__':
    run_game()
