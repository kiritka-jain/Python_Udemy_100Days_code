import random
import art


def choose_random_card():
    """Chooses the random card from the given list of the cards."""

    deck = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen']
    card = random.choice(deck)
    return card


def get_card_value(card):
    """
    Gives the integer value of the card drawn
    :param card: str or int
    :return: int
    """
    if type(card) == int:
        return card
    if type(card) == str and card != 'ace':
        return 10
    if card == 'ace':
        return 11


def check_card_sum(card_1, card_2):
    """
    Gives the total sum of both the cards.
    :param card_1: int or str
    :param card_2: int or str
    :return: int
    """
    card_val_1 = get_card_value(card_1)
    card_val_2 = get_card_value(card_2)
    card_sum = card_val_1 + card_val_2
    if card_sum > 21 and (card_1 == 'ace' or card_2 == 'ace'):
        return card_sum - 10
    return card_sum


def add_new_card(prev_sum):
    """
    Add new card and gives total sum for all the cards.
    :param prev_sum: int
    :return: int
    """
    new_card = choose_random_card()
    new_card_val = get_card_value(new_card)
    new_sum = prev_sum + new_card_val
    print(new_sum)
    return new_sum


def compare_sums(player_sum, computer_sum):
    """
    Compares the total sum of cards for both the player and the computer.
    :param player_sum: int
    :param computer_sum: int
    :return: str
    """

    if computer_sum < player_sum < 22:
        return 'You Win'
    if player_sum < computer_sum < 22:
        return "You lose"
    if player_sum == computer_sum:
        return "Game Draw"
    if computer_sum > 21:
        return "You Win"
    if player_sum > 21:
        return "You lose"


def hit_or_stand(player_sum, computer_sum):
    hit = input("Do you want to hit? press 'y' for yes and 'n' for no ")
    if hit == 'y':
        player_new_sum = add_new_card(player_sum)
        return compare_sums(player_new_sum, computer_sum)

    if player_sum > computer_sum and computer_sum < 17:
        new_computer_sum = add_new_card(computer_sum)
        return compare_sums(player_sum, new_computer_sum)

    if player_sum > computer_sum:
        return "You win"

    return "You lose"


def game_blackjack(player_sum, computer_sum):
    if (player_sum == 21 and computer_sum == 21) or player_sum == computer_sum:
        return 'Game Draw'
    if player_sum == 21 and computer_sum < 21:
        return "You Win!"
    if (player_sum < 21 and computer_sum == 21) or player_sum > 21:
        return 'You lose'

    return hit_or_stand(player_sum, computer_sum)


def play_game():
    print(art.logo)

    player_card_1 = choose_random_card()
    player_card_2 = choose_random_card()
    computer_card_1 = choose_random_card()
    computer_card_2 = choose_random_card()

    player_total = check_card_sum(player_card_1, player_card_2)
    computer_total = check_card_sum(computer_card_1, computer_card_2)
    print(f"Computer's first card is {computer_card_1}")
    print(f"Your cards are: {player_card_1},{player_card_2} total sum = {player_total}")

    print(game_blackjack(player_total, computer_total))
    print(f"computer's second card is{computer_card_2}")


if __name__ == '__main__':
    play_game()
