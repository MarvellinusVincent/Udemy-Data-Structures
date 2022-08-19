# Top Down approach
def numberfactor(n):
    dic = {}
    def helper(n):
        if n == 0 or n == 1 or n ==2:
            return 1
        if n == 3:
            return 2
        elif n in dic:
            return dic[n]
        else:
            rec1 = helper(n - 1)
            rec2 = helper(n - 3)
            rec3 = helper(n - 4)
            dic[n] = rec1 + rec2 + rec3
            return dic[n]
    return helper(n)
print(numberfactor(7))

# Bottom Up approach
def numberfactor(n):
    res = [1, 1, 1, 2]
    for i in range(4, n + 1):
        res.append(res[i - 1] + res[i - 3] + res[i - 4])
    return res[n]
print (numberfactor(7))