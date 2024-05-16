#################
# Caesar Cipher #
#################

# Start of program.
print("Do you need to encrypt a message, or do you need to decrypt one?\n")

# Choose to encrypt or decrypt.
encode_or_decode_choice = str(input("Type \"encode\" to encrypt, or type \"decode\" to decrypt: \n").lower())
if encode_or_decode_choice == "encode":
    print("encode") # TEST CODE
elif encode_or_decode_choice == "decode":
    print("decode") # TEST CODE
else:
    print("You don't follow instructions well, do you?")
    exit()

message = str(input("Type your message: \n"))
if message == "":
    print("You don't follow instructions well, do you?")
    exit()

shift_number = int(input("Type the shift number: \n"))

# print("Here is the encoded result: ")
# print("Type \"yes\" if you want to go again; otherwise, type \"no\": ")
# print("Here is the decoded result: ")

# End of program.
print()
print("There you go.") # TEST CODE