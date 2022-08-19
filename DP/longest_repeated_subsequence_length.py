def LRSLength(X, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m-1] == X[n-1] and m != n:
        return 1 + LRSLength(X, m - 1, n - 1)
    return max(LRSLength(X, m, n - 1), LRSLength(X, m - 1, n))