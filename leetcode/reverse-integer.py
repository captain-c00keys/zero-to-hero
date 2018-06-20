"""Reverse an integer."""


def reverse(x):
    """Reverse input X."""
    temp = x
    collection = []
    while temp:
        digit = temp % 10
        temp //= 10
        collection.append(digit)
    return ','.join(collection)


print(reverse(8738))
