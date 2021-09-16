import art
import random
import game_data


def entry_generator():
    entry = random.choice(game_data.data)
    return entry


def entry_list(entry):
    entry_list = []
    for key in entry:
        if key != 'follower_count':
            entry_list.append(entry[key])
    return entry_list


def compare_entries(entry_1, entry_2):
    if entry_1['follower_count'] > entry_2['follower_count']:
        return entry_1
    if entry_1['follower_count'] < entry_2['follower_count']:
        return entry_2


def player_choice(player_answer, entry_1, entry_2):
    if player_answer == 'A':
        return entry_1
    return entry_2


def run_game():
    game_continue = True
    score = 0
    entry_1 = entry_generator()
    while game_continue:
        entry_2 = entry_generator()
        print(art.logo)
        print(f"Compare A: {entry_list(entry_1)}")
        print(art.vs)
        print(f"Against B: {entry_list(entry_2)}")
        player_answer = input("Who has more followers? Type 'A' or 'B'")
        player_option = player_choice(player_answer, entry_1, entry_2)
        higher_followers = compare_entries(entry_1, entry_2)
        if player_option != higher_followers and higher_followers is not None:
            game_continue = False
            print(f"You guessed it wrong and your score is {score}")
            return game_continue
        score += 1
        entry_1 = higher_followers


if __name__ == '__main__':
    run_game()
