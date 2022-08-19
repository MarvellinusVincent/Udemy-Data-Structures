def SCSLength(X, Y, m, n):
	if m == 0 or n == 0:
		return n + m
	if X[m - 1] == Y[n - 1]:
		return SCSLength(X, Y, m - 1, n - 1) + 1
	return min(SCSLength(X, Y, m, n - 1) + 1, SCSLength(X, Y, m - 1, n) + 1)