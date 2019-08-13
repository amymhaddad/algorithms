"""Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line."""
arr = [-4, 3, -9, 0, 4, 1]


def number_type(arr):
    """Find the total number of each number type"""

    total_positive_numbers = 0
    total_negative_numbers = 0
    total_zero_numbers = 0

    for number in arr:
        if number > 0:
            total_positive_numbers += 1
        elif number < 0:
            total_negative_numbers += 1
        else:
            total_zero_numbers += 1
    return sorted(
        [total_positive_numbers, total_negative_numbers, total_zero_numbers],
        reverse=True,
    )


def list_fractional_elements():
    """Find the fractional element for each number type"""
    sorted_number_type = number_type(arr)

    fractional_number = []
    for number in sorted_number_type:
        ratio = number / len(arr)
        rounded_numbers = f"{ratio:.6f}"
        fractional_number.append(rounded_numbers)
    return fractional_number


def plusMinus():
    """Diplay each number on a separate line"""
    for number in list_fractional_elements():
        print(number)
