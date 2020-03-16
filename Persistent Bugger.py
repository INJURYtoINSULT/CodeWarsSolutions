def persistence(n):
    return splitter(n, 0)


def splitter(num, count):
    digit_list = [int(digit) for digit in str(num)]

    if num > 9:
        mult = 1
        for digit in digit_list:
            mult = mult * digit
        return splitter(mult, count + 1)
    else:
        return count
