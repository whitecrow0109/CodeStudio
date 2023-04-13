def collidingAsteroids(asteroids:list):
    n = len(asteroids)
    ans = []
    for i in range(n):
        x = asteroids[i]
        if len(ans) == 0 or x >= 0:
            ans.append(x)
        else:
            while True:
                m = len(ans)
                if m == 0 or ans[m - 1] < 0:
                    ans.append(x)
                    break
                elif ans[m - 1] == abs(x):
                    ans.pop()
                    break
                elif ans[m - 1] < abs(x):
                    ans.pop()
                elif ans[m - 1] > abs(x):
                    break
    return ans