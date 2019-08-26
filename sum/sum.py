WORDS = ["a", "neat", "beat", "house", "me", "button", "mat"]


def tuple_of_word_lengths():
    """Return a tuple with the length of the shortest word,
    the length of the longest word, and the average word length."""

    longest_word = max(WORDS, key=len)
    shortest_word = min(WORDS, key=len)
    average = (len(longest_word) + len(shortest_word)) // 2

    return (shortest_word, longest_word, average)


print(tuple_of_word_lengths())
