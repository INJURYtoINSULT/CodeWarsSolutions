def seven(m, count=0):
    y = m % 10
    x = (m - y)//10
    z = (x - (2 * y))
    if m == 0:
        return m, count
    elif z < 100:
        return z, count + 1
    else:
        return seven(z, count + 1)
