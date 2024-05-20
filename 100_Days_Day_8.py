#################
# Caesar Cipher #
#################

# ASCII art for beginning banner/logo (courtesy of https://replit.com/@appbrewery/caesar-cipher-4-start#art.py).
banner_logo = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''

# Start of program.
print(banner_logo)
print("Do you need to encrypt a message, or do you need to decrypt one?\n")

# Choose to encrypt or decrypt.
encode_or_decode_choice = str(input("Type \"encode\" to encrypt, or type \"decode\" to decrypt: \n").lower())
if encode_or_decode_choice != "encode" and encode_or_decode_choice != "decode":
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
        for char in written_message:
            if char in alphabet_list:
                letter_position = alphabet_list.index(char)
                new_letter = alphabet_list[letter_position + num]
                new_message += new_letter
            else:
                new_message += char
        print("Here is the encoded result:\n" + new_message)
    elif choice == "decode":
        for char in written_message:
            if char in alphabet_list:
                letter_position = alphabet_list.index(char)
                new_letter = alphabet_list[letter_position - num]
                new_message += new_letter
            else:
                new_message += char
        print("Here is the decoded result:\n" + new_message)

# Calling the encryption/decryption function.
caesar_cipher(choice = encode_or_decode_choice, written_message = message, num = shift_number)

# End of program.
print()
print("Type \"yes\" if you want to go again; otherwise, type \"no\": ") # TEST CODE