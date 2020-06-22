# PROBLEM STATEMENT - Dungeon Problem
# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
# The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially 
# positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

class Solution:
	def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
		DP = [float('inf') for _ in dungeon[0]]
		DP[-1] = 1

		for i in reversed(range(len(dungeon))):
			DP[-1] = max(DP[-1] - dungeon[i][-1], 1)
			for j in reversed(range(len(dungeon[i]) - 1)):
				min_HP = min(DP[j], DP[j + 1])
				DP[j] = max(min_HP - dungeon[i][j], 1)

		return DP[0]