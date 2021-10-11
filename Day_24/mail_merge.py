PLACE_HOLDER = '[name]'
with open("Names/invited_names.txt", mode='r') as name_file:
    names = name_file.readlines()
""
with open("Letters/starting_letter.txt", mode='r') as stating_file:
    letter_content = stating_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER,striped_name)
        with open(f"./Output/letters_for_{striped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
