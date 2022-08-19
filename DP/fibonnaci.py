# Top Down approach
def fibTD(n):
    dic = {}
    def helper(n):
        if n == 1 or n == 2:
            return 1
        if n not in dic:
            dic[n] = helper(n - 1) + helper(n - 2)
        return dic[n]
    return helper(n)
print (fibTD(10))

# Bottom Up approach
def fibBU(n):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n]
print (fibBU(10))

# Iterative approach
def fibIter(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b
print (fibIter(10))