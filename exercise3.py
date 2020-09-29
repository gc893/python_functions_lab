def occurances(str, char):
    letters = list(str)
    counter = 0
    for letter in letters:
        if letter == char:
            counter +=1
    print(counter)

occurances('hello', 'l')