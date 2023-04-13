def kthSmallLarge(arr, n, k):
    arr.sort()
    return arr[k - 1], arr[n - k]