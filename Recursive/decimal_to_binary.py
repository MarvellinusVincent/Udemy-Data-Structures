def db(decimal):
    if decimal == 0:
        return 1
    return decimal % 2 + 10 * db(int(decimal/2))
