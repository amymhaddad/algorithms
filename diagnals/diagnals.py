""""Given a square matrix, calculate the absolute difference between the sums of its diagonals."""

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def sum_diagonal_1(arr):
    """Sum the numbers for diagnal 1, which starts at the top left of the matrix."""
    diagonal_1 = 0
    for i, row in enumerate(arr):
        diagonal_1 += row[i]
    return diagonal_1


def sum_diagonal_2(arr):
    """Sum the numbers for diagnal 2, which starts at the top right of the matrix."""
    diagonal_2 = 0
    for i, row in enumerate(arr):
        diagonal_2 += row[-i - 1]
    return diagonal_2


def absolute_difference():
    """Return the absolute difference between the sum of diagonals 1 and 2"""
    return abs(sum_diagonal_1(arr) - sum_diagonal_2(arr))
