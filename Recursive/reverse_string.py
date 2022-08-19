def reverse(strng):
    if len(strng) == 0:
        return strng
    return strng[len(strng) - 1] + reverse(strng[0:len(strng) - 1])