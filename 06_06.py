# PROBLEM STATEMENT - Queue Reconstruction by Height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        answer = []
        
        for x in people:
            answer.insert(x[1], x)
        return answer