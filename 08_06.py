# PROBLEM STATEMENT - Power of Two
# Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True