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

# Encryption function.
def encrypt(plaintext, num):
    encoded_message = ""
    for letter in plaintext:
        plaintext_letter_position = alphabet_list.index(letter)
        ciphertext_letter = alphabet_list[plaintext_letter_position + num]
        encoded_message += ciphertext_letter
    print("Here is the encoded result:\n" + encoded_message)

# Decryption function.
def decrypt(ciphertext, num):
    decoded_message = ""
    for letter in ciphertext:
        ciphertext_letter_position = alphabet_list.index(letter)
        plaintext_letter = alphabet_list[ciphertext_letter_position - num]
        decoded_message += plaintext_letter
    print("Here is the decoded result:\n" + decoded_message)

# Encrypt or decrypt based off the user's decision.
if encode_or_decode_choice == "encode":
    encrypt(plaintext = message, num = shift_number)
elif encode_or_decode_choice == "decode":
    decrypt(ciphertext = message, num = shift_number)

# End of program.
print()
print("Type \"yes\" if you want to go again; otherwise, type \"no\": ") # TEST CODE