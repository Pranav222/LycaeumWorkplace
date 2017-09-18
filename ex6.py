""" Write a function called biggest3 which takes three numerical arguments
a , b and c and returns the larger of the three """ 


def biggest3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
