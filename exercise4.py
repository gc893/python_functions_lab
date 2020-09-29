def product(*args):
    result = 1
    for n in args:
        result *= n
    
    if len(args) <1:
        result = 0
    
    print(result)

product(1,2,3)