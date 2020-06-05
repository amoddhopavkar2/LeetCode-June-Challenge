# PROBLEM STATEMENT - Random Pick with Weight

class Solution:
    
    def __init__(self, w: List[int]):
        self.data = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.data, random.randint(1, self.data[-1]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()