from sys import stdin

def getProductArrayExceptSelf(arr, n) :
    MOD = 10 ** 9 + 7
    ret, zero = 1, 0
    for i in range(n):
        if arr[i] == 0:
            zero += 1
        else:
            ret *= arr[i]
    lst = []
    for i in range(n):
        if arr[i] == 0:
            if zero == 1:
                lst.append(ret)
            else:
                lst.append(0)
        else:
            if zero >= 1:
                lst.append(0)
            else:
                lst.append(ret * pow(arr[i], MOD - 2, MOD) % MOD)
    return lst