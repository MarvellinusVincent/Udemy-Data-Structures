def LCS(X, Y, m, n, T):
    if m == 0 or n == 0:
        return str()
    if X[m - 1] == Y[n - 1]:
        return LCS(X, Y, m - 1, n - 1, T) + X[m - 1]
    if T[m - 1][n] > T[m][n - 1]:
        return LCS(X, Y, m - 1, n, T)
    else:
        return LCS(X, Y, m, n - 1, T)

def LCSLength(X, Y, m, n, T):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
 
 
X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)
T = [[0 for x in range(n + 1)] for y in range(m + 1)]
LCSLength(X, Y, m, n, T)
print(LCS(X, Y, m, n, T))
