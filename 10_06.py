# PROBLEM STATEMENT - Search Insert Position
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
                elif nums[i] < target:
                    if i == len(nums) - 1:
                        return i+1
                    elif nums[i + 1] > target:
                        return i+1