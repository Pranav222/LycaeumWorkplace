"""Write a function called smallest_in which takes a list of numbers l
and returns the smallest number in the list."""

def smallest_in(l):
    b = l[0]
    for i in l:
        if i < b:
            b = i
    print (b)
