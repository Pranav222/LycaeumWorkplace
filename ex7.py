"""Write a functmion called biggest_in which takes a list of numbers l
and returns the largest number in the list."""

def biggest_in(l):
    b = l[0]
    for i in l:
        if i > b:
            b = i
    print (b)
