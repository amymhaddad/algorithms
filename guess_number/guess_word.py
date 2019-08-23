"""Pick a random word and have the user try to guess it. Provide feedback on the guessed word"""
import random

WORD_CHOICES = ["a", "be", "cat", "dog", "elf"]
RANDOM_WORD = random.choice(WORD_CHOICES)


def guess_word(WORD_CHOICES, RANDOM_WORD):
    """See if user can guess the random word and provide feedback on their guess"""
    print("Here are the list of words: ")
    for word in WORD_CHOICES:
        print(word)

    print()

    while True:
        user_guess = input("Guess a word from the list of words: ")
        if user_guess == RANDOM_WORD:
            return "You guessed it!"

        elif RANDOM_WORD > user_guess:
            print("Next time, choose a word that's later in the list.\n")

        else:
            print("Next time, choose a word that's earlier in the list.\n")


print(guess_word(WORD_CHOICES, RANDOM_WORD))
