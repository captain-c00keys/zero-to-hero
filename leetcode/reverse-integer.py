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

# sencond try 
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = 0
        while x:
            digit = x % 10
            x //= 10
            temp.append(digit)
            
            temp = rev * 10 + pop;
        rev = temp;