"""Reverse an integer."""


def reverse(x):
    """Reverse input X."""
    ab_temp = abs(x)
    if x:
        collection = []
        while x:
            digit = x % 10
            x //= 10
            collection.append(digit)
        return collection

    if -x:
        collection = []
        while ab_temp:
            digit = ab_temp % 10
            ab_temp //= 10
            collection.append(digit)
        return collection


print(reverse(8738))
