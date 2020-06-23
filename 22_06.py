# PROBLEM STATEMENT - Single Number II
# Given a non-empty array of integers, every element appears three times 
# except for one, which appears exactly once. Find that single one.

# NOTE - Your algorithm should have a linear runtime complexity.

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		one, two, three = 0, 0, 0
		for x in nums:
			two |= one & x
			one ^= x
			three = one & two
			one &= ~three
			two &= ~three
		return one