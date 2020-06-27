class Solution:
	def numSquares(self, n: int) -> int:
		dp = [2 ** 32] * (n + 1)
		for i in range(1, n+1):
			if math.sqrt(i) - int(math.sqrt(i)) == 0:
				dp[i] = 1
			else:
				j = 1
				while j * j <= i:
					dp[i] = min(dp[i], dp[i-j*j] + 1)
					j += 1
		return dp[n]