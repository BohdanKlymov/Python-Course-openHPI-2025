# One of the nice features of Python is that it supports Unicode. Therefore it is possible to use emojis just like other characters in strings. 
# In this exercise you will use this feature to build an emoji translator.

# Below is a dictionary that maps English terms to Emojis (broken into multiple lines for better readability).

# Use this dictionary to build a program that:

# Reads a sentence from the user. Replaces all the words in the sentence with the corresponding Emoji.

emoji_dict = {
        "happy": "😃",
        "heart": "😍",
        "rotfl": "🤣",
        "smile": "😊",
        "crying": "😭",
        "kiss": "😘",
        "clap": "👏",
        "grin": "😁",
        "fire": "🔥",
        "broken": "💔",
        "think": "🤔",
        "excited": "🤩",
        "boring": "🙄",
        "winking": "😉",
        "ok": "👌",
        "hug": "🤗",
        "cool": "😎",
        "angry": "😠",
        "python": "🐍",
}

sentence = input("Please enter a sentence: ")
words = sentence.split()
output = [emoji_dict.get(word, word) for word in words]
print(" ".join(output))