# Vignère Cipher
# You already implemented a solution for the Caesar cipher in week 3. 
# As this cipher is quite weak, let's turn to another cipher, the Vignère cipher.

# Like the Caesar cipher, the Vignère cipher is a simple substitution algorithm, that means, 
# each letter is replaced by another letter. In the Caesar cipher, each letter is shifted the same number of times. 
# And this number is the key. In Vignère these number of shifts change from letter to letter. 
# The number of shifts are given by a keyword which is repeated until it matches the length of the text to be encrypted.

# For simplification we assume, that only letters are encrypted and that we only have to deal with lower case letters. Let's have a look at the following example:

# In the first line there is the clear text.
# In the second line there is the repeated keyword random.
# In the third line the letter from the keyword is replaced by it's position in the alphabet (a: 0, b: 1, c: 2, … z: 25). 
# As r is on position 17, there is a 17 in the first position of the third row. 
# This position determines how often the corresponding letter from the clear text has to be shifted.
# In the fourth line you can see the secret text. 
# The first letter p from the clear text is shifted 17 times and results in g (as the end of the alphabet is already reached after 11 shifts, one starts again at the beginning of the alphabet). The second letter y is shifted 0 times as the a from random is at position 0 of the alphabet. Thus, this y is mapped to y. Important: The blank is not shifted as it is no letter. However the repetition of the keyword in line two is not influenced by that.
                                       
# Clear Text	p	y	t	h	o	n	 	i	s	 	b	e	a	u	t	i	f	u	l
# Keyword	r	a	n	d	o	m	r	a	n	d	o	m	r	a	n	d	o	m	r
# Position	17	0	13	3	14	12	17	0	13	3	14	12	17	0	13	3	14	12	17
# Secret Text	g	y	g	k	c	z	 	i	f	 	p	q	r	u	g	l	t	g	c


# Your Task
# Implement a program, that gets a text as input and in addition a keyword, which is the number of shifts.

# Implement a function encrypt_letter(), that gets a character and the key as input. 
# The return value will be the encrypted character.
# Implement a function calculate_shifts(), 
# that gets a letter as input parameter and returns the position of this letter in the alphabet (starting with a at position 0):
# Implement a function encrypt_text(), 
# that gets a text and a keyword as input and returns the encrypted text. 
# This function calls both calculate_shifts()and encrypt_letter()



def calculate_shifts(letter):
    return ord(letter) - ord('a')


def encrypt_letter(char, key_shift):
    if not char.isalpha():
        return char
    shifted = (ord(char) - ord('a') + key_shift) % 26
    return chr(ord('a') + shifted)


def encrypt_text(plain_text, key_word):
    plain_text = plain_text.lower()
    key_word = key_word.lower()
    encrypted = ""
    key_index = 0
    key_length = len(key_word)
    for char in plain_text:
        key_char = key_word[key_index % key_length]
        shift = calculate_shifts(key_char)
        encrypted += encrypt_letter(char, shift)
        key_index += 1
    return encrypted


user_text = input("Which text should be encrypted: ")
user_keyword = input("Which keyword should be used? ")
print(encrypt_text(user_text, user_keyword))