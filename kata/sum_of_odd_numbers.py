"""Sum of Odd Numbers."""


def row_sum_odd_numbers(n):
    """Math to get solution."""
    total = (n * (n-1) + 1) * (n + 1) - 1
    return total
