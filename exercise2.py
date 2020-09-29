def largest(li):
    max = 0
    for item in li:
        if item > max:
            max = item
    print(max)

largest([1,3,5,4,2,0])