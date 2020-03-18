def seven(m, count=0):
    y = m % 10
    x = (m - y)//10
    z = (x - (2 * y))
    print(x, y, z)
    if m == 0:
        return (m, count)
    if z % 7 == 0 and z < 100:
        print(z % 7, z)
        return (z, count + 1)
    elif z < 100:
        return (z, count + 1)
    else:
        return seven(z, count + 1)
