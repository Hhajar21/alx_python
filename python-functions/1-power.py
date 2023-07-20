def pow(a, b):
    if a == 0 and b < 0:
        raise ValueError("Cannot raise 0 to a negative power")

    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result

