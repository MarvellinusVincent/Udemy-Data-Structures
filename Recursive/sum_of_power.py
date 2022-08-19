def power(base, exp):
    assert exp >= 0 and int(exp) == exp
    if exp == 0:
        return base
    return base * power(base, exp - 1)