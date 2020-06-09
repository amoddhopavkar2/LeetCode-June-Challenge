# PROBLEM STATEMENT - Is Subsequence
# Given a string s and a string t, check if s is subsequence of t.

class Solution(object):
    def isSubsequence(self, s, t):
        len_1 = len(s)
        len_2 = len(t)

        i = 0
        j = 0

        while i < len_1 and j < len_2:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        if i == len_1:
            return True
        return False