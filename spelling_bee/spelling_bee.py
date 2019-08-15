"""Determine how many valid words there are in each puzzle"""

wordlist = ["APPLE", "PLEAS", "PLEASE"]
puzzles = ["AELWXYZ", "AELPXYZ", "AELPSXY", "SAELPXY", "XAELPSY"]


def spellingBeeSolutions(wordlist, puzzles):
    """Count the number of valid words contained in each puzzle"""
    counter = []
    word_counter = 0

    for puzzle in puzzles:

        for word in wordlist:

            if len(word) < 5 or puzzle[0][0] not in word:
                word_counter += 0
            elif not set(word).issubset(set(puzzle)):
                word_counter += 0

            else:
                word_counter += 1

        counter.append(word_counter)

        word_counter = 0
    return counter


print(spellingBeeSolutions(wordlist, puzzles))
