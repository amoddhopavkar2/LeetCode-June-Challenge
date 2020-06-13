# PROBLEM STATEMENT - Largest Divisible Subset
# Given a set of distinct positive integers, 
# find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        pointer = [1] * len(nums)
        prev = [-1] * len(nums)
        largest_index = 0
        result = []
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if pointer[i] < pointer[j] + 1:
                        pointer[i] = pointer[j] + 1
                        prev[i] = j
                        
            if pointer[largest_index] < pointer[i]:
                largest_index = i
                
        i = largest_index
        while i != -1:
            result.append(nums[i])
            i = prev[i]
            
        return result[::-1]