# Top Down approach
def findMinOperation(s1, s2, index1, index2):
    dic = {}
    def helper(s1, s2, index1, index2):
        if index1 == len(s1):
            return len(s2)-index2
        if index2 == len(s2):
            return len(s1)-index1
        if s1[index1] == s2[index2]:
            return helper(s1, s2, index1+1, index2+1)
        else:
            key = str(index1) + str(index2)
            if key not in dic:
                deleteOp = 1 + helper(s1, s2, index1, index2+1)
                insertOp = 1 + helper(s1, s2, index1+1, index2)
                replaceOp = 1 + helper(s1, s2, index1+1, index2+1)
                dic[key] = min(deleteOp, insertOp, replaceOp)
            return dic[key]
    return helper(s1, s2, index1, index2)

print(findMinOperation("table", "tbrltt", 0, 0))

# Bottom Up approach
def findMinOperation(s1, s2):
    dic = {}
    def helper(s1, s2):
        for i1 in range(len(s1)+1):
            dictKey = str(i1)+'0'
            dic[dictKey] = i1
        for i2 in range(len(s2)+1):
            dictKey = '0'+str(i2)
            dic[dictKey] = i2
        
        for i1 in range(1,len(s1)+1):
            for i2 in range(1,len(s2)+1):
                if s1[i1-1] == s2[i2-1]:
                    dictKey = str(i1)+str(i2)
                    dictKey1 = str(i1-1)+str(i2-1)
                    dic[dictKey] = dic[dictKey1]
                else:
                    dictKey = str(i1)+str(i2)
                    dictKeyD = str(i1-1)+str(i2)
                    dictKeyI = str(i1)+str(i2-1)
                    dictKeyR = str(i1-1)+str(i2-1)
                    dic[dictKey] = 1 + min(dic[dictKeyD], min(dic[dictKeyI],dic[dictKeyR]))
        dictKey = str(len(s1))+str(len(s2))
        return dic[dictKey]
    return helper(s1, s2)
print(findMinOperation("table", "tbrltt"))