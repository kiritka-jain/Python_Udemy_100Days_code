message_to_encrypt = (input("Enter the message you want to encrypt:"))
shifting_number = int(input("Type the shifting number:"))
perform_action = input("What do you want to do: encrypt or decrypt")


def encrypt_message(message_to_encrypt, shifting_number):
    encrypted_string = ''
    for letter in message_to_encrypt:
        letter_ord = ord(letter)
        shifted_base = letter_ord + shifting_number
        if (122 >= shifted_base >= 97) or (90 >= shifted_base >= 65):
            encrypted_string += chr(shifted_base)
        elif (shifted_base > 122) or (shifted_base > 90):
            encrypted_string += chr(shifted_base - 26)
        else:
            encrypted_string += letter
    return encrypted_string


def decrypt_message(encrypted_message, shifting_number):
    decrypted_string = ''
    for letter in encrypted_message:
        letter_ord = ord(letter)
        rev_shifting_base = letter_ord - shifting_number
        if (97 <= rev_shifting_base <= 122) or (97 <= rev_shifting_base <= 122):
            decrypted_string += chr(rev_shifting_base)
        elif rev_shifting_base < 97 or rev_shifting_base < 65:
            decrypted_string += chr(rev_shifting_base + 26)
        else:
            decrypted_string+=letter
    return decrypted_string

if perform_action == 'encrypt':
    encrypted_message = encrypt_message(message_to_encrypt, shifting_number)
    print("The encrypted message is:"+encrypted_message)
else:
    decrypted_message = decrypt_message(message_to_encrypt, shifting_number)
    print("The decrypted message is:"+decrypted_message)
