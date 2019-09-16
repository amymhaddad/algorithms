DAYS = ["none", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

VERSE_PHRASES = {
    1: "a Partridge in a Pear Tree.",
    2: "two Turtle Doves, ",
    3: "three French Hens, ",
    4: "four Calling Birds, ",
    5: "five Gold Rings, ",
    6: "six Geese-a-Laying, ",
    7: "seven Swans-a-Swimming, ",
    8: "eight Maids-a-Milking, ",
    9: "nine Ladies Dancing, ",
    10: "ten Lords-a-Leaping, ",
    11: "eleven Pipers Piping, ",
    12: "twelve Drummers Drumming, ",
}


def recite(start_verse, end_verse):
    """Return the verses for the "Twelve Days of Christmas" song"""

    return [select_verses(number) for number in range(start_verse, end_verse + 1, 1)]


def select_verses(number):
    """Algorithm to get the correct verses for the "Twelve Days of Christmas" song"""

    day_number = DAYS[number]
    verses = ""
    verses += f"On the {day_number} day of Christmas my true love gave to me: "

    for day in reversed(range(1, number + 1)):
        second_clause = VERSE_PHRASES[day]

        if day == 1 or day > 2:
            verses += second_clause
        elif day == 2:
            verses += second_clause + "and "
    return verses
