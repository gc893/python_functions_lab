def sum_to(n):
    sum = 0
    for num in [item for item in range(1, n+1, 1)]:
        sum += num
    print(sum)

sum_to(4)