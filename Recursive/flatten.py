def flatten(arr):
    result = []
    for each in arr:
        if type(each) is list:
            result.extend(flatten(each))
        else:
            result.append(each)
    return result