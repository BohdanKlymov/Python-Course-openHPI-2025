# A Caesar cipher is a simple encryption technique. 
# The encryption using a Ceasar cipher replaces a letter in 
#     the plain text with a letter that is a fixed number down in the alphabet. 
# For example, with a shift of 5 the following substitutions would take place:

# a → f
# b → g
# c → h
# …
# v → a
# w → b
# …
# z → e
# Using this substitutions, a plain text can be encrypted:

# Plaintext: programming python is fun!
# Encrypted text: uwtlwfrrnsl udymts nx kzs!
# Your task for the bonus exercise is the implementation of a Caesar cipher with a variable shift. 
# The program should ask the user for a number of characters for the shift first. 
# Next the program should ask the user for a plain text sentence and print the encrypted text.

alphabet = "abcdefghijklmnopqrstuvwxyz"

shift_input = input("Please enter the number of places to shift: ")

if not shift_input.isdecimal():
    print("You need to enter a number between 0 and 25!")
else:
    shift = int(shift_input)
    if shift < 0 or shift > 25:
        print("You need to enter a number between 0 and 25!")
    else:
        sentence = input("Please enter a sentence: ")

        sentence = sentence.lower()
        encrypted_sentence = ""

        for char in sentence:
            if char in alphabet:
                new_index = (alphabet.find(char) + shift) % 26
                encrypted_sentence += alphabet[new_index]
            else:
                encrypted_sentence += char

        print("The encrypted sentence is:", encrypted_sentence)