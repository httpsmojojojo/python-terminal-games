import random

MAX_TRIES = 10
no_guess = 0

# List of words
words = ["goodmorning", "python", "programming", "computer", "keyboard", "internet", "algorithm"]

# Select a random word from the list
word = random.choice(words)
word = word.lower()
print(word)

while True:
    key = input("Guess letter: ")
    if key in word:
        print(word + " contains " + key)
        word = word.replace(key, "")
        print(len(word))
        if len(word) == 0:
            print("You win")
            break
    else:
        print("wrong")
        no_guess += 1
        if no_guess >= MAX_TRIES:
            print("You lose")
            break
