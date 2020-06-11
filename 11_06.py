# PROBLEM STATEMENT - Given an array with n objects colored red, white or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for x in nums:
            count[x] += 1

        for i in range(count[0]):
            nums[i] = 0

        for i in range(count[0], count[1] + count[0]):
            nums[i] = 1

        for i in range(count[1] + count[0], count[2] + count[1] + count[0]):
            nums[i] = 2