# PROBLEM STATEMENT - Unique Binary Search Tree
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

class Solution:
    def numTrees(self, n: int) -> int:
        counts = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]