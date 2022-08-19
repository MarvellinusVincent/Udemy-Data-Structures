def LCSLength(S1, S2, lenS1, lenS2):
    if lenS1 == 0 or lenS2 == 0:
        return 0
    if S1[lenS1 - 1] == S2[lenS2 - 1]:
        return 1 + LCSLength(S1, S2, lenS1 - 1, lenS2 - 1)
    return max(LCSLength(S1, S2, lenS1, lenS2 - 1), LCSLength(S1, S2, lenS1 - 1, lenS2))