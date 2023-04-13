from typing import *

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[0, 0, 0]] * (n + 1)
    for i in range(1, n + 1):
        x, y, z = dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]
        dp[i][0] = max(y, z) + points[i - 1][0]
        dp[i][1] = max(x, z) + points[i - 1][1]
        dp[i][2] = max(x, y) + points[i - 1][2]
    return max(max(dp[n][0], dp[n][1]), dp[n][2])