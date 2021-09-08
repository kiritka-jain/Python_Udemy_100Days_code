import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ['apple', 'mango', 'strawberry']
word = random.choice(word_list)
word_len = len(word)
blanks = []
matched_letter = ''
life_lines = 6
chances = 0
hangman_index = 1
for _ in range(word_len):
    blanks.append("_")
print(blanks)

game_over = False


def letter_matching(player_letter):
    for i in range(word_len):
        if player_letter == word[i]:
            blanks[i] = player_letter
    return blanks


while chances < word_len and life_lines > 0:
    if '_' not in blanks:
        game_over = True
        print("Game Over!")
        break
    else:
        player_letter = input("Enter a letter.").lower()
        chances += 1
        if player_letter not in word:
            life_lines -= 1
            print(HANGMANPICS[hangman_index])
            hangman_index += 1
        matched_letter = letter_matching(player_letter)
        print(matched_letter)
if '_' not in matched_letter:
    print("You Win!:")
else:
    print('You Lose!')
