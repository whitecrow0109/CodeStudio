def maximizeScore(arr,n,k):
    x = [0]
    for i in range(n):
        x.append(x[i] + arr[i])
    ans = 0
    for i in range(0, k + 1):
        ans = max(ans, x[i] + x[n] - x[n - k + i])
    return ans
    
