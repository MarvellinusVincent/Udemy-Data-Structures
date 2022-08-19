my_list = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def unique(lst):
    # dic = {}
    # for num in lst:
    #     if num not in dic:
    #         dic[num] = 1
    #     else:
    #         return False
    # return True
    res = []
    for num in lst:
        if num in res:
            return False
        else:
            res.append(num)
    return True