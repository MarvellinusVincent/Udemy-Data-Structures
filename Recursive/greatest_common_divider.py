def gcd(num1, num2):
    if num1 < 0:
        num1 = abs(num1)
    if num2 < 0:
        num2 = abs(num2)
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)
