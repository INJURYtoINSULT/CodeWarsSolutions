def solution(number):
    sum = 0
    for num in range(0, number):
        if (num % 3 == 0 or num % 5 == 0):
           sum += num
    return sum

