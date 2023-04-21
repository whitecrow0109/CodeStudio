def findLargestMinDistance(boards:list, k:int):

    def can(T):
        now, cnt = 0, 1
        for i in range(len(boards)):
            if boards[i] > T:
                return 0
            now += boards[i]
            if now > T:
                cnt += 1
                now = boards[i]
        return cnt <= k
        
    lo, hi = 1, 1000000000
    while lo + 1 < hi:
        mid = lo + hi >> 1
        if can(mid):
            hi = mid
        else:
            lo = mid
    return lo if can(lo) else hi