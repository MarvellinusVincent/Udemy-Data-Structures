def sum_of_digits(n):
    if n == 0:
        return n
    return n % 10 + sum_of_digits(n // 10)