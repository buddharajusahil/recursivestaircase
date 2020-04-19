
# Code prints the resulting amount
# dp is the dynamic programming table


# Number of steps on the staircase
N = 6

# Array of all the possible steps you can take
# For this example, you can take 1, 3, or 5 steps at a time
steps = [1, 3, 5]



steps.sort()

def dstair(N, steps):
	dp = [ [0] * (N + 1) for _ in range(len(steps))]

	for y in range(0, len(steps)):
		for x in range(0, N + 1):
			if x == 0:
				dp[y][x] = 1
			elif steps[y] > x:
				if x == 0:
					dp[y][x] = 0
				else:
					dp[y][x] = dp[y - 1][x]
			elif steps[y] <= x:
				for i in range(0, y + 1):
					dp[y][x] += dp[y][x - steps[i]]

	print(dp[len(steps) - 1][N])

dstair(N, steps)