I'm given a list of words and a list of puzzles. I need to see how many valid words I can generate with each puzzle. 

Each string of letters in the "puzzles" list is a puzzle; I'm comparing each puzzle with the words in the word list to see how many valid words there are in each puzzle.

There are several constraints for a word to be valid: words must be at least 5 letters; words contain the key letter (which is the first letter of the puzzle word); words can't include letters outside of puzzle letters.