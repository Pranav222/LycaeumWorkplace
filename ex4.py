"""Write a function called tables which takes two arguments m and n. It
should print the multiplication tables of m from 1 to n."""

def tables(m,n):
    for i in range(1,n+1):
        mul = (m * i)
        print(f"{m} * {i} = {mul}")
