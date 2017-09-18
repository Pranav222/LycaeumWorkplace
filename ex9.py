"""Write a function called fizzbizz which takes an integer argument n.
It should print numbers from 1 to n with the following conditions.
 if the number is divisible by 3, it should print fizz
 if the number is divisible by 5, it should print bizz
 if the number is divisible by 15, it should print fizzbizz
 Otherwise, just print the number."""

def fizzbizz(n):
    a = range(1,n+1)
    for i in a:
        if i % 15 ==0:
            print ("fizzbizz")
        elif i % 5 ==0:
            print ("bizz")
        elif i % 3 ==0:
            print("fizz")
        else:
            print(i)
