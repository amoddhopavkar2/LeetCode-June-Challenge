# PROBLEM STATEMENT - Permutation Sequence
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        k = k - 1
        fact = math.factorial(n - 1)
        
        permutation = [i for i in range(1, n + 1)]
        for i in reversed(range(n)):
            index = floor(k / fact)
            current = permutation[index]
            result += str(current)
            permutation.remove(current)
            
            if i > 0:
                k %= fact
                fact /= i
        
        return result