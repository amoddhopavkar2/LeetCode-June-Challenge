# PROBLEM STATEMENT - Coin Change 2

class Solution:
	def change(self, amount:int, coins: List[int]) -> int:
		size = len(coins)

		arr = [[0] * (amount + 1) for x in range(size + 1)]

		for i in range(size + 1):
			arr[i][0] = 1

		for i in range(1, size + 1):
			for j in range(1, amount + 1):
				if coins[i - 1] > j:
					arr[i][j] = arr[i - 1][j]
				else:
					arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]

		return arr[size][amount]