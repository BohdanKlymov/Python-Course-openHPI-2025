# Using this substitutions, a plain text can be encrypted:

# Plaintext: programming python is fun!
# Encrypted text: uwtlwfrrnsl udymts nx kzs!
# Your task for the assignment is to implement a Caesar cipher with a shift of 5. 
# The program should ask the user for a plain text sentence and print the encrypted text.

encryption = {
    "a":"f","b":"g","c":"h","d":"i","e":"j","f":"k","g":"l","h":"m",
    "i":"n","j":"o","k":"p","l":"q","m":"r","n":"s","o":"t","p":"u",
    "q":"v","r":"w","s":"x","t":"y","u":"z","v":"a","w":"b","x":"c",
    "y":"d","z":"e"
}

text_input = list(input("Please enter a sentence: "))

for i, letter in enumerate(text_input):
    text_input[i] = encryption.get(letter, letter)

encrypted = "".join(text_input)
print(f"The encrypted sentence is: {encrypted}")