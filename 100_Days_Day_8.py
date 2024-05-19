#################
# Caesar Cipher #
#################

# Start of program.
print("Do you need to encrypt a message, or do you need to decrypt one?\n")

# Choose to encrypt or decrypt.
encode_or_decode_choice = str(input("Type \"encode\" to encrypt, or type \"decode\" to decrypt: \n").lower())
if encode_or_decode_choice == "":
    print("You don't follow instructions well, do you?")
    exit()

# Provide your plaintext or ciphertext.
message = str(input("Type your message: \n"))
if message == "":
    print("You don't follow instructions well, do you?")
    exit()

# Choose the number of letters that you wish to shift everything by.
shift_number = int(input("Type a shift number from 1 to 25: \n"))
if shift_number < 1 or shift_number > 25:
    print("You don't follow instructions well, do you?")
    exit()

# Alphabet list (listed twice to account for large shift numbers or end letters like "z").
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Encryption/decryption function.
def caesar_cipher(choice, written_message, num):
    new_message = ""
    if choice == "encode":
        for letter in written_message:
            letter_position = alphabet_list.index(letter)
            new_letter = alphabet_list[letter_position + num]
            new_message += new_letter
        print("Here is the encoded result:\n" + new_message)
    elif choice == "decode":
        for letter in written_message:
            letter_position = alphabet_list.index(letter)
            new_letter = alphabet_list[letter_position - num]
            new_message += new_letter
        print("Here is the decoded result:\n" + new_message)

# Calling the encryption/decryption function.
caesar_cipher(choice = encode_or_decode_choice, written_message = message, num = shift_number)

# End of program.
print()
print("Type \"yes\" if you want to go again; otherwise, type \"no\": ") # TEST CODE