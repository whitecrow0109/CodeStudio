MOD = 1000000007

def sumInRanges(arr, n, queries, q):
    ans, thisSum = [], [0] * (n + 5)
    oneSum = sum(arr)
    for i in range(n):
        thisSum[i + 1] = thisSum[i] + arr[i]
    for i in range(q):
        L, R = queries[i][0], queries[i][1]
        L -= 1
        l, r = L % n, R % n
        sumVal = (R // n - L // n) * oneSum
        ans.append((sumVal + thisSum[r] - thisSum[l]) % MOD)
    return ans

for _ in range(int(input().strip())):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().strip().split(" "))))
    print(" ".join(str(x) for x in sumInRanges(arr, n, queries, q)))