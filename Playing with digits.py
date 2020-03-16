def dig_pow(n, p):
    digits = []
    for d in str(n):
        digits.append(d)

    sum = 0
    for dig in digits:
        sum = sum + (int(dig) ** p)
        p = p + 1

    multiplier = sum / n
    if (sum % n == 0):
        return multiplier
    else:
        return -1
